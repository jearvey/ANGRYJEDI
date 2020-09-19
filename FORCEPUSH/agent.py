import socket
import sys
import json
import time
import uuid

time.sleep(0)
uuid = uuid.uuid4()
MsgNum = 0
def GenMsg(x):
    if (x == 0):\
        NewMsg = b'{{"id": 0, "name": "test", "Type": "init"}}i'
    else:
        NewMsg = b"tbd"
    return NewMsg



HOST, PORT = "localhost", 1776

Msg = GenMsg(MsgNum)

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(Msg)


    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print("Sent:     {}".format(Msg))
print("Received: {}".format(received))
