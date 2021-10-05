# Day 8 - The Json Module
# 1     Json stands for Javascript Object Notation. Json uses a data map structure and usess very less data unlike XML. ie. {'a':[{'x':1},{'y':2}]} 
#       Basically, Like what we did in with message_send and message_recv, we are importing the json module for the complicated results. 
      
import socket
import json # 2

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

def json_send(): # 3
    jsondata = json.dumps(data) # 4
    client.send(jsondata.encode()) # 5

def json_recv(size=1024): # 6
    data = '' # 7
    while True:
        try: # 8
            data += client.recv(size).decode().rstrip()
            return json.loads(data)
        except ValueError: # 9
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

server_conn()

# testing


#########################

# 2     importing json module that comes with the standard modules of python3
# 3     Unlike what we have did previously on message_send/recv, this is straight forward, we are not sending a header to the receiver.
# 4     dumps converts python objects into a json string
# 5     sending it to the receiver.
# 6     this time, the default is 1024. because...
# 7     we are making a chunk. it is a container that holds the message that we are receiving.
# 8     we are going in an infinite loop again and try if we are still receiving a data from the sender.
#       If we received, we will be going to encode it and strip the white space from the right to avoid unnecessary white spaces.
#       and then, we are appending the chunk to the (data = ''). and return the the entire chunk by loading the dump (json.load())
# 9     If it returns a ValueError while we are still receiving a data, continue the iteration. (kinda tricking the machine in a different way)

# Q     What is this json tool for?
#       - We need this tool for larger outputs.
#       If we need that for larger output, Why not we increase the byte size of the message_recv/message_send function and use it?
#       - This can be useful for complicated output. Also in a .json files.
#       How can we test this json tool?
#       - We are going to make a new function on the next-next tutorial.

#########################

# pwning tmrw!