import socket
import os
import json

HOST = 'coloca o ip do servidor' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = (HOST, PORT)

file_fullname = input("Digite o nome do arquivo: ")

tcp.connect(dest)

file_ext = file_fullname.split('.')[-1] # extensão
file_name = file_fullname.split('.')[0] # nome sem extensão
file_size = os.stat(file_fullname).st_size

fileDict = {
	"nome" : file_name,
	"size" : file_size,
	"ext" : file_ext
}

#enviar dados da imagem pro servidor
tcp.send(str(len(json.dumps(fileDict))).encode())
tcp.send(json.dumps(fileDict).encode('utf-8'))

print("size enviado = " + str(file_size))
print("nome enviado = " + file_name)
print("extensão enviada = " + file_ext)


file = open(file_fullname,"rb")
file_quadro = file.read(2048)
while file_quadro:
     tcp.send(file_quadro)
     file_quadro = file.read(2048)


file.close()
tcp.close()
input('Pressione ENTER para sair')
