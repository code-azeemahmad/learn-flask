import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = True
    SECRET_KEY = str(os.getenv("SECRET_KEY"))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
