# Day 7 - Making the message adaptable to any type.
# 1     There are cases that we like to send message other than string like integer, float, list, tuple, or dictionary.
#       We could mess our code if we are going to derive it again manually so I decided to make it automated.

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


def message_send(string, size=8): # 2
    no_str = False # 3
    if type(string) != str: # 4
        string =str(string)
        no_str = True # 5
    body = string.encode()
    length = len(body)
    header = str(length).encode()
    header += b' ' * (size - len(header))
    client.send(header)
    client.send(body)
    if no_str == True: # 6
        client.send('T'.encode())
    else:
        client.send('F'.encode())

def message_recv(size=8):
    while True:
        header = client.recv(size).decode()
        if header:
            body_size = int(header)
            body = client.recv(body_size).decode()
            no_str = client.recv(1).decode() # 7
            break
    if no_str == 'T': # 8
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
msg1 = message_recv()
msg2 = message_recv()
msg3 = message_recv()

print(msg1)
print(type(msg1))

print(msg2)
print(type(msg2))

print(msg3)
print(type(msg3))

#########################

# 2     We are giving the default parameter (size = 8) if size were not given, if .encode() is empty, it will automatically format it to 'utf-8'.
# 3     We will be going to set a variable that is always false, ( becase the default is string )
# 4     If the message is not string, then we will make it a string. ( very straight forward )
# 5     But we are going to change the no_str variable to become true as an exchange
# 6     If it is True, we are going to send an additional message that contains 'T' or 'F'( True of False )
# 7     Before we break the loop, We are going to receive the 'T' or 'F' message and assign it back to no_str
# 8     Now if no_str is True, We are going to evaluate the body to return it's true type.

#########################

# pwning tmrw!