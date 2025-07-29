from pydantic_settings import BaseSettings
from dotenv import find_dotenv, load_dotenv
import os

dot_env = find_dotenv()

load_dotenv(dot_env)

class Settings(BaseSettings):
    database_url : str

    class Config:
        env_file = ".env.DATABASE_URL"

# Create an instance
settings = Settings()

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
refresh_key = os.getenv("REFRESH_SECRET_KEY")