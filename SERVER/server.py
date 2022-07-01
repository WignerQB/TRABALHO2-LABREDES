import socket
import os
from _thread import *
import json
import sys

data = dict()
RESETdata = dict()
CONEXOES = dict()
CLIENTS_CONECTADOS = []
ListaContatos = []
ADDRESS = []

MyAddress = socket.gethostbyname(socket.gethostname())

f = open('conf.json','r')
data = json.load(f)
HOST = sys.argv[1]
PORT = data['Server']["PORT"]

data["AddressDest"] = {}
json_object = json.dumps(data, indent = 4)
with open("conf.json", "w") as outfile:
    outfile.write(json_object)


f.close()

ServerSocket = socket.socket()

CONTADOR = 0
try:
    ServerSocket.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

print('\nConectando...\n')
ServerSocket.listen(2)


def InformarConectados(ListaContatos, CONEXOES, CLIENTS_CONECTADOS):
    TEXTO = "\nUsuários Online:\n"
    for j in ListaContatos:
        TEXTO = TEXTO + str(j) + "\n"
    TEXTO = TEXTO + "\n"
    for ips in CLIENTS_CONECTADOS:
        CONEXOES[ips].send(str.encode(TEXTO))


def clients(Client, IPREM, CONEXOES, CLIENTS_CONECTADOS):
    global data
    REM = " "

    Client.send(str.encode('\nConectado!\n'))
    Name = Client.recv(2048)

    Name = Name.decode('utf-8')

    data["AddressDest"][Name] = address[0]
    json_object = json.dumps(data, indent = 4)
    with open("conf.json", "w") as outfile:
        outfile.write(json_object)

    ListaContatos = []
    for i in data["AddressDest"]:
        ListaContatos.append(i)

    InformarConectados(ListaContatos, CONEXOES, CLIENTS_CONECTADOS)
    #Client.send(str.encode('Canal aberto!\n'))
    while True:
        Mensagem = Client.recv(2048)
        Mensagem = Mensagem.decode('utf-8')
        with open("conf.json", encoding= 'utf-8') as ConfigFile:
            data = json.load(ConfigFile)

        for i in data['AddressDest']:
            if IPREM == data['AddressDest'][i]:
                REM = i

        if Mensagem == "SAIR":
            del data["AddressDest"][REM]
            json_object = json.dumps(data, indent = 4)
            with open("conf.json", "w") as outfile:
                outfile.write(json_object)

            del CONEXOES[IPREM]
            CLIENTS_CONECTADOS.remove(IPREM)
            ListaContatos = []
            for i in data["AddressDest"]:
                ListaContatos.append(i)
            InformarConectados(ListaContatos, CONEXOES, CLIENTS_CONECTADOS)
            print(IPREM + ' desconectou!')
            print('Número de clientes: ' + str(len(CLIENTS_CONECTADOS)) + '\n')


        try:
            MSG = Mensagem.split(":")
            DEST = data["AddressDest"][MSG[0]]

            DESTSOCKET = CONEXOES[DEST]
            reply = "(" + REM + ") >>> " + MSG[1]
            if Mensagem == '':
                #print("Entrei")
                Client.close()
                break
            DESTSOCKET.sendall(str.encode(reply))
        except:
            pass
    DESTSOCKET.close()
    Client.close()

while True:

    Client, address = ServerSocket.accept()
    print('Conectado em: ' + address[0])

    HOST = sys.argv[1]

    try:
        ind = CLIENTS_CONECTADOS.index(address[0])
    except:
        ind = -1
    if ind == -1 or CLIENTS_CONECTADOS == []:
        CLIENTS_CONECTADOS.append(address[0])
        CONEXOES[address[0]] = Client
        ADDRESS.append(address)
    print('Número de clientes: ' + str(len(CLIENTS_CONECTADOS)) + '\n')
    start_new_thread(clients, (Client, address[0], CONEXOES, CLIENTS_CONECTADOS, ))

