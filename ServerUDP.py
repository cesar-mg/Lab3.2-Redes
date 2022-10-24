import datetime
import os
import socketserver as SocketServer, threading, time

path = ''
lock = threading.Lock()

class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].decode("utf-8")
        client_id = data
        socket = self.request[1]
        current_thread = threading.current_thread()
        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, data))
        file = open(path,"r",encoding='utf-8')
        data = file.read(1024)
        init = time.time()
        while data:
            socket.sendto(data.encode("utf-8"), self.client_address)
            data = file.read(1024)
        fin = time.time()
        file.close()
        tiempo = fin - init
        print(tiempo)
        
        lock.acquire()
        date = datetime.datetime.now()
        name = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "-" + str(date.hour) + "-" + str(date.minute) + "-" + str(date.second)
        file_stats = os.stat(path)
        msg = "Nombre del archivo: " + path + " Tamanio del archivo: " + str(file_stats.st_size)
        msg += " Cliente: " + str(client_id)
        msg += "\nEl tiempo calculado fue de: " + str(tiempo) +"\n"

        log = open("Logs/"+name+"-log.txt","a")
        log.write(msg)
        log.close()
        lock.release()

        ok =["R","1"] #socket.recieve(1024).decode("utf-8")
        msg = "Nombre del archivo: " + path + " Tamanio del archivo: " + tam
        msg += " Cliente: " + ok[1]
        if ok[0] == "E":
            msg += " Entrega Exitosa"
        else:
            msg += " Entrega Fallida"
        msg += "El tiempo calculado fue de: " + str(tiempo) +"\n"
        print('Archivo enviado en:', str(tiempo))
    
class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "10.0.2.15", 8888

    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)
    f = int(input("Ingrese archivo que desea envíar. 1) Para 100mb 2) Para 250 mb."))
    clientes_actuales = 0
    tam = 0
    if f == 1:
        path = "test_100.txt"
        tam = "100 mb"
    else:
        path = "test_250.txt"
        tam = "250 mb"

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        server_thread.start()
        print("Server started at {} port {}".format(HOST, PORT))
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        exit()