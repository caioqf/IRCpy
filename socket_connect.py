import socket

PORT = 6969
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

