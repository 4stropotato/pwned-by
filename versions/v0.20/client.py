# Day 2
# 7 Nothing much will happen here.

import socket

def ip_address():
    global server_ip
    serv_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serv_ip.connect(("8.8.8.8", 80))
    server_ip = serv_ip.getsockname()[0]
    serv_ip.close()
    return server_ip

########################

server_ip = ip_address() # 8
server_port = 5555

########################

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 9

# 10 since the server is now listening..
client.connect((server_ip,server_port))  # 11
confirmation = 'Connect!'.encode('utf-8') # 17
client.send(confirmation) # 18

########################

# 8     Should be the same ip and port as the server.py
# 9     concatinating ip and tcp socket
# 11    initiate 3 way handshake to the server_ip and server_port, let's go back to server.py
# 17    let's convert ('Connect!') to bytes and assign it to confimation.
# 18    let's send the confirmation to the server. Let's go to server.py

########################

# pwning tmrw!
