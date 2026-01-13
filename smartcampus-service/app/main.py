from fastapi import FastAPI
from app.interfaces.http.controllers.pddl_controller import router as pddl_router

app = FastAPI(title="Smart Campus Service")

app.include_router(pddl_router)