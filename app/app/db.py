import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

DB_URL = os.getenv('MONGODB_URL')
DB_NAME = os.getenv('MONGO_INITDB_DATABASE')


class MongoDB:
    client: AsyncIOMotorClient = None
    database = None

    @classmethod
    async def connect(cls):
        cls.client = AsyncIOMotorClient(DB_URL)
        cls.database = cls.client[DB_NAME]
        print("✅ Connexion à MongoDB réussie!")

    @classmethod
    async def close(cls):
        cls.client.close()
        print("❌ Connexion à MongoDB fermée!")


db = MongoDB()
