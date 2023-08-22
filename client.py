import socket

host, port = ('localhost', 8001)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    socket.connect((host, port))
    print("Je viens de me connecter")

    data = input("Msg : ")
    data = data.encode("utf8")
    socket.sendall(data)


except ConnectionRefusedError:
    print("Le serveur n'a pas été trouvé")
finally:
    socket.close()