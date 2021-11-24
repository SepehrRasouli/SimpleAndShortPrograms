import time
import winsound
frequency = 2500
duration = 5000

def timer(a):
    while a > 0:
        a -= 1
        time.sleep(1)
        print(a)

    if a == 0:
        winsound.Beep(frequency, duration)
        ended()

def secoundtim():
    secound = input("How Many Secounds Do You Want To Count Down? When The Count Down Ends , A Beep Sound Will Start And Continue For 5 Secounds\n")
    while not secound.isdigit():
        print("Enter A Digit !")
        secound = input("How Many Secounds Do You Want To Count Down?\n")

    secound = int(secound)
    timer(secound)

def ended():
    yon = input("Do You Want To Return ? Y or N\n")
    if yon == "Y":
        secoundtim()
    
    if yon == "N":
        SystemExit
    
    else:
        ended()

secoundtim()