# Code to open the socket, send the command and then retrieve the data
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # file handle that doesn't have any data associated with it yet
mysock.connect(('data.pr4e.org', 80)) # reach out and connect that socket to a destination accross the internet with the domain name data.pr4e.org; 80 is the port
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # http command; the .encodde is there because there are strings in python that are in unicode and we need to get them into utf-8
mysock.send(cmd)

while True:
    data = mysock.recv(512) # receive up to 512 characters
    if len(data) < 1:
        break
    print(data.decode(),end='') # print the data and decode it from utf-8 to unicode

mysock.close() # close connection
