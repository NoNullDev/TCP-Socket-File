import socket
import os
import json

HOST = 'coloca o ip do servidor' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor está

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = (HOST, PORT)

tcp.connect(dest)

image_fullname = 'imagem-cliente.png' 
image_ext = image_fullname.split('.')[1] # extensão
image_name = image_fullname.split('.')[0] # nome sem extensão
image_size = os.stat(image_fullname).st_size

imageDict = {
	"nome" : image_name,
	"size" : image_size,
	"ext" : image_ext
}

#enviar dados da imagem pro servidor
tcp.send(str(len(json.dumps(imageDict))).encode())
tcp.send(json.dumps(imageDict).encode('utf-8'))

print("size enviado = " + str(image_size))
print("nome enviado = " + image_name)
print("extensão enviada = " + image_ext)


imagem = open(image_fullname,"rb")
imagem_quadro = imagem.read(2048)
while imagem_quadro:
     tcp.send(imagem_quadro)
     imagem_quadro = imagem.read(2048)


imagem.close()
tcp.close()
input('Press ENTER to exit')
