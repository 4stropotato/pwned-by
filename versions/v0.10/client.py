# Day 1 - getting your own ipaddress in python
# 2     Notice that it has the same code. Yes, because we are initializing the code to with the same ip address to communicate to each other

import socket

def ip_address():
    global server_ip
    serv_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serv_ip.connect(("8.8.8.8", 80))
    server_ip = serv_ip.getsockname()[0]
    serv_ip.close()
    return server_ip

server_ip = ip_address()

print(server_ip)

# pwning tmrw!
