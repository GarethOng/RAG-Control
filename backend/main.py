import uvicorn
from fastapi import FastAPI
from typing import Optional

app = FastAPI()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pydantic_settings import BaseSettings

from connections.database import mongodb_client
from connections.openai import generate_embedding


@app.get("/")
async def root():
    return {"message": "Hello World"}   

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)