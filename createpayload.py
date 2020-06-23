import subprocess
import sys

#getmsflocation from main.py

def main():
    #test
    print(useros)
    print("\n")
    print("os")

def os():
    useros = 0
    if sys.platform.startswith('linux'):
        useros = "linux"
    elif sys.platform.startswith('win'):
        useros = "windows"
    else:
        n = int(input("Could not detect OS automatically.\n\nAre you generating from: \n1. Windows\n2. Linux\n"))
        for i in range(0,2):
            choice = int(input('Enter a Number: '))
            if (choice == 1):
                useros = "windows"
            elif (choice == 2):
                useros = "linux"
            else:
                print('Invalid OS. Exitting')
                quit()

def payloadtype():
    os = 0
    n = int(input("What type payload are you generating?\n")
            for i in range(0,5):
                print("1. Windows\n")
                print("2. Linux\n")
                print("3. Python\n")
                print("4. PHP\n")
                print("5. More Options"\n\n)
                #print("6. Back\n\n")

                choice = int(input("Enter a Number: "))
                
                if (choice == 1):
                    os = "windows"
                if (choice == 2):
                    os = "linux"
                if (choice == 3):
                    os = "python"
                if (choice == 4):
                    os = "php")
                if (choice == 5):
                    print("\n\n\n\n\n\n\n"
                    for i in range(0,6):
                        print("1. Multi\n")
                        print("2. cmd\n")
                        print("3. java\n")
                        print("4. tty\n")
                        print("5. osx"\n)
                        print("6. Generic\n\n:")
                        #print("7. Back\n\n")
                        
                        choice = int(input("Enter a Number: "))

                            if (choice == 1):
                                os = "Multi"
                            if (choice == 2):
                                os = "cmd"
                            if (choice == 3):
                                os = "java"
                            if (choice == 4):
                                os = "tty"
                            if (choice == 5):
                                os = "osx"
                            if (choice == 6):
                                os = "generic"
                    else:
                        quit()
            else:
                quit()


if __name__=='__main__':
    main()
