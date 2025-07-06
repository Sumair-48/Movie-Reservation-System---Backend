from pydantic_settings import BaseSettings
from dotenv import find_dotenv, load_dotenv

dot_env = find_dotenv()

load_dotenv(dot_env)

class Settings(BaseSettings):
    database_url : str

    class Config:
        env_file = ".env"

# Create an instance
settings = Settings()