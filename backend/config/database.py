from typing import Optional

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pydantic_settings import BaseSettings

uri = "mongodb+srv://garethong85867545:TKrtvZSe6GMhDHKJ@cluster0.5ftuawz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

class Settings(BaseSettings):
    # database configurations
    MONGO_URL: Optional[str] = None

    class Config:
        env_file = ".env"
        from_attributes = True
   
client = MongoClient(Settings().MONGO_URL, server_api=ServerApi('1'))