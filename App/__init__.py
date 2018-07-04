from .settings import config
from .extensions import extensions_init
from flask import Flask
from .views import blueprint_register


def create_app(configName):

    app = Flask(__name__)
    app.config.from_object(config[configName])
    extensions_init(app)
    blueprint_register(app)
    return app

