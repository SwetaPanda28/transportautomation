__author__ = 'vivek'

import socket
import threading
import math
from decimal import *
import datetime
from django.utils import timezone
from django.db import connection

import os
import django


#os.environ["DJANGO_SETTINGS_MODULE"] = 'TrackingProject.settings'


#from .models import *
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TrackingProject.settings")

django.setup()

from TrackingProject.models import *


f= open("gpsdatathreaded.txt","w+")
f.close()

runnning= open("runninglogs.txt","w+")
runnning.close()

mylist = []

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = '192.168.1.10'
        self.port = 8000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(1)
        while True:
            client, address = self.sock.accept()
            print('Connected by', address)
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        mylist = []
        #print " I am here"
        size = 1024
        while True:
            try:
                data = client.recv(size)
                print "data is"
                print data
                if not data: break
                print "----------------------------------------------------------"
                print "Client Says: " + data
                print "##########################################################"

                for i in data:
                    # print hex(ord(i))
                    #print "getting hex repr"

                    #355480020823579
                    mylist.append(hex(ord(i)))
                    # Do a little bit more processing

                    # Login Packet
                    #'0x78', '0x78', '0xd', '0x1', '0x3', '0x55', '0x48', '0x80', '0x20', '0x82', '0x35', '0x79', '0x1', '0x1c', '0x8a', '0xbd', '0xd', '0xa']

                    # Location Packet
                    #['0x78', '0x78', '0x1f', '0x12', '0x12', '0x9', '0x3', '0xd', '0x12', '0xc', '0xc9', '0x4', '0x89', '0x50', '0xc1', '0x8', '0xe9', '0x20', '0x36', '0x0', '0x3c', '0x0', '0x1', '0x2e', '0xd0', '0x1b', '0x62', '0x0', '0x8d', '0x21', '0x1', '0x1c', '0xa8', '0x6', '0xd', '0xa']

                    # Status Packet
                    #['0x78', '0x78', '0xa', '0x13', '0x45', '0x0', '0x40', '0x0', '0x1', '0x1', '0x1d', '0xfa', '0x98', '0xd', '0xa']

                print len(mylist)

                if len(mylist) == 18:
                    print '############################'
                    print "Login Packet from!"
                    print client, address
                    imie = mylist[4].replace("0x", "") + mylist[5].replace("0x", "") + mylist[6].replace("0x", "") + mylist[7].replace("0x", "") + mylist[8].replace("0x", "") + mylist[9].replace("0x", "") + mylist[10].replace("0x", "") + mylist[11].replace("0x", "")
                    print imie
                    f = open("gpsdata" + imie + ".txt", "a")
                    f.write("%s\n" % mylist)
                    f.close()
                    print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'

                elif len(mylist) == 36:
                    print "we have received Data Packet from %s" %(imie)

                    f = open("gpsdata" + imie + ".txt", "a")
                    f.write("%s\n" % mylist)
                    f.close()

                    print "Protocol Number : %s" % (mylist[3])

                    x = int(mylist[3], 16)
                    print x

                    print "Time is %s : " % (mylist[4] + mylist[5] + mylist[6] + mylist[7] + mylist[8] + mylist[9] )
                    print "Time is decimal is {} {} {} {} {} {}:".format(int(mylist[4], 16), int(mylist[5], 16),
                                                                         int(mylist[6], 16), int(mylist[7], 16),
                                                                         int(mylist[8], 16), int(mylist[9], 16))


                    print "Latitude is  %s : " % (mylist[11] + mylist[12] + mylist[13] + mylist[14]  )
                    decLatHex = mylist[11].replace("0x","") +  mylist[12].replace("0x","") +  mylist[13].replace("0x","") +  mylist[14].replace("0x","")

                    #decLat= int((str(int(mylist[11], 16))  + str(int(mylist[12], 16) ) + str(int(mylist[13], 16))  + str(int(mylist[14], 16))))
                    decLat = int(decLatHex,16)
                    tempLat = Decimal(decLat)/Decimal(30000)

                    ############################### Degress #########################################

                    degreesLat = Decimal((tempLat)/Decimal(60))

                    print degreesLat

                    runnning = open("runninglogs.txt", "a")
                    runnning.write("%s %s\n" % (degreesLat,decLatHex))
                    runnning.close()

                    #tempdegreesLat_dec, tempdegreesLat_int = math.modf(tempdegreesLat)  # (0.5678000000000338, 1234.0)
                    #degreesLat = tempdegreesLat_int

                    ################################ Minutes ###################################@

                    #tempMinutesLat = tempdegreesLat_dec/60
                    #tempMinutesLat_dec, tempMinutesLat_int = math.modf(tempMinutesLat)

                    ################################# Seconds ###################################

                    #tempSecondsLat = tempMinutesLat_dec / 60
                    #tempSecondsLat_dec, tempSecondsLat_int = math.modf(tempSecondsLat)


                    ############################################################################

                    #print tempLat



                    print "Longitude is  %s : " % (mylist[15] + mylist[16] + mylist[17] + mylist[18]  )
                    print "Longitude in Decimal is  {} {} {} {}: ".format(int(mylist[15], 16), int(mylist[16], 16),
                                                                          int(mylist[17], 16), int(mylist[18], 16))


                    decLongHex = mylist[15].replace("0x","") +  mylist[16].replace("0x","") +  mylist[17].replace("0x","") +  mylist[18].replace("0x","")

                    # decLat= int((str(int(mylist[11], 16))  + str(int(mylist[12], 16) ) + str(int(mylist[13], 16))  + str(int(mylist[14], 16))))
                    decLong = int(decLongHex, 16)
                    tempLong = Decimal(decLong) / Decimal(30000)

                    ############################### Degress #########################################

                    degreesLong = Decimal((tempLong) / Decimal(60))

                    print degreesLong
                    runnning = open("runninglogs.txt", "a")
                    runnning.write("%s %s\n" % (degreesLong, decLongHex))
                    runnning.close()



                    print "Speed is  %s : " % (mylist[19]  )
                    print "Speed in decimal is  %d : " % int(mylist[19], 16)

                    print "Saving Data"

                    p = Warehouse(insertdate=datetime.datetime.now(), generateddate=datetime.datetime.now(), latitude=degreesLat,longitude=degreesLong,imienumber= Device.objects.get(imienumber = 352887078364431))
                    p.save()


                else:
                    print "Other Packet"
                mylist = []
                print "**********************************************************"
                # Packet = decoder.decode(data)
                #print "Decoded Data: " + Packet
                #conn.sendall("Server Says:hi")


            except:
                client.close()
                return False


if __name__ == "__main__":
    while True:
        port_num = 8000
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()


# Got the initial code from

#https://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client

