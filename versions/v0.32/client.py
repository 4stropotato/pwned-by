# Day 6 Completing the Send/Receive functions for both scripts (single script won't work)

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


def message_send(string, size):
    body = string.encode('utf-8')
    length = len(body)
    header = str(length).encode('utf-8')
    header += b' ' * (size - len(header))
    client.send(header)
    client.send(body)

def message_recv(size):
    while True:
        header = client.recv(size).decode('utf-8')
        if header:
            body_size = int(header)
            body = client.recv(body_size).decode('utf-8')
            break
    return body


def client_conn():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((server_ip,server_port)) 


client_conn()

# testing
print(message_recv(2))

print(message_recv(2))

print(message_recv(2))

# pwning tmrw!