from flask import jsonify
from flask_restful import Resource
from finconnect.util.date import date_now


class HealthCheckResource(Resource):
    def get(self):
        return jsonify(
            {
                "versão": "0.1.0",
                "mensagem": "Operação realizada com sucesso",
                "status": 200,
                "timestamp": str(date_now()),
            }
        )
