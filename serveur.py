import socket

host, port = ('', 8001)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Serveur allumé")

while True:
    socket.listen()
    conn, address = socket.accept()
    print("Client connecté")

    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)


conn.close()
socket.close()
