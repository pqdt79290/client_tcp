import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        msg = input("Mensagem: ") + "\n"
        client.sendto(msg.encode(), ("192.168.1.4", 4466))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())
        if data.decode() == "sair\n" or msg == "sair\n":
            break
        client.close()
except Exception as error:
    print("Um erro ocorreu")
    print(error)
    client.close()
