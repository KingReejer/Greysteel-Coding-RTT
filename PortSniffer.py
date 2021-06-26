#!/usr/bin/python
import time
import datetime
import socket
import subprocess
import sys


subprocess.call('clear', shell=True)

server = input("What is the host IP: ")
start_now = datetime.datetime.now()

print("*"*60)
print(start_now.strftime("\nStarting scan at: %H:%M:%S \n"))
print("*"*60)


#Check for ports
for port in range(21, 5500):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((server, port))
    if result ==0:
            time.sleep(.25)
            print("\nPort {} is open\n".format(port))
sock.close()

print("*"*60)
time.sleep(.25)
finished_now = datetime.datetime.now()
print(finished_now.strftime("\n Your scan has finished at: %H:%M:%S \n"))
print("*"*60)
time.sleep(.25)
print(f"\nTime taken is: {finished_now - start_now }\n")
print("*"*60)
