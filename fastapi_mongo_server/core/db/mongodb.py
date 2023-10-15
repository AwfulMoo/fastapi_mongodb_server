from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorClient
from fastapi_mongo_server.settings import MongoDBConfig


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorDatabase:
    return db.client[MongoDBConfig.database_name]
