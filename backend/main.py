from fastapi import FastAPI
from typing import Optional

app = FastAPI()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pydantic_settings import BaseSettings

@app.get("/")
async def root():
    return {"message": "Hello World"}
 
 
class Settings(BaseSettings):
    # database configurations
    MONGO_URL: Optional[str] = None

    class Config:
        env_file = ".env"
        from_attributes = True

# Create a new client and connect to the server
client = MongoClient(Settings().MONGO_URL, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)