import os

class Config:
    DEBUG = False
    PORT = os.environ.get('PORT') or 5000
    ENV = os.environ.get('ENV')

class Development(Config):
    DEBUG = True

class Production(Config):
    DEBUG = False
    PORT = os.environ.get('PORT') or 8080