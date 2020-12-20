from flask import Blueprint
from flask_restful import Api

from .user import UserResource, UserIdResource
from .health_check import HealthCheckResource
from .login import LoginResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(HealthCheckResource, "/health/")
    api.add_resource(UserResource, "/user/")
    api.add_resource(UserIdResource, "/user/<id>")
    api.add_resource(LoginResource, "/login/")
    app.register_blueprint(bp)