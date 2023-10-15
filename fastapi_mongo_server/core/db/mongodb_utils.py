from motor.motor_asyncio import AsyncIOMotorClient
from fastapi_mongo_server.settings import MongoDBConfig
from fastapi_mongo_server.core.db.mongodb import db


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(
        username=MongoDBConfig.username,
        password=MongoDBConfig.password,
        host=MongoDBConfig.host,
        port=MongoDBConfig.port,
        connect=True
    )
    print(
        f"Conencted to {MongoDBConfig.host}:{MongoDBConfig.port}. Database: {MongoDBConfig.database_name}"
    )


async def close_mongo_connection():
    db.client.close()
