# # Day 4 Cleaning the code

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


def client_conn(): # new function
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((server_ip,server_port))

def message_send(): # new function
    confirmation = 'Connect!'.encode('utf-8')
    client.send(confirmation)

client_conn()
message_send()

# pwning tmrw!