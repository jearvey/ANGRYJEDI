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
        Type, cmd, value = TaskType()
        if (cmd == 0):
            json_to_load = {"id": uuid, "Type": Type, "task": "admin_tasker"}
        elif (cmd == 1):
            json_to_load = {"id": uuid, "Type": Type, "task": "admin_tasker", "value": value}
        else:
            json_to_load = {"id": uuid, "Type": Type, "task": cmd}
        json_final = json.dumps(json_to_load)
        replyMsg = str.encode(json_final)

    return replyMsg


def TaskType():
    print("What do you want to do?\n")
    for i in range(0, 2):
        print("1. Task\n")
        print("2. Change Callback Time\n")
        print("3. View Current Callback Time\n")

        choice = int(input("Enter a number: "))

        if (choice == 1):
            Type = "task"
            cmd = input("Enter command to task: \n")
            value = 0
            return Type, cmd, value

        if (choice == 2):
            Type = "ChangeTimer"
            cmd = 1
            value = int(input("What do you want to change the callback to in hours?\n"))
            return Type, cmd, value
 
        if (choice == 3):
            Type = "ViewTimer"
            cmd = 0
            value = 0
            return Type, cmd, value

        else:
            quit()

    else:
        quit()
