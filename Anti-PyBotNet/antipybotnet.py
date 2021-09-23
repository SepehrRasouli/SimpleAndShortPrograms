import binascii
import os
import time
path = input("Complete Path to the File => ") + '\\'
filename = input("Filename => ")
path_with_filename = path + filename
with open(path_with_filename, 'rb') as f:
    content = f.read()
data = binascii.hexlify(content)

if  '7079626f746e6574' in data.decode("utf-8"):
    print("The file is infected.")
    time.sleep(10)
else:
    print("It seems like that the file is clean...")
    time.sleep(10)
