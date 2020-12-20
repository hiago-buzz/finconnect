from flask import request, jsonify
from flask_restful import Resource
from finconnect.ext.auth import create_user
from finconnect.util.response import format_response
from finconnect.models import User


class UserResource(Resource):
    def get(self):

        users = User.query.order_by(User.full_name).all()
        if len(users):
            data = [user.to_dict() for user in users]
            message = "Usuários listados com sucesso"
            return format_response(data=data, message=message)
        else:
            data = []
            message = "Nenhum Usuário Encontrado"
            status_code = 204
            return format_response(data=data, message=message, status_code=status_code)

    def post(self):

        user = create_user(request.json)

        if user:
            data = user.to_dict()
            return format_response(data=data, message="Usuários cadastrado com sucesso")
        else:
            return format_response(message="Email já esta cadastrado", status_code=400)


class UserIdResource(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            data = user.to_dict()
            return format_response(data=data, message="Usuário listado com sucesso")
        else:
            return format_response(message="Usuário não Existe", status_code=200)