
import socket
import os
from _thread import *

ServerSocket = socket.socket()
HOST = '127.0.0.1'
PORT = 1233
CONTADOR = 0
try:
    ServerSocket.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

print('Conectando...')
ServerSocket.listen(5)


def clients(connection):
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Conectado em: ' + address[0] + ':' + str(address[1]))
    start_new_thread(clients, (Client, ))
    CONTADOR += 1
    #print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()