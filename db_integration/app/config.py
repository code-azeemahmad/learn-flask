import os
from dotenv import load_dotenv

load_dotenv()   # Read the .env file and load its contents into the environment.

class Config:
    DEBUG = True
    SECRET_KEY = str(os.getenv("SECRET_KEY"))   # that environment contains those values, you can ask for one.

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True


'''
Configuration is information that controls how your 
application behaves without changing the source code.

Development vs Production

Imagine a user causing an exception.
Debug mode may expose:

File paths
Source code
Installed packages
Environment details

That's a security risk.
'''
