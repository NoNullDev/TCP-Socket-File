import socket
HOST = 'coloca o ip do servidor'              # Endereco IP do Servidor
PORT = 5005            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print("ativado")
while True:
    con, cliente = tcp.accept()
    print ('Conectado por',cliente)
    while True:
        imagem  =  open("imagem-server.png", "wb")
        
        imagem_quadro = con.recv(2048)

        while imagem_quadro:
            imagem.write(imagem_quadro)
            imagem_quadro = con.recv(2048)
        imagem.close()

        if not msg:
            print("FIM - Conexao Perdida")
            break
        elif msg == "fim":
            print("FIM - Cliente pediu para encerrar o programa")
            break
    print ('Finalizando conexao do cliente'), cliente
    con.close()
    