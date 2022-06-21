#DEVE SER INFORMADO O IP AONDE SERÁ ARMAZENADO O SERVIDOR
import socket
import os
from _thread import *
import json

MyAddress = socket.gethostbyname(socket.gethostname())

f = open('conf.json','r')
data = json.load(f)
for i in data['MyAddress']:
    if MyAddress == data['MyAddress'][i]:
        MyName = i
f.close()

ServerSocket = socket.socket()
HOST = '192.168.124.1'
PORT = 1233
CONTADOR = 0
try:
    ServerSocket.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

print("Eu sou", MyName)

print('Conectando...')
ServerSocket.listen(2)

CLIENTS_CONECTADOS = []
CONEXOES = dict()

def clients(SELFconnection, CONEXOES, REM):
    SELFconnection.send(str.encode('Conectado!'))
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

    if address[0] == '192.168.124.1':
        REM  = 'C1'
    elif address[0] == '192.168.124.2':
        REM = 'G1'
    elif address[0] == '192.168.124.18':
        REM = 'G2'
    elif address[0] == '192.168.124.34':
        REM = 'C2'

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

