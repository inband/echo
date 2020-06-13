import sys
import socket


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

#accept connection
conn, addr = s.accept()

q = b'quit\r\n'
while True:
    data = conn.recv(1024)
    if data == q:
        s.shutdown(socket.SHUT_RDWR)
        print('Client disconnected: {}'.format(addr))
    else:
        print(data.decode('utf-8'))
        print(data.decode('ascii'))
        print(data)
        conn.send(data)
                
print(conn)
print(addr)

#s.shutdown(socket.SHUT_RDWR)
#s.close()




