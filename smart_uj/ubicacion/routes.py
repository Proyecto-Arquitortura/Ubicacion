from flask import Blueprint, make_response, jsonify, request, abort

from . import models

ubicacion_bp = Blueprint('ubicacion', __name__)
