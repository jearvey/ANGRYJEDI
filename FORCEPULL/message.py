import json

def BuildTask(data):
    raw_reply = data.decode()
    reply = json.loads(raw_reply)
    print(reply)
    if (reply["Type"] == "init"):
        task = '{"id": 1, "task": "uname -a"}'
        replyMsg = str.encode(task)
    else:
        uuid = reply["id"] + 1
        task = input("Task to complete: ")
        json_to_load = {"id": uuid, "Type":"cmd", "task": task}
        json_final = json.dumps(json_to_load)
        replyMsg = str.encode(json_final)
        
    return replyMsg
