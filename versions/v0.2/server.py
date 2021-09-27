# Day 2 The socket module
# As you noticed, we already used socket module as on the first day. The socket module is the core module that we are using since this course is more about networking.

import socket

def ip_address():
    global server_ip
    serv_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serv_ip.connect(("8.8.8.8", 80))
    server_ip = serv_ip.getsockname()[0]
    serv_ip.close()
    return server_ip

########################

server_ip = ip_address() # we can change the server ip to any ip from our machine. ie. 192.168.1.8
server_port = 5555 # v0.2 We can choose any available ports on 65535 or 1111111111111111 in binary

########################

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # We're going to concatenate our IPv4 (AF_INET) to our Transmission Control Protocol socket (SOCK_STREAM) or TCP. By the way (SOCK_DGRAM) is User Defind Protocol socket or UDP that is less reliable that TCP. 
server.bind((server_ip,server_port)) # binding local end port's number to the ip

# The server's port is open, we can now listen the the incoming connection, we can now listen to the incoming connections.
server.listen(5) # 5 is queue size through the parameter backlog. Let's go to the client.py 1>>>>>>>>>

client, ip = server.accept() # 2>>>>>>>>>> coming back to this file to accept the connection request from the client.py that gives 2 variables; client = connection data, and ip = returns tuple of ip of the client and port

# Now we received the ip and port...
# Let's have a confirmation that the client is sending a message to our system 3>>>>>>>>>>>

confirmation = client.recv(8).decode('utf-8') # 4>>>>>>>>>>>> Convert back the bytes to string and assign it to the variable confirmation
print(confirmation) # Check if working!

# if the message shows 'Connect!', the code is working and we can now start hacking the system!
# pwning tmrw!