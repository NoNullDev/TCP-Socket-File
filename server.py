import socket
import os
import json

HOST = 'coloca o ip do servidor' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor está

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print("ativado")

con, cliente = tcp.accept()
print ('Conectado por',cliente)

length = int(con.recv(2).decode())
fileDict = json.loads((con.recv(length)).decode('utf-8'))

print("size recebido = " + str(fileDict["size"]))
print("nome recebido = " + fileDict["nome"])
print("extensão recebida = " + fileDict["ext"])


file = open(fileDict["nome"] + '-server.' + fileDict["ext"], "wb")

file_quadro = con.recv(2048)
while file_quadro:
    file.write(file_quadro)
    file_quadro = con.recv(2048)


file.close()
con.close()
input('Pressione ENTER para sair')
