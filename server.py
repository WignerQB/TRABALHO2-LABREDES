#servidor-tcp.py
import socket
import pickle

HOST = '127.0.0.1' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor esta
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.bind((HOST, PORT))
SOCKET.listen(1)

REC = []

while True:
    CON, CLIENT = SOCKET.accept()
    print('Conectado com', CLIENT)
    while True:
        DADOS = CON.recv(1024)
        if DADOS == b'': 
            break
        REC.append(DADOS)
        MSG = pickle.loads(b''.join(REC))
        print(CLIENT, MSG)
    print('Finalizando conexao do cliente', CLIENT)
    CON.close()
