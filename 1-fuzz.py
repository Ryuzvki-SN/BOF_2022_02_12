#!/usr/bin/python
# Python Script (fuzz.py)

import socket
import sys
import time

ip = sys.argv[1]
port = int(sys.argv[2])

timeout = 5
buffer = b"A" * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((ip, port))
        s.recv(1024)
        s.send(buffer)
        print(s.recv(1024))
    except(Exception,):
        print("Fuzzing crashed at {} bytes".format(len(buffer)))
        sys.exit(0)
    s.close()
    buffer += b"A" * 100
    time.sleep(1)
