from smart_uj import db


class Ubicacion(db.Model):
    id = db.column(db.Integer, primary_key=True)
    coordenada_x = db.column(db.Float)
    coordenada_y = db.column(db.Float)
    id_usuario = db.column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    ip_publica = db.column(db.String(50))
    hora = db.column(db.DateTime)

    def __init__(self, coordenada_x, coordenada_y, id_usuario, ip_publica, hora):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.id_usuario = id_usuario
        self.ip_publica = ip_publica
        self.hora = hora

    def __repr__(self):
        return '<Ubicacion %r>' % self.id

    def to_json(self):
        return {
            'id': self.id,
            'coordenada_x': self.coordenada_x,
            'coordenada_y': self.coordenada_y,
            'id_usuario': self.id_usuario,
            'ip_publica': self.ip_publica,
            'hora': self.hora.strftime("%H:%M:%S")
        }

def get_ubicacion():
    return None


def get_ubicacion_id(id):
    return None


def create_ubicacion(coordenada_x, coordenada_y, id_usuario, ip_publica, hora):
    return None

