from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient

from ..logging import LOGGER
from config import MONGO_DB_URI


LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    _mongo_async_ = _mongo_client_(MONGO_DB_URI)
    _mongo_sync_ = MongoClient(MONGO_DB_URI)
    mongodb = _mongo_async_.AnonX
    pymongodb = _mongo_sync_.AnonX
    LOGGER(__name__).info("Connected to your Mongo Database.")
except:
    raise SystemExit("Failed to connect to your Mongo Database. Please check your MONGO_DB_URI and try again.")
