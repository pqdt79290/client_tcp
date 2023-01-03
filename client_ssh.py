import paramiko

host = "192.168.1.4"
user = "root"
passwd = "pqdt@79290"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:
    stdin, stdout, stderr = client.exec_command(input("Comando: "))
    for line in stdout.readlines():
        print(line.strip())


     erros = stderr.readlines()
     if erros:
         print(erros)
