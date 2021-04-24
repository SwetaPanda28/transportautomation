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

host = 'localhost'       # Symbolic name meaning all available interfaces
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

        for i in data:
            #print hex(ord(i))
            mylist.append(hex(ord(i)))
            # Do a little bit more processing

            # Login Packet
            #'0x78', '0x78', '0xd', '0x1', '0x3', '0x55', '0x48', '0x80', '0x20', '0x82', '0x35', '0x79', '0x1', '0x1c', '0x8a', '0xbd', '0xd', '0xa']

            # Location Packet
            #['0x78', '0x78', '0x1f', '0x12', '0x12', '0x9', '0x3', '0xd', '0x12', '0xc', '0xc9', '0x4', '0x89', '0x50', '0xc1', '0x8', '0xe9', '0x20', '0x36', '0x0', '0x3c', '0x0', '0x1', '0x2e', '0xd0', '0x1b', '0x62', '0x0', '0x8d', '0x21', '0x1', '0x1c', '0xa8', '0x6', '0xd', '0xa']

            # Status Packet
            #['0x78', '0x78', '0xa', '0x13', '0x45', '0x0', '0x40', '0x0', '0x1', '0x1', '0x1d', '0xfa', '0x98', '0xd', '0xa']

        print len(mylist)

        if len(mylist) == 36:
                print "we have received Data Packet"

                f = open("gpsdata.txt", "a")
                f.write("%s\n" % mylist)
                f.close()

                print "Protocol Number : %s" %(mylist[3])

                x = int(mylist[3], 16)
                print x

                print "Time is %s : " %(mylist[4] + mylist[5] + mylist[6] + mylist[7] + mylist[8] + mylist[9] )
                print "Time is decimal is {} {} {} {} {} {}:".format(int(mylist[4],16) , int(mylist[5],16) , int(mylist[6],16) , int(mylist[7],16) , int(mylist[8],16) , int(mylist[9],16))

                print "Latitude is  %s : " % (mylist[11] + mylist[12] + mylist[13] + mylist[14]  )
                print "Latitude in Decimal is  {} {} {} {}:".format(int(mylist[11],16) , int(mylist[12],16) , int(mylist[13],16) , int(mylist[14],16))

                print "Longitude is  %s : " % (mylist[15] + mylist[16] + mylist[17] + mylist[18]  )
                print "Longitude in Decimal is  {} {} {} {}: ".format(int(mylist[15],16) , int(mylist[16],16) , int(mylist[17],16) , int(mylist[18],16 ))

                print "Speed is  %s : " % (mylist[19]  )
                print "Speed in decimal is  %d : " % int(mylist[19],16 )
        mylist = []
        print "**********************************************************"
        #Packet = decoder.decode(data)
        #print "Decoded Data: " + Packet
        #conn.sendall("Server Says:hi")

    except socket.error:
        print "Error Occured."
        break

conn.close()

