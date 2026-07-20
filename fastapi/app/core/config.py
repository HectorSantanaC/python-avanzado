from pydantic import BaseSettings

class Setting (BaseSettings):
  SECRET_KEY: str
  ALGORITHM: str = "HS256"
  ACCES_TOKEN_EXPIRE_MINUTES: int = 30
  DATABASE_URL: str

  class Config:
    env_file = ".env"

settings = Setting()