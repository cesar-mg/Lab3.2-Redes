import socket
import sys
import threading
def recieve_file(file_name,sock):
    file = open(file_name, "w")
    # Leemos de a 1024 bytes
    archivo = sock.recv(1024).decode("utf-8")
    try:
        while archivo:
            file.write(archivo)
            archivo = sock.recv(1024).decode("utf-8")
    except TimeoutError:
        nada = 1
    file.close()
    return

def handle_client(client_id):
    HOST, PORT = "localhost", 8888
    data = "R"
    file_name = "ArchivosRecibidos/Cliente" + str(client_id) + "-Prueba-"+str(clientes)+".txt"
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto((data + "\n").encode("utf-8"), (HOST, PORT))
    recieve_file(file_name,sock)

    print("Sent:     {}".format(data))
    #print("Received: {}".format(received))
clientes = 1
for i in range(clientes):
    t = threading.Thread(target=handle_client, args=((i+1,)))
    t.start()