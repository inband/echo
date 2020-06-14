import sys
import socket
import os
#import threading


host = ''
port = 7

address_family = socket.AF_INET
transport_protocol = socket.SOCK_STREAM

#create socket
s = socket.socket(address_family, transport_protocol)

#bind to socket
try:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
except:
    #OSError: [Errno 98] Address already in use
    print('Address is already in use')

#listen for connection
s.listen(5)

def help():
    return b'Use quit or quit() to exit\r\n'

def quit(data):
    q = b'quit\r\n'
    q_brackets = b'quit()\r\n'
    if data == q:
        return True
    elif data == q_brackets:
        return True
    else:
        return False


def client_child(conn, addr):
    #q = b'quit\r\n'
    print(pid)
    #conn, addr = accept
    print('Client connected: {}'.format(addr))
    while True:
        data = conn.recv(1024)
        if quit(data):
            conn.shutdown(socket.SHUT_RDWR)
            print('Client disconnected: {}'.format(addr))      
            conn.close()
            return
        elif data == b'help\r\n':
            conn.send(help())
        else:
            #print(data.decode('utf-8'))
            #print(data.decode('ascii'))
            print(data)
            conn.send(data)


while True:
    #threads = list()
    conn, addr = s.accept()
    #t = threading.Thread(target=client_thread(conn, addr))
    #t = threading.Thread(target=client_thread, args=(conn, addr,))
    #print(t)
    #threads.append(t)
    #t.start()
    pid = os.fork()
    if pid == 0:
        client_child(conn, addr)





