from bson import ObjectId
from typing import List
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi_mongo_server.core.models.task_model import TaskModel
from fastapi_mongo_server.core.db.mongodb import get_database

router = APIRouter(
    prefix="/tasks"
)


@router.get("/", response_model=List[TaskModel], response_description="List all tasks")
async def list_tasks(db: AsyncIOMotorDatabase = Depends(get_database)):
    # tasks is the MongoDB collection
    tasks = await db.tasks.find().to_list(1000)
    return tasks


@router.get("/{id}", response_model=TaskModel, response_description="Return individual task")
async def get_task(id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    # tasks is the MongoDB collection
    task = await db.tasks.find_one({"_id": ObjectId(id)})
    return task
