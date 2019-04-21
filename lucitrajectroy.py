# coding: utf-8

'''
luci project final codes

nithin pb
Cochin University of Sciecne and Technolgy
department of electronics

'''
#lucitrajectroy.py

#servo sent code test1
#trajectroy planning and servo controls


import luciserial
import lucisight

#the funtions makeluci to follow the face


def servoDecision1(xVal):
    if xVal>180:
        luciserial.servoRotate(1,1)
    elif xVal<140:
        luciserial.servoRotate(1,2)

def servoDecision2(yVal):
    if yVal>140:
        luciserial.servoRotate(2,1)
    elif yVal<100:
        luciserial.servoRotate(2,2)

def servoDecision3(yVal):
    if yVal>180:
        luciserial.servoRotate(3,1)
    elif yVal<160:
        luciserial.servoRotate(3,2)

def servoDecision4(hVal):
    if hVal>80:
        luciserial.servoRotate(4,1)
    elif hVal<120:
        luciserial.servoRotate(4,2)

def servoDecision5(xVal):
    if xVal>250:
        luciserial.servoRotate(5,1)
    elif xVal<50:
        luciserial.servoRotate(5,2)

class trajectoryface:

    def xyhwval(self,x,y,w,h):
        xval=x
        yavl=y
        wval=w
        hval=h
    

    def printval(self):
        print(x,y,w,h)
        



#trajectorys

#surprise, recognizing a familiar face
def reco():
    #move back quckly class
    #head x
    #neck y
    #hand =h
    #leg =l
    #foot =f
    #move hand and leg only
    servosent.ll = 40 # init of servvo3
    servosent.hh = 0 # init of servo4
    data="X{0:d}Y{1:d}H{2:d}L{3:d}F{4:d}".format(servosent.xx, servosent.yy, servosent.hh, servosent.ll, servosent.ff)
    luciserial.servorotate2(data)
    print(data)

    


#first shy contact
def shy():
    #shy pass value to class
    #head x
    #neck y
    #hand =h
    #leg =l
    #foot =f
    #move hand and leg only
    servosent.ll = 40 # init of servvo3
    servosent.hh = 0 # init of servo4
    data="X{0:d}Y{1:d}H{2:d}L{3:d}F{4:d}".format(servosent.xx, servosent.yy, servosent.hh, servosent.ll, servosent.ff)
    luciserial.servorotate2(data)
    print(data)

#closer inspection
def closer():
    #pass to class
    #head x
    #neck y
    #hand =h
    #leg =l
    #foot =f
    #move hand and leg only
    servosent.ll = 40 # init of servvo3
    servosent.hh = 0 # init of servo4
    data="X{0:d}Y{1:d}H{2:d}L{3:d}F{4:d}".format(servosent.xx, servosent.yy, servosent.hh, servosent.ll, servosent.ff)
    luciserial.servorotate2(data)
    print(data)

#move down and watch the face from a frog’s perspective  (looking cute)
def cute():
    #pass to class

    #head x
    #neck y
    #hand =h
    #leg =l
    #foot =f
    #move hand and leg only
    servosent.ll = 40 # init of servvo3
    servosent.hh = 0 # init of servo4
    data="X{0:d}Y{1:d}H{2:d}L{3:d}F{4:d}".format(servosent.xx, servosent.yy, servosent.hh, servosent.ll, servosent.ff)
    luciserial.servorotate2(data)
    print(data)


#go up again and nod (pretending an agreement)
def nod():
    #pass to class
    #move back quckly class
    #head x
    #neck y
    #hand =h
    #leg =l
    #foot =f
    #move hand and leg only
    servosent.ll = 40 # init of servvo3
    servosent.hh = 0 # init of servo4
    data="X{0:d}Y{1:d}H{2:d}L{3:d}F{4:d}".format(servosent.xx, servosent.yy, servosent.hh, servosent.ll, servosent.ff)
    luciserial.servorotate2(data)
    print(data)


def main():
	servoDecision5()
	servoDecision4()
	servoDecision3()
	servoDecision2()
	servoDecision1()


if __name__=='__main__':
	main()