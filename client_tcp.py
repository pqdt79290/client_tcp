import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    client.connect(("192.168.1.4", 4466))
    client.send(b"Oi tudo bem?\n")
    pacote_recebidos = client.recv(1024).decode()
    print(pacote_recebidos)
except Exception as error:
    print("Um erro ocorreu")
    print(error)
    
