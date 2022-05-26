import zmq
from . import models


class ubicacion:
    def __init__(self):
        self.socket = None

    # Socket configuration
    def socket_config(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect('tcp://127.0.0.1:6501')  # TODO change to the correct ip and port
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")

    # Open the socket
    def open(self):
        self.socket_config()
        print("Waiting for data...")
        while True:
            # Receive data
            # string = self.socket.recv()  # TODO Uncomment this line
            string = "4.631898 -74.064832 1 186.82.160.17 14:32:30"
            coordenada_x, coordenada_y, id_usuario, ip_publica, hora = string.split()  # Split the
            """
            coordenada_x = coordenada_x.decode("utf-8")
            coordenada_y = coordenada_y.decode("utf-8")
            id_usuario = id_usuario.decode("utf-8")
            ip_publica = ip_publica.decode("utf-8")
            hora = hora.decode("utf-8")
            """
            models.create_ubicacion(coordenada_x, coordenada_y, id_usuario, ip_publica, hora)


if __name__ == "__main__":
    ubicacion_data = ubicacion()
    # Login
    try:
        ubicacion_data.open()
    except KeyboardInterrupt:
        print("\n\nClosing the socket...")
        ubicacion_data.socket.close()
        print("Socket closed")