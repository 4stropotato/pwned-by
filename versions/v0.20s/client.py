# Day 2
# Nothing much will happen here.

import socket

def ip_address():
    global server_ip
    serv_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serv_ip.connect(("8.8.8.8", 80))
    server_ip = serv_ip.getsockname()[0]
    serv_ip.close()
    return server_ip

########################

server_ip = ip_address() # v0.2 Should be the same ip and port as the server.py
server_port = 5555 # v0.2 

########################

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # concatinating ip and tcp socket

# since the server is now listening..
client.connect((server_ip,server_port)) # 1>>>>>>>>>>>>>> initiate 3 way handshake to the server_ip and server_port, returning back to server.py 2>>>>>>>>>>> 
confirmation = 'Connect!'.encode('utf-8') # let's convert the string to bytes
client.send(confirmation) # 3>>>>>>>>>>>> let's send the confirmation to the server 4>>>>>>>>>>

# pwning tmrw!
