import json

def BuildTask(data):
    raw_reply = data.decode()
    reply = json.loads(raw_reply)
    #newid = reply[id] + 1
    #newdic = {"id":newid}
    print(reply)
    if (reply["Type"] == "init"):
        task = '{"id": 1, "task": "uname -a"}'
        replyMsg = str.encode(task)
    return replyMsg
