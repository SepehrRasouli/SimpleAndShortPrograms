# generate a password with length "passlen" with no duplicate characters in the password

import random
def randome():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = input("How Much Long You Want Your Pass To Be?\n")
    passlen = int(passlen)
    try:
        p =  "".join(random.sample(s,passlen ))
    except ValueError:
        print("Too Long.")
        randome()
    else:
        print (p)
        randome()

randome()