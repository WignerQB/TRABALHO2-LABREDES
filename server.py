#DEVE SER INFORMADO O IP AONDE SERÁ ARMAZENADO O SERVIDOR
import socket
import os
from _thread import *
import json

data = dict()

MyAddress = socket.gethostbyname(socket.gethostname())

f = open('conf.json','r')
data = json.load(f)
HOST = data['Server']["HOST"]
PORT = data['Server']["PORT"]
print(data)

for i in data['AddressDest']:
    if MyAddress == data['AddressDest'][i]:
        MyName = i
f.close()

ServerSocket = socket.socket()

CONTADOR = 0
try:
    ServerSocket.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

print('Conectando...')
ServerSocket.listen(2)

CLIENTS_CONECTADOS = []
CONEXOES = dict()

def clients(SELFconnection, CONEXOES, REM):
    #SELFconnection.send(str.encode('Conectado!'))
    while True:
        data = SELFconnection.recv(2048)
        data = data.decode('utf-8')
        try:
            MSG = data.split("$")
            if MSG[0] == "C1":
                DEST = '192.168.124.1'
            elif MSG[0] == "G1":
                DEST = '192.168.124.2'
            elif MSG[0] == "G2":
                DEST = '192.168.124.18'
            elif MSG[0] == "C2":
                DEST = '192.168.124.34'
            DESTSOCKET = CONEXOES[DEST]
            print(DESTSOCKET)
            print(MSG[1])
            reply =  REM + ": " + MSG[1]
            if not data:
                break
            DESTSOCKET.sendall(str.encode(reply))
        except:
            pass
    DESTSOCKET.close()
    SELFconnection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Conectado em: ' + address[0] + ':' + str(address[1]))
    
    Client.send(str.encode('Conectado!'))
    while True:
        Name = Client.recv(2048)
        if not Name:
            break
    Name = Name.decode('utf-8')

    X = "X" + str(CONTADOR+1)
    #data.update({"AddressDest":{X:address[0]}})
    data["AddressDest"][Name] = address[0]
    print(data)
    json_object = json.dumps(data, indent = 4)
    with open("conf.json", "w") as outfile:
        outfile.write(json_object)

    HOST = data['Server']["HOST"]
    """if address[0] == '192.168.124.1':
        REM  = 'C1'
    elif address[0] == '192.168.124.2':
        REM = 'G1'
    elif address[0] == '192.168.124.18':
        REM = 'G2'
    elif address[0] == '192.168.124.34':
        REM = 'C2'"""

    REM = "X"
    start_new_thread(clients, (Client, CONEXOES, REM, ))
    try:
        ind = CLIENTS_CONECTADOS.index(address[0])
    except:
        ind = -1
    if ind == -1 or CLIENTS_CONECTADOS == []:
        CLIENTS_CONECTADOS.append(address[0])
        CONEXOES[address[0]] = Client
        CONTADOR += 1
    print('Número de clientes: ' + str(CONTADOR))
ServerSocket.close()

