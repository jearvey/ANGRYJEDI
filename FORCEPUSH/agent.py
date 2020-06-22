import socket
import sys
import json

HOST, PORT = "localhost", 1776

m = b'{"id": 1, "name": "FORCEPUSH"}'

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(m)


    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print("Sent:     {}".format(m))
print("Received: {}".format(received))
