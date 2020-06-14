###Bug TIME_WAIT

Server side:
'''
OSError: [Errno 98] Address already in use
'''

Client side:
'''
nat@dev:~$ sudo ss -an | grep TIME
tcp   TIME-WAIT   0        0                                          127.0.0.1:7                                               127.0.0.1:60210  
'''


This error occurs when the TCP connection is actively disconnected.
From **socket** use setsockopt(level, optname, value: int)

socket.SOL_SOCKET is 
'''
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

''' 

Information regarding the level, socket.SOL_SOCKET is found in:
'''
man 2 setsockopt 

'''


Information on socket.SO_REUSEADDR is found in:
'''
man 7 socket
'''



