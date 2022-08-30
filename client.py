import socket
HOST = 'coloca o ip do servidor' # Endereco IP do Servidor
PORT = 5005 # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')

imagem = open("imagem-cliente.png","rb")
imagem_quadro = imagem.read(2048)
while imagem_quadro:
	tcp.send(imagem_quadro)
	imagem_quadro = imagem.read(2048)

while msg != '\x18':
     tcp.sendto(text, dest)
     msg = input()
tcp.close()



