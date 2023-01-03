import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(("0.0.0.0", 4466))
    server.listen(5)
    print("Aguardando mensagem...")

    client_socket, addres = server.accept()
    print("Received from: " + address[0])

    while True:
        data = client_socker.recv(1024).encode()
        print(data)
        client_socket.send(input("Mensagem: ").encode())

        server.close()

   except Exception as error:
       print("Erro: ", error)
       server.close()



