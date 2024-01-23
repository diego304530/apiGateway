from flask import Flask
from dotenv import load_dotenv
import os
import json


class Config:

    def getApp():
        app = Flask("__name__")
        return app

    def getDatabaseConnection():
        load_dotenv()
        host = os.environ['DATABASE_HOST']
        port = os.environ['DATABASE_PORT']
        db = os.environ['DATABASE_NAME']
        return f'mongodb://{host}:{port}/{db}'

    def getConfigJson():
        with open('Config/config.json') as f:
            data = json.load(f)
        return data

    def getHeadersJson():
        return {"Content-Type": "application/json; charset=utf-8"}
