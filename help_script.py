# Python Script (badchar.py)

print("\t----------------------")
print("\t|    BAD CHARACTER   |")
print("\t----------------------")
print("\n[+] Example No Badchar (Please include \\x00) => Enter Bad Characters: \\x00")
print("[+] Example Got Badchar => Enter Bad Characters: \\x02\\x03\\x04")

INPUTS = input("\n[+] Enter Bad Characters: ")
OUTPUT_INPUTS = r"{0}".format(INPUTS)
LISTREM = INPUTS.split("\\x")
LISTBADCHAR = r""
for x in range(1, 256):
    if "{:02x}".format(x) not in LISTREM:
        LISTBADCHAR += r"\x" + "{:02x}".format(x)
print(LISTBADCHAR)
