# Day 5 Sending message (Client), Receiving (Server)


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


# 2 making message_send function.

def message_send(string, size): # 3
    body = string.encode('utf-8') # 4
    length = len(body) # 5
    header = str(length).encode('utf-8') # 6
    header += b' ' * (size - len(header)) # 7
    client.send(header) # 8
    client.send(body) # 9
    # 10 let's go to the server.py


def client_conn():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((server_ip,server_port)) 


client_conn()

# testing
message_send('Connected!', 2)

message_send('4stropotato', 2)

message_send('If you were able to print this from the server, You are awesome!', 2)



########################

# 3 new function with param string(message), and the size of bytes so that the server will know how much packet it has to receive.
# 4 we have to convert it to bytes so that every machine would understand the message.
# 5 counting the length of the string and,
# 6 converting it again to bytes. ie. 'string' has a length of 5 and converting 5 into a byte, turning b'5' 
# 7 adding spaces to the filler, ie. we gave the args 'string' as the string and 8 as the size.
#   the length of string (b'5') is 1, so 8 - 1 = 7,
#   we will make seven white spaces in bytes and add it to the filler. (b'5       ') <- this has 7 white spaces
# 8 as we gave 8 bytes for the size, we will send an 8 bytes message to the server (b'5       ').
#   We will send the filler first as the header so that the server will know how many packets it will be going to receive next time.
# 9 now we will send the actual message.

########################

# pwning tmrw!