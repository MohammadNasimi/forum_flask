from flask import jsonify


def resource_not_found(e):
    return jsonify(error=str(e)), 404


def resource_sever_error(e):
    return jsonify(error=str(e)), 500
