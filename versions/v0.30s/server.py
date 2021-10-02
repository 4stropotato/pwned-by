# Day 4 - Cleaning the code + sending message from client to server

import socket

def ip_address():
    global server_ip
    serv_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serv_ip.connect(("8.8.8.8", 80))
    server_ip = serv_ip.getsockname()[0]
    serv_ip.close()
    return server_ip

#########################

server_ip = ip_address() 
server_port = 5555 

#########################



def server_conn():
    global server,client,ip
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip,server_port))
    server.listen(5)
    #####   DELETABLE   #####
    from pathlib import Path
    exec(Path('client.py').read_text())
    #####   DELETABLE   #####
    client, ip = server.accept()

def message_recv(): # new function
    confirmation = client.recv(8).decode('utf-8')
    print(confirmation)

server_conn()
message_recv()

# pwning tmrw!