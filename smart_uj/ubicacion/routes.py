from flask import Blueprint, make_response, jsonify, request, abort
import _thread
from . import models
from .sensores import ubicacion as ubicacion_sensores


ubicacion_bp = Blueprint('ubicacion', __name__)


@ubicacion_bp.route('/', methods=['GET', 'OPTIONS'])
@ubicacion_bp.route('/ping', methods=['GET', 'OPTIONS'])
@ubicacion_bp.route('/heathcheck', methods=['GET', 'OPTIONS'])
def heathcheck():
    return make_response(jsonify({"Mensaje": "Ok"}), 200)


# Retorna todas las ubicaciones
@ubicacion_bp.route('/ubicacion', methods=['GET', 'OPTIONS'])
def get_ubicacion():
    if request.method == 'GET':
        ubicacion = models.get_ubicacion()
        return make_response(jsonify(ubicacion), 200)
    if request.method == 'OPTIONS':
        return make_response(jsonify({"Mensaje": "OK"}), 200)


# Retorna la ubicacion de un usuario
@ubicacion_bp.route('/ubicacion/<string:id>', methods=['GET', 'OPTIONS'])
def get_ubicacion_id(id):
    if request.method == 'GET':
        ubicacion = models.get_ubicacion_id(id)
        return make_response(jsonify(ubicacion), 200)
    if request.method == 'OPTIONS':
        return make_response(jsonify({"Mensaje": "OK"}), 200)


# Crea una ubicacion
@ubicacion_bp.route('/ubicacion/<string:id>', methods=['POST', 'OPTIONS'])
def create_ubicacion(id):
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            coordenada_x = request_data['coordenada_x']
            coordenada_y = request_data['coordenada_y']
            ip_publica = request_data['ip_publica']
            hora = request_data['hora']
            ubicacion = models.create_ubicacion(coordenada_x, coordenada_y, id, ip_publica, hora)
            return make_response(jsonify(ubicacion), 200)
        except Exception as e:
            print(e)
            return make_response(jsonify({"Mensaje": e}), 500)
    if request.method == 'OPTIONS':
        return make_response(jsonify({"Mensaje": "OK"}), 200)


# Recibe las ubicaciones de los sensores
@ubicacion_bp.route('/recibir_ubicaciones', methods=['GET', 'OPTIONS'])
def recibir_ubicaciones():
    def recibir_ubicaciones_thread():
        ubicacion_data = ubicacion_sensores()
        ubicacion_data.socket_config()
        ubicacion_data.open()
    if request.method == 'GET':
        _thread.start_new_thread(recibir_ubicaciones_thread, ())
        return make_response(jsonify({"Mensaje": "Recibiendo ubicaciones..."}), 200)
    if request.method == 'OPTIONS':
        return make_response(jsonify({"Mensaje": "OK"}), 200)