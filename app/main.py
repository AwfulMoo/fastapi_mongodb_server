from fastapi import FastAPI

from app.routers import users, tasks
from app.core.db import mongodb_utils

app = FastAPI(
    title="fastapi_mongo_server",
    description="FastApi and Mongo Connetion server template",
    version="1.0.0",
    docs_url="/"
)

app.add_event_handler("startup", mongodb_utils.connect_to_mongo)
app.add_event_handler("shutdown", mongodb_utils.close_mongo_connection)
app.include_router(users.router)
app.include_router(tasks.router)
