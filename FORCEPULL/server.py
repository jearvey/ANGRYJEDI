import socket
from _thread import *
import threading 
import message 
import signal

print_lock = threading.Lock() 
 
def threaded(c): 
    while True: 
        data = c.recv(4096) 
        if not data: 
            #print('No data received') 
            print_lock.release() 
            break 
        reply = message.BuildTask(data)
        c.send(reply) 
    c.close() 
  
#safely exit program when use of Ctrl C
def signal_handler(signal, frame):
    sys.exit(0)

def Main(): 
    host = "localhost" 
    port = 1776
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reopen if addr in use
    s.bind((host, port)) 
    print("socket binded to port", port) 
    s.listen(5) 
    print("socket is listening") 
    while True: 
        c, addr = s.accept() 
        print_lock.acquire() 
        #print('Connected to :', addr[0], ':', addr[1]) 
        start_new_thread(threaded, (c,)) 
    s.close()
    signal.signal(signal.SIGINT, signal_handler)
  
  
if __name__ == '__main__': 
    Main() 
