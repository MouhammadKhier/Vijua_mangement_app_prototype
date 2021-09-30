import os


class BaseConfig:
    # SERVER_NAME = 'http://127.0.0.1:5000/'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    SECRET_KEY = "thisIsSecret"


class DevelopmentConfig(BaseConfig):
    DATABASE_URI = "mongodb+srv://Prototype:123456789123456789@prototype.38psx.mongodb.net/Prototype?retryWrites=true&w=majority"
    DATABASE_NAME = "Prototype"
    ENV = 'development'
    DEBUG = True


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    DATABASE_URI = "mongodb+srv://Prototype:123456789123456789@prototype.38psx.mongodb.net/Prototype?retryWrites=true&w=majority"
    DATABASE_NAME = "Prototype"