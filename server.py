#DEVE SER INFORMADO O IP AONDE SERÁ ARMAZENADO O SERVIDOR
import socket
import os
from _thread import *
import json
import sys
import time

data = dict()
RESETdata = dict()
CONEXOES = dict()
CLIENTS_CONECTADOS = []
ListaContatos = []
IPS = []

MyAddress = socket.gethostbyname(socket.gethostname())

f = open('conf.json','r')
data = json.load(f)
HOST = data['Server']["HOST"]
PORT = data['Server']["PORT"]

f.close()

ServerSocket = socket.socket()

CONTADOR = 0
try:
    ServerSocket.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

print('Conectando...')
ServerSocket.listen(2)


def InformarConectados(ListaContatos, CONEXOES, IPS):
    TEXTO = "\nUsuários Online:\n"
    for j in ListaContatos:
        TEXTO = TEXTO + str(j) + "\n"
    TEXTO = TEXTO + "\n"
    for ips in IPS:
        CONEXOES[ips].send(str.encode(TEXTO))


def clients(Client, IPREM, CONEXOES, IPS, data):

    REM = " "

    Client.send(str.encode('Conectado!'))
    Name = Client.recv(2048)

    Name = Name.decode('utf-8')

    data["AddressDest"][Name] = address[0]
    json_object = json.dumps(data, indent = 4)
    with open("conf.json", "w") as outfile:
        outfile.write(json_object)

    ListaContatos = []
    for i in data["AddressDest"]:
        ListaContatos.append(i)

    InformarConectados(ListaContatos, CONEXOES, IPS)
    Client.send(str.encode('Canal aberto!'))
    while True:
        Mensagem = Client.recv(2048)
        Mensagem = Mensagem.decode('utf-8')
        with open("conf.json", encoding= 'utf-8') as ConfigFile:
            data = json.load(ConfigFile)
        print(Mensagem)
        time.sleep(1)
        if Mensagem == "Desconectar":
            del data["AddressDest"][REM]
            print(data["AddressDest"])
            json_object = json.dumps(data, indent = 4)
            with open("conf.json", "w") as outfile:
                outfile.write(json_object)


        for i in data['AddressDest']:
            if IPREM == data['AddressDest'][i]:
                REM = i

        try:
            MSG = Mensagem.split(":")
            DEST = data["AddressDest"][MSG[0]]

            DESTSOCKET = CONEXOES[DEST]
            reply = "(" + REM + ") >>> " + MSG[1]
            if Mensagem == '':
                print("Entrei")
                Client.close()
                break
            DESTSOCKET.sendall(str.encode(reply))
        except:
            pass
    DESTSOCKET.close()
    Client.close()

while True:

    Client, address = ServerSocket.accept()
    print('Conectado em: ' + address[0] + ':' + str(address[1]))

    HOST = data['Server']["HOST"]

    try:
        ind = CLIENTS_CONECTADOS.index(address[0])
    except:
        ind = -1
    if ind == -1 or CLIENTS_CONECTADOS == []:
        CLIENTS_CONECTADOS.append(address[0])
        CONEXOES[address[0]] = Client
        IPS.append(address[0])
        CONTADOR += 1
    print('Número de clientes: ' + str(CONTADOR))
    start_new_thread(clients, (Client, address[0], CONEXOES, IPS, data, ))

#ServerSocket.close()

