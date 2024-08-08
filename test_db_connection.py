import sqlalchemy
from sqlalchemy import create_engine, text
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
engine = create_engine(settings.database_url)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print(result.fetchone())
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
