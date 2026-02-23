from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .scheduler_interface import IScheduler
from app.domain.entities.plan import ScheduleAction
import httpx
import logging
import asyncio

class APSchedulerImpl(IScheduler):
  def __init__(self, base_url: str = None, api_key: str = None, client: httpx.AsyncClient = None, timezone="UTC"):
    self.logger = logging.getLogger(__name__)
    self.base_url = base_url or "http://localhost:8000"
    self.api_key = api_key or "test-api-key"

    try:
      loop = asyncio.get_running_loop()

    except RuntimeError:
      loop = None

    if loop is not None:
      self.scheduler = AsyncIOScheduler(event_loop=loop, timezone=timezone)
    else:
      self.scheduler = AsyncIOScheduler(timezone=timezone)

    self._client_provided = client is not None
    self.client = client or httpx.AsyncClient(base_url=self.base_url, timeout=10.0)
    self.scheduler.start()

  async def _execute_iot_call(self, action: ScheduleAction):
     self.logger.info("Executing action %s for device %s at %s", action.action_name, action.target_device_id, action.execution_time)

     if action.command == "UNKNOWN":
      self.logger.warning("Unknown command for action %s, skipping", action.action_name)
      return

     try:
       url = f"/device/{action.target_device_id}/control"
       payload = {"command": action.command, "duration": action.duration}
       headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else None

       for attempt in range(3):
         response = await self.client.post(url, json=payload, headers=headers)

         if response.status_code < 400:
           self.logger.info("Action %s executed successfully: %s", action.action_name, response.status_code)
           break
         else:
           self.logger.warning("Attempt %d failed: %s", attempt + 1, response.status_code)
           await asyncio.sleep(2 ** attempt)
       else:
         self.logger.error("Failed to call external API for action %s", action.action_name)

     except Exception:
       self.logger.exception("Error calling external API")

  def schedule_action(self, action: ScheduleAction):
    job_id = f"{action.action_name}:{action.target_device_id}:{action.execution_time.isoformat()}"
    
    self.scheduler.add_job(
      self._execute_iot_call,
      'date',
      run_date=action.execution_time,
      args=[action],
      id=job_id,
      replace_existing=True
    )

  def schedule_many(self, actions: list[ScheduleAction]):
    for action in actions:
      self.schedule_action(action)

  def clear_all_jobs(self):
    """Remove all pending appointments from the scheduler."""
    try:
      self.scheduler.remove_all_jobs()
      self.logger.info("All scheduled jobs have been cleared.")
    except Exception as e:
      self.logger.error(f"Error clearing scheduled jobs: {e}")

  def get_scheduled_jobs(self):
    """Return a list of all currently scheduled jobs."""
    jobs = self.scheduler.get_jobs()
    job_list = []
    for job in jobs:
      job_list.append({
        "id": job.id,
        "next_run_time": job.next_run_time.isoformat() if job.next_run_time else None,
        "function": job.func.__name__,
        "args": str(job.args),
      })
    return job_list
  
  async def shutdown(self):
    self.logger.info("Shutting down scheduler")
    self.scheduler.shutdown(wait=False)

    if not self._client_provided:
      await self.client.aclose()