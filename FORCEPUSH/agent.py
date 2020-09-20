import socket
import sys
import json
import time
import uuid
import subprocess

time.sleep(0)
uuid = uuid.uuid4()
MsgNum = 0

def GenMsg(x):
    if (x == 0):
        NewMsgJ = '{"id": 0, "name": "test", "Type": "init"}'
        NewMsg = str.encode(NewMsgJ)
    else:
        reformat = x.split(" ")
        print(reformat)
        output = subprocess.Popen(reformat,stdout=subprocess.PIPE).communicate()[0]
        print(output)
        NewMsg = output.decode("utf-8")
    return NewMsg


Msg = GenMsg(MsgNum)


while True:
    HOST, PORT = "localhost", 1776
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
        sock.sendall(Msg)
        print("Sending:     {}".format(Msg))

        received = sock.recv(1024)
        print("Recevied:    {}".format(received))
        raw_received = received.decode()
        receive = json.loads(raw_received)
        if (receive["task"] != "quit"):
            MsgDraft = GenMsg(receive["task"])
            Msg = str.encode(MsgDraft)
        else:
            exit()

    finally:
        sock.close()
    continue

print("Closing...")
