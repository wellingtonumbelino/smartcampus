import asyncio
import logging
import httpx

logger = logging.getLogger(__name__)

async def send_action(client: httpx.AsyncClient, device_id: str, command: str, duration: float, api_key: str = None):
  url = f"/device/{device_id}/control"
  payload = {"command": command, "duration": duration}
  headers = {"Authorization": f"Bearer {api_key}"} if api_key else None

  for attempt in range(3):
    try:
      response = await client.post(url, json=payload, headers=headers)
      response.raise_for_status()
      logger.info("Sent action %s to %s: %s", command, device_id, response.status_code)
      return response
    
    except Exception as e:
      logger.warning("Attempt %d failed sending to %s: %s", attempt + 1, device_id, e)
      await asyncio.sleep(2 ** attempt)
    
    raise RuntimeError("Failed to send action after retries")