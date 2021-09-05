from motor.motor_asyncio import AsyncIOMotorClient
from app.settings import MongoDBConfig
from app.core.db.mongodb import db


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(
        host=MongoDBConfig.host,
        port=MongoDBConfig.port,
        connect=True
    )
    print(
        f"Conencted to {MongoDBConfig.host}:{MongoDBConfig.port}. Database: {MongoDBConfig.db}"
    )


async def close_mongo_connection():
    db.client.close()
