import serial
import os
import random
import time
ser=serial.Serial(port="/dev/ttyACM0",baudrate=115200,timeout=1)
while True:
    x=random.randint(0,180)
    y=20
    h=0
    l=40
    f=150
    
    
    x=input("x")
    #y=input("y")
    #h=input("h")
    #l=input("l")
    #f=input("f")


    data="X{0:d}Y{1:d}H{2:d}L{3:d}F{4:d}".format(x,y,h,l,f)
    #print("[INFO]data ready to sent")
    ser.write(data)
    #print("[INFO]data sent")
    a=input("a")
    b=input("b")
    c=input("c")
    d=input("d")
    e=input("e")
    data="A{0:d}B{1:d}C{2:d}D{3:d}E{4:d}".format(a,b,c,d,e)
    #print("[INFO]data ready to sent")
    ser.write(data)
