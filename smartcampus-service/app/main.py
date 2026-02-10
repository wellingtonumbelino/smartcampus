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
  from app.interfaces.http.dependencies import get_scheduler, _parser_instance

  scheduler = get_scheduler()
  parser = PDDLPlanParser()

  try:
    with open("data/plan.pddl", "r", encoding="utf-8") as f:
      pddl_content = f.read()

    reference_date = datetime.now(timezone.utc).replace(hour=7, minute=0, second=0, microsecond=0)

    actions = parser.parse_file(pddl_content, reference_date)

    scheduler.schedule_many(actions)
    app.state.scheduler = scheduler   
    
  except FileNotFoundError:
    print("plan.pddl file not found. Scheduler will not be initialized.")
  
  yield
  
  if hasattr(app.state, "scheduler"):
    await app.state.scheduler.shutdown()

app = FastAPI(title="Smart Campus Service", lifespan=lifespan)

app.include_router(pddl_router)
app.include_router(planner_router)