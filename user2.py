import socket
import pickle
import time
import numpy as np


Contatos = dict()
#Contatos['192.168.124.1'] = 9000 #C1
Contatos['C1'] = ('192.168.124.1', 9000) #C1
Contatos['G2'] = ('192.168.124.18', 9001) #G2
Contatos['C2'] = ('192.168.124.34', 9001) #C2


while True:
    print(" ")
    DEST = input("Digite o destinatario da mensagem:")
    try:
        CONEXAO = Contatos[DEST]
        print(" ")
        print("HOST: ", CONEXAO[0], "PORT: ",  CONEXAO[1])
    except:
        print("Destinatario nao consta na lista de contatos!")

