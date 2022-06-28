import socket
import _thread
import json

ClientSocket = socket.socket()
host = '192.168.124.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Name = input("Digite o nome do usuário: ")

MyAddress = socket.gethostbyname(socket.gethostname())

f = open('conf.json','r')
data = json.load(f)
for i in data['MyAddress']:
    if MyAddress == data['MyAddress'][i]:
        MyName = i
f.close()


print("As mensagens devem conter o destinatário no início e a mensagem logo após, com um $ separando")
print("Exemplo: C1$Ola Mundo!")
print("\n\n\n\n")

Response = ClientSocket.recv(1024)
ClientSocket.send(str.encode(Name))

def exibirMSG(CSocket):
    while True:
        Response = CSocket.recv(1024)
        print(Response.decode('utf-8'))

def enviarMSG(CSocket):
    while True:
        MSG = input('')
        VETORMSG = MSG.split("$")
        try:
            ind = VETORMSG[0].index(MyName)
        except:
            ind = -1
        if ind ==  -1 and len(VETORMSG) > 1:
            CSocket.send(str.encode(MSG))
        else:
            print("Mensagem inválida!")



try:
    _thread.start_new_thread(exibirMSG, (ClientSocket,))
    _thread.start_new_thread(enviarMSG, (ClientSocket,))
except:
    exit()
    ClientSocket.close()

while True:
    pass
