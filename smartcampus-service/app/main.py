from fastapi import FastAPI
from app.interfaces.http.controllers.pddl_controller import router as pddl_router
from app.interfaces.http.controllers.planner_controller import router as planner_router

app = FastAPI(title="Smart Campus Service")

app.include_router(pddl_router)
app.include_router(planner_router)