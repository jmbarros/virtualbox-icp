#!/usr/bin/python 

import socket
import fcntl
import struct
import os

host="/etc/hosts"
icp="/opt/ibm-cloud-private-ce-2.1.0.2/cluster/hosts"

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ip=get_ip_address('enp0s3')
hostname=socket.gethostname()

file = open( host , "w")
file.write("127.0.0.1 localhost \n")
file.write( ip + " " + hostname + "\n")
file.close()

file = open( icp, "w")
file.write("[master] \n")
file.write( ip + "\n")
file.write("[worker] \n")
file.write( ip + "\n")
file.write("[proxy] \n")
file.write( ip + "\n")
file.close()
