from bson import ObjectId
from typing import List
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi_mongo_server.core.models.user_model import UserModel
from fastapi_mongo_server.core.db.mongodb import get_database

router = APIRouter(
    prefix="/users"
)


@router.get("/", response_model=List[UserModel], response_description="List all users")
async def list_users(db: AsyncIOMotorDatabase = Depends(get_database)):
    # users is the MongoDB collection
    users = await db.users.find().to_list(1000)
    return users


@ router.get("/{id}", response_model=UserModel, response_description="Return individual user")
async def get_user(id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    # users is the MongoDB collection
    user = await db.users.find_one({"_id": ObjectId(id)})
    return user
