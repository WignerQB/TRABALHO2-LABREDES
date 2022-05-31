#ESTE PROGRAMA RODA NA MÁQUINA G1

import socket
import pickle
import time
import numpy as np


Contatos = dict()
#Contatos['192.168.124.1'] = 9000 #C1
"""Contatos['C1'] = ('192.168.124.1', 9000) #C1
Contatos['G2'] = ('192.168.124.18', 9001) #G2
Contatos['C2'] = ('192.168.124.34', 9001) #C2"""
Contatos['C1'] = ('127.0.0.1', 5000) #C1
Contatos['G2'] = ('127.0.0.1', 5000) #G2
Contatos['C2'] = ('127.0.0.1', 5000) #C2


while True:
    print(" ")
    DEST = input("Digite o destinatario da mensagem:")
    try:
        CONEXAO = Contatos[DEST]
        print(" ")
        print("HOST: ", CONEXAO[0], "PORT: ",  CONEXAO[1])
    except:
        print("Destinatario nao consta na lista de contatos!")
    else:
        print("Conectado com: ", CONEXAO)
        break

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.connect(CONEXAO)
print("Para sair use CTRL+X\n")
MSG = input()
while MSG != '\x18':
    PACOTE = pickle.dumps(MSG)
    SOCKET.sendall(bytes(PACOTE))
    MSG = input()
SOCKET.close()
