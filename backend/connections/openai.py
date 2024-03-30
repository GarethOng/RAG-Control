from typing import Optional
from pydantic_settings import BaseSettings
import openai
from config import Settings
        
openai.api_key = Settings().OPENAI_API_KEY

def generate_embedding(text: str) -> list[float]:

    response = openai.Embedding.create(
        model="text-embedding-ada-002", 
        input=text
    )
    return response['data'][0]['embedding']
