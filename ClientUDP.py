import datetime
import os
import socket
import sys
import threading
import time

lock = threading.lock()

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
    HOST, PORT = "10.0.2.15", 8888
    data = str(client_id)
    file_name = "ArchivosRecibidos/Cliente" + str(client_id) + "-Prueba-"+str(clientes)+".txt"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto((data + "\n").encode("utf-8"), (HOST, PORT))
    print("Cliente " + str(client_id) + " conectado y recibiendo datos...")
    init = time.time()

    recieve_file(file_name,sock)

    lock.acquire()
    fin = time.time()
    tiempo = fin - init 

    file_stats = os.stat(file_name)
    
    date = datetime.datetime.now()
    name = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "-" + str(date.hour) + "-" + str(date.minute) + "-" + str(date.second)
    msg = "Nombre del archivo: " + file_name + " Tamanio del archivo: " + file_stats.st_size
    msg += " Cliente: " + str(client_id)
    msg += "\nEl tiempo calculado fue de: " + str(tiempo) +"\n"

    log = open("Logs/"+name+"-log.txt","w")
    log.write(msg)
    log.close()
    lock.release()

    print("Cliente " + str(client_id) + " recibió los datos.")
clientes = 1
for i in range(clientes):
    t = threading.Thread(target=handle_client, args=((i+1,)))
    t.start()