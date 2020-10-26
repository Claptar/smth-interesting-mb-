import socket


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        sock = socket.create_connection((host, port), timeout=timeout)

    def get(self):
        pass

    def put(self):
        pass
