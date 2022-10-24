
import socket

HOST = "10.0.2.15"
PORT = 49152
bufferSize = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))

    bytesToSend = str.encode("REQUEST_FILE")
    s.sendto(bytesToSend, (HOST, PORT))

    msgFromServer = s.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])
