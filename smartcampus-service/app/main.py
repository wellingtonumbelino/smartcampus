from fastapi import FastAPI
from app.interfaces.http.controllers.pddl_controller import router as pddl_router
from app.interfaces.http.controllers.planner_controller import router as planner_router
from app.infrastructure.pddl.plan_parser import PDDLPlanParser
from app.infrastructure.scheduler.apscheduler_impl import APSchedulerImpl
from datetime import datetime, timezone
import os
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
  # startup
  try:
    with open("data/plan.pddl", "r", encoding="utf-8") as f:
      pddl_content = f.read()

    reference_date = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)

    parser = PDDLPlanParser()
    actions = parser.parse_file(pddl_content, reference_date)

    base_url = os.getenv("THIRD_PARTY_BASE_URL", "http://localhost:8000")
    api_key = os.getenv("THIRD_PARTY_API_KEY")
    app.state.schedular = APSchedulerImpl(base_url=base_url, api_key=api_key)
    app.state.schedular.schedule_many(actions)
    
  except FileNotFoundError:
    pass
  
  yield
  
  # shutdown
  if getattr(app.state, "schedular", None):
    import asyncio
    asyncio.run(app.state.schedular.shutdown())

app = FastAPI(title="Smart Campus Service", lifespan=lifespan)

app.include_router(pddl_router)
app.include_router(planner_router)