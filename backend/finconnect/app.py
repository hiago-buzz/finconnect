from flask import Flask

from finconnect.ext import configuration

def minimal_app(**config):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app