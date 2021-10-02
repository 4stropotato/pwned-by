# Day 4 - Cleaning the code + sending message from client to server
#       1 As a programmer, it is very important to make a clean code. (Readable and Organized) So it is important that we arrange our code according to it's functionality. 

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



def server_conn(): # 1
    global server,client,ip
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip,server_port))
    server.listen(5)
    client, ip = server.accept()

def message_recv(): # 2
    confirmation = client.recv(8).decode('utf-8') # 3
    print(confirmation)

server_conn()
message_recv()

#########################

# 1     Cleaning # Since we only have few codes yet, we can put all the remaining code in a container where we can call to make a connection.
# 2     Receiving message from client
# 3     from client that were given from (client, ip = server.accept()), we will be receiving 8 bytes from the client and we will be decoding it.

#########################

# pwning tmrw!