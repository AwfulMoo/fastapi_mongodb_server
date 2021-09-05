from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorClient
from app.settings import MongoDBConfig


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorDatabase:
    return db.client[MongoDBConfig.db]
