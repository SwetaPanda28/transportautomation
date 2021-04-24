__author__ = 'vivek'
__author__ = 'vivek'

'''
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('192.168.1.10', 8000))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        print buf
        #break
'''

import socket

import csv

f= open("gpsdata.txt","w+")
f.close()


from select import select

#from impacket import ImpactDecoder

host = '192.168.1.10'       # Symbolic name meaning all available interfaces
port = 8000     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
#decoder = ImpactDecoder.IPDecoder()

print host , port
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
mylist = []
while True:

    try:
        data = conn.recv(1024)


        # Here we need to see if the data is an HTTP Data. If the Data is HTTP Data, handle is accordingly.
        if not data: break
        print "----------------------------------------------------------"
        print "Client Says: " + data
        print "##########################################################"


        print "**********************************************************"
        #Packet = decoder.decode(data)
        #print "Decoded Data: " + Packet
        #conn.sendall("Server Says:hi")

    except socket.error:
        print "Error Occured."
        break

conn.close()


