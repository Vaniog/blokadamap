import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "..", ".env"))


class Config(BaseSettings):
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB')
    POSTGRES_HOST: str = os.environ.get('POSTGRES_HOST')
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT") or 5432

    DATABASE_URL: str = \
        "postgresql://" + POSTGRES_USER + ":" + POSTGRES_PASSWORD + \
        "@" + POSTGRES_HOST + ":" + POSTGRES_PORT + "/" + POSTGRES_DB


config = Config()
