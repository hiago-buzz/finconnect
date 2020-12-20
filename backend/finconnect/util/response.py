from flask import jsonify


def format_response(data=[], message="Successo", status_code=200):
    return jsonify({"data": data, "message": message, "status_code": status_code})