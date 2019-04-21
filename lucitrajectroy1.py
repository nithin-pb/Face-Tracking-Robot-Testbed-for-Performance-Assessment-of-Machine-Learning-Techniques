# coding: utf-8

'''
luci project final codes

nithin pb
Cochin University of Sciecne and Technolgy
department of electronics

'''
#lucitrajectroy.py


#trajectroy planning and servo controls

#servo rotationg funtion test2


import luciserial

#the funtions makeluci to follow the face

def servosent(x,y,w,h):
    centerx=(x+w)/2
    centery=(y+h)/2
    

    servosent.xx = int(centerx)
    servosent.yy = int(centery)

    output = "X{0:d}Y{1:d}Z".format(servosent.xx, servosent.yy)
    print(x, y, servosent.xx, servosent.yy , output)
    luciserial.servorotate2(output)
'''
#trajectorys

#surprise, recognizing a familiar face
def reco():


#first shy contact
def shy():


#closer inspection
def closer():


#move down and watch the face from a frog’s perspective  (looking cute)
def cute():



#go up again and nod (pretending an agreement)
def nod():
'''


def main():
	servoDecision5()
	servoDecision4()
	servoDecision3()
	servoDecision2()
	servoDecision1()


if __name__=='__main__':
	main()