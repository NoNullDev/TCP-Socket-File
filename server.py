import socket
import os
import json

HOST = 'coloca o ip do servidor' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print("ativado")

con, cliente = tcp.accept()
print ('Conectado por',cliente)

length = int(con.recv(2).decode())
imageDict = json.loads((con.recv(length)).decode('utf-8'))

print("size recebido = " + str(imageDict["size"]))
print("nome recebido = " + imageDict["nome"])
print("extensão recebida = " + imageDict["ext"])


imagem = open("imagem-server." + imageDict["ext"], "wb")

imagem_quadro = con.recv(2048)
while imagem_quadro:
    imagem.write(imagem_quadro)
    imagem_quadro = con.recv(2048)


imagem.close()
con.close()
input('Press ENTER to exit')
