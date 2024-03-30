from typing import Optional

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pydantic_settings import BaseSettings

from config import Settings
   
class MongoDBConnection:
   def __init__(self, db_name) -> None:
       self.client = None
       self.db = None
       self.db_name = db_name
   
   def connect(self) -> None:
      try:
         self.client = MongoClient(Settings().MONGO_URL, server_api=ServerApi('1'))
         self.db = self.client[self.db_name]
         print("Pinged your deployment. You successfully connected to MongoDB!")
      except Exception as e:
         print(e)
   
   def get_db(self, db_name: str) -> None:
      return self.db
   
   def close(self) -> None:
      if self.client:
         self.client.close()

# Create a new client and connect to the server
mongodb_client = MongoDBConnection('docs')
mongodb_client.connect()

