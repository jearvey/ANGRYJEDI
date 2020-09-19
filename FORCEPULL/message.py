import json

def BuildTask(data):
    raw_reply = data.decode()
    reply = json.loads(raw_reply)
    #reply = reply1.replace("'","")
    #newid = reply[id] + 1
    #newdic = {"id":newid}
    print(reply)
    if (reply["Type"] == "init"):
        task = b'{"id": 1, "task": "uname -a"}'
    return task
