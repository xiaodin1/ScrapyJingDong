# -*- coding:utf-8 -*-

from flask import Flask
from config import devconfig
from flask_restful import Api

api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(devconfig)
    devconfig.init_app(app)
    api.init_app(app)
    from .apis import api as api_blueprint
    app.register_blueprint(api_blueprint)
    return app






