import socketserver as SocketServer, threading, time

class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].decode("utf-8")
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
    HOST, PORT = "0.0.0.0", 8888

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