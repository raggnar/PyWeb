import socket

from Server import Server

HOST = ''
PORT = 80
isRunning = True


def __init__():
    while isRunning:
        sock = socket.socket()
        sock.bind((HOST, PORT))
        sock.listen(0)
        conn, addr = sock.accept()
        server.add(conn, addr)


server = Server()
__init__()