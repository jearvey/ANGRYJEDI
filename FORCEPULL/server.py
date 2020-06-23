import socket
from _thread import *
import threading 
import message  

print_lock = threading.Lock() 
 
def threaded(c): 
    while True: 
        data = c.recv(1024) 
        if not data: 
            print('No data received') 
            print_lock.release() 
            break 
        reply = c.message(data)
        c.send(reply) 
    c.close() 
  
  
def Main(): 
    host = "localhost" 
    port = 1776
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
    s.listen(5) 
    print("socket is listening") 
    while True: 
        c, addr = s.accept() 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 
