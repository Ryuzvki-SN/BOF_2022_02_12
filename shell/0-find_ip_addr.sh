#! /bin/bash

for ip in 192.168.72.{1..254}; do
ping -c 1 -t 1 $ip > /dev/null && echo “${ip} is up”; 
done