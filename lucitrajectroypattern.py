# coding: utf-8

'''
luci project final codes

nithin pb
Cochin University of Sciecne and Technolgy
department of electronics

'''
#lucitrajectroypattern.py

#servo sent code test1
#trajectroy planning and servo controls


import luciserial
import lucisight
import time
global d
d=0
global c
c=0
def passi(d):
    global c
    if d==1:
            print("[INFO] face found!!")
            c=0
            #write a funtion that always calls the pattern generator and checks the value of d 
    else:
        faceLook(d)
        c=c+1

def faceLook(d):
    if (d==0): #if no face is available
        if (c>=60):
            #print(c)      
            data="A120sB30C30D20E0"
            luciserial.servorotate2(data)
            print("[INFO] error 10")
        





def main():
    print("[INFO]lucitrajectorypattern running")
    faceLook() 



if __name__=='__main__':
	main()