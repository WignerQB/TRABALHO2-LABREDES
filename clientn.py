import socket
import _thread
import json

f = open('conf.json','r')
data = json.load(f)
HOST = data['Server']["HOST"]
PORT = data['Server']["PORT"]

ClientSocket = socket.socket()

print('Waiting for connection')
try:
    ClientSocket.connect((HOST, PORT))
except socket.error as e:
    print(str(e))

Name = input("Digite o nome do usuário: ")
ClientSocket.send(str.encode(Name))

MyAddress = socket.gethostbyname(socket.gethostname())


print("As mensagens devem conter o destinatário no início e a mensagem logo após, com um $ separando")
print("Exemplo: C1:Ola Mundo!")
print("\n\n\n\n")

Response = ClientSocket.recv(2048)
print(Response.decode('utf-8'))

def exibirMSG(CSocket):
    while True:
        try:
            Response = CSocket.recv(2048)
            print(Response.decode('utf-8'))
        except KeyboardInterrupt:
            CSocket.close()
            a = input("Encerrando conexão. Pressione qualquer tecla.")
            exit()

def enviarMSG(CSocket):
    while True:
        try:
            MSG = input('')
            if MSG == '\x03':
                CSocket.close()
                a = input("Encerrando conexão. Pressione qualquer tecla.")
                exit()
            VETORMSG = MSG.split(":")
            try:
                ind = VETORMSG[0].index(Name)
            except:
                ind = -1
            if ind ==  -1 and len(VETORMSG) > 1:
                CSocket.send(str.encode(MSG))
            else:
                print("Mensagem inválida!")
        except KeyboardInterrupt:
            CSocket.close()
            a = input("Encerrando conexão. Pressione qualquer tecla.")
            exit()




try:
    _thread.start_new_thread(exibirMSG, (ClientSocket,))
    _thread.start_new_thread(enviarMSG, (ClientSocket,))
except:
    ClientSocket.close()

while True:
    try:
        pass
    except KeyboardInterrupt:
        ClientSocket.close()
        a = input("Encerrando conexão. Pressione qualquer tecla.")
        exit()
