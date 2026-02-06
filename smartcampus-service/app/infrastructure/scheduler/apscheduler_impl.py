from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .scheduler_interface import IScheduler
from app.domain.entities.plan import ScheduleAction
import httpx

class APSchedulerImpl(IScheduler):
  def __init__(self):
    self.scheduler = AsyncIOScheduler()
    self.scheduler.start()

  async def _execute_iot_call(self, action: ScheduleAction):
     print(f"--- Executing action: {action.action_name} on device {action.target_device_id} with command {action.command} for duration {action.duration} hours ---")

     async with httpx.AsyncClient() as client:
        try:
          url = f"https://api.terceira.com/device/{action.target_device_id}/control"
          payload = {"command": action.command}
          await client.post(url, json=payload)

        except Exception as e:
          print(f"Error calling external API: {e}")

  def schedule_action(self, action: ScheduleAction):
    self.scheduler.add_job(
      self._execute_iot_call,
      'date',
      run_date=action.execution_time,
      args=[action],
      id=f"{action.target_device_id}_{action.execution_time.timestamp()}"
    )

  def schedule_many(self, actions: list[ScheduleAction]):
    for action in actions:
      self.schedule_action(action)