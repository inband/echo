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
    s.bind((host,port))
except:
    #OSError: [Errno 98] Address already in use
    print('Address is already in use')

#listen for connection
s.listen(5)

def client_child(conn, addr):
    q = b'quit\r\n'
    #conn, addr = accept
    print('Client connected: {}'.format(addr))
    while True:
        data = conn.recv(1024)
        if data == q:
            conn.shutdown(socket.SHUT_RDWR)
            print('Client disconnected: {}'.format(addr))      
            conn.close()
            return
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





