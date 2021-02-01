import socket
import threading

HEADER = 64
PORT = 5001
SERVER = '192.168.0.101'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DC"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[SERVER] New connection from {addr}.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif msg == '!CONNECTED':
                print(f"[ACTIVE CONNECTIONS]  {threading.activeCount() - 1}")

            print(f"{addr} {msg}")
            conn.send("OPA MIKAEL".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[SERVER] Listening {SERVER} on port {PORT}...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start()


