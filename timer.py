import time

def countdown_timer(sec):
    while sec>0:
        min=int(sec/60)
        secs=int(sec%60)
        timer=f"{min}:{secs}"
        print(timer)
        sec-=1
    print("times up!!!")

time=input('Enter time in seconds:-  ')
countdown_timer(int(time))