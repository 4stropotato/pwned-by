# Day 5 Sending message (Client), Receiving (Server)
# Today, we are going to start a conversation within the connection we had made. To make it more understandable, we will move to the client.py to make a message_send function. >>>>>>>>>>>>>>>>1

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

# 2>>>>>>>>>>>>>> receiving the message. since the clienct sent message twice, we will be receiving a message twice as well. One for the header, the other one for the body or the actual message.
def message_recv(size): # new function. message_recv with size 8
    while True: # infinite loop until we confirm that we have received the header.
        header = client.recv(size).decode('utf-8')
        if header: # if we are not receiving a message it will automatically give as false, but if the header has a value, then it will be turning True
            body_size = int(header) # received bytes with white spaces b'5       '. if we convert it to int it will be going to 5. and that 5 will be the new size for the body
            body = client.recv(body_size).decode('utf-8') # the body size for the body is the size that we gave from the header.
            break # after a sucessful conversation we will break the loop.
    return body # returning the body's value

def server_conn():
    global server,client,ip
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip,server_port))
    server.listen(5)
    #####   DELETABLE   #####
    from pathlib import Path            # PATHLIB IS INJECTED SO THAT WE HAVE TO EXECUTE 1 FILE ONLY
    exec(Path('client.py').read_text()) # PATHLIB IS INJECTED SO THAT WE HAVE TO EXECUTE 1 FILE ONLY
    #####   DELETABLE   #####
    client, ip = server.accept()

server_conn()

# testing
print(message_recv(2))

print(message_recv(2))

print(message_recv(2))
# pwning tmrw!