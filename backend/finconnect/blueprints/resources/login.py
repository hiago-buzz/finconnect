from flask import abort, jsonify, request
from flask_restful import Resource

from finconnect.ext.auth import verify_login


class LoginResource(Resource):
    def post(self):
      return verify_login(request.json)
