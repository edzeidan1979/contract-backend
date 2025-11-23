from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.contracts import router as contracts_router
from .routes.chat import router as chat_router
from .routes.schedules import router as schedules_router
from .scheduler import start_scheduler
from .db import init_db

app = FastAPI(title="Contract Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contracts_router, prefix="/contracts")
app.include_router(chat_router, prefix="/chat")
app.include_router(schedules_router, prefix="/schedules")

@app.on_event("startup")
async def startup_event():
    init_db()
    start_scheduler()

