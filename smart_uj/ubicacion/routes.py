from flask import Blueprint, make_response, jsonify, request, abort

from . import models


ubicacion_bp = Blueprint('ubicacion', __name__)


@ubicacion_bp.route('/ubicacion', methods=['GET', 'OPTIONS'])
def get_ubicacion():
    if request.method == 'GET':
        ubicacion = models.get_ubicacion()
        return make_response(jsonify(ubicacion), 200)
    if request.method == 'OPTIONS':
        return make_response(jsonify({"Mensaje": "OK"}), 200)


@ubicacion_bp.route('/ubicacion/<string:id>', methods=['GET', 'OPTIONS'])
def get_ubicacion_id(id):
    if request.method == 'GET':
        ubicacion = models.get_ubicacion_id(id)
        return make_response(jsonify(ubicacion), 200)
    if request.method == 'OPTIONS':
        return make_response(jsonify({"Mensaje": "OK"}), 200)


@ubicacion_bp.route('/ubicacion/<string:id>', methods=['POST', 'OPTIONS'])
def create_ubicacion(id):
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            coordenada_x = request_data['coordenada_x']
            coordenada_y = request_data['coordenada_y']
            ip_publica = request_data['ip_publica']
            hora = request_data['hora']
            ubicacion = models.create_ubicacion(coordenada_x, coordenada_y, ip_publica, hora)
            return make_response(jsonify(ubicacion), 200)
        except Exception as e:
            print(e)
            return make_response(jsonify({"Mensaje": e}), 500)
    if request.method == 'OPTIONS':
        return make_response(jsonify({"Mensaje": "OK"}), 200)