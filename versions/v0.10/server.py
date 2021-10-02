# Day 1 getting your own ipaddress in python..
# 1     ALthough there are many easy ways, this is the most effective way to get the ip of your own system using python.

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
