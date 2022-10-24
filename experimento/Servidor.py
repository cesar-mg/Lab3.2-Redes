import socket, time

HOST = "10.0.2.15"
PORT = 49152
bufferSize = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    f = int(input("Ingrese archivo que desea envíar. 1) Para 100mb 2) Para 250 mb."))
    clientes_actuales = 0
    tam = ""
    if f == 1:
        path = "test_100.txt"
        tam = "100 mb"
    else:
        path = "test_250.txt"
        tam = "250 mb"
    
    file = open(path,"r",encoding='utf-8')
    data = file.read(1024)
    init = time.time()

    s.bind((HOST, PORT))

    while(True):

        bytesAddressPair = s.recvfrom(bufferSize)

        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        
        print(clientMsg)
        print(clientIP)
        init = time.time()
    
        # Sending a reply to client
        with open(path,"rb",encoding='utf-8') as file:
            while (byte := file.read(bufferSize)):
                s.sendto(byte, address)
