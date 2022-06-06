import socket

ClientSocket = socket.socket()
host = '192.168.124.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

print("As mensagens devem conter o destinatário no início e a mensagem logo após, com um $ separando")
print("Exemplo: C1$Ola Mundo!")

Response = ClientSocket.recv(1024)
while True:
    
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

    MSG = input('Eu: ')
    VETORMSG = MSG.split("$")
    try:
        ind = VETORMSG[0].index("G10")
    except:
        ind = -1
    if ind ==  -1 and len(VETORMSG) > 1:
        ClientSocket.send(str.encode(MSG))
    else:
        print("Mensagem inválida!")

ClientSocket.close()
