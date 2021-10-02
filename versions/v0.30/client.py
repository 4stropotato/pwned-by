# Day 4 - Cleaning the code + sending message from client to server

import socket

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


def client_conn(): # 4
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((server_ip,server_port))

def message_send(): # 5
    confirmation = 'Connect!'.encode('utf-8') # 6
    client.send(confirmation) # 7

client_conn()
message_send()

#########################

# 4     Cleaning
# 5     Sending message to the server
# 6     We will be encoding the string ('Connect!') to utf-8 first and then...
# 7     We are going to send it to the client variable. Also given from (client = socket.socket(socket.AF_INET, socket.SOCK_STREAM))

#########################

# pwning tmrw!