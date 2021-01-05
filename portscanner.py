#!/usr/bin/python3
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "178.33.238.61"
port = 80
def portScan(port):
    if s.connect_ex((host, port)):
        print("the port is closed")
    else :
        print("the port is open")


portScan(port)
     
