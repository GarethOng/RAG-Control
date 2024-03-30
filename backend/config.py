from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # database configurations
    MONGO_URL: Optional[str] = None
    # openai configurations
    OPENAI_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"
        from_attributes = True