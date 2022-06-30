import socket
import _thread
import json
import sys
import os

f = open('conf.json','r')
data = json.load(f)
HOST = data['Server']["HOST"]
PORT = data['Server']["PORT"]

ClientSocket = socket.socket()
Name = input("Digite o nome do usuário: ")
try:
    ClientSocket.connect((HOST, PORT))
except socket.error as e:
    print(str(e))

ClientSocket.send(str.encode(Name))

MyAddress = socket.gethostbyname(socket.gethostname())


print("\nAs mensagens devem conter o destinatário no início e a mensagem logo após, com um : separando")
print("\nExemplo: C1:Ola Mundo!")
print("\nPara sair digite: SAIR\n\n")

Response = ClientSocket.recv(2048)
print(Response.decode('utf-8'))

def exibirMSG(CSocket):
    while True:
        Response = CSocket.recv(2048)
        print(Response.decode('utf-8'))

def enviarMSG(CSocket):
    while True:
        MSG = input('')
        CSocket.send(str.encode(MSG))


try:
    _thread.start_new_thread(exibirMSG, (ClientSocket,))
    _thread.start_new_thread(enviarMSG, (ClientSocket,))
except KeyboardInterrupt:
    ClientSocket.send(str.encode("Desconectar"))
    time.sleep(1)
    ClientSocket.close()
    _thread.interrupt_main()
    sys.exit()

while True:
    pass
