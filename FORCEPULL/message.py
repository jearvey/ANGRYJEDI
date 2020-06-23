import json

def BuildTask(data):
    reply = json.load(data)
    newid = json.reply['id'] + 1
    newdic = {"id": newid}
    if (json.reply['Type'] == 'init'):
        task = b'{"id": 1, "task": "uname -a"}'
    #elif - to do
    return task
