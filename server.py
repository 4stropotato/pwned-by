# Day 4 Cleaning the code
# As a programmer, it is very important to make a clean code. (Readable and Organized) So it is important that we arrange our code according to it's functionality. 
# Header sned/receive

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



def server_conn(): # new function # Since we only have few codes yet, we can put all the remaining code in a container where we can call to make a connection.
    global server,client,ip
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip,server_port))
    server.listen(5)
    #####   DELETABLE   #####
    from pathlib import Path            # PATHLIB IS INJECTED SO THAT WE HAVE TO EXECUTE 1 FILE ONLY
    exec(Path('client.py').read_text()) # PATHLIB IS INJECTED SO THAT WE HAVE TO EXECUTE 1 FILE ONLY
    #####   DELETABLE   #####
    client, ip = server.accept()

def message_recv(): # new function
    confirmation = client.recv(8).decode('utf-8')
    print(confirmation)

server_conn()
message_recv()

# pwning tmrw!