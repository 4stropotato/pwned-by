# Day 3 - Making a the files to execute at the same time

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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip,server_port))


server.listen(5)

#####   DELETABLE   #####

from pathlib import Path               # ( OPTIONAL )
exec(Path('client.py').read_text())  # ( OPTIONAL )

#####   DELETABLE   #####

client, ip = server.accept()
confirmation = client.recv(8).decode('utf-8')
print(confirmation)


########################

# ( OPTIONAL ) THIS IS AN ALTERNATIVE WAY IF YOU WANT TO EXECUTE THE TWO FILES AT ONCE IF YOU'RE LAZY TO OPEN 2 SHELLS # You can delete this code if you liked to

########################

# pwning tmrw!
