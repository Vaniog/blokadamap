import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(BaseSettings):
    DATABASE_URL: str = os.environ.get("DATABASE_URL")


config = Config()
