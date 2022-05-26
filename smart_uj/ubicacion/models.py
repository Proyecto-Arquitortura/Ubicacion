from smart_uj import db


class Ubicacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coordenada_x = db.Column(db.Float)
    coordenada_y = db.Column(db.Float)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    ip_publica = db.Column(db.String(50))
    hora = db.Column(db.DateTime)

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
    ubicaciones = Ubicacion.query.all()
    return ubicaciones


def get_ubicacion_id(id):
    ubicacion = Ubicacion.query.filter_by(id_suario=id).first()
    return ubicacion


def create_ubicacion(coordenada_x, coordenada_y, id_usuario, ip_publica, hora):
    ubicacion = Ubicacion(coordenada_x, coordenada_y, id_usuario, ip_publica, hora)
    db.session.add(ubicacion)
    db.session.commit()
    return ubicacion
