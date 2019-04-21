'''
luci project final codes

nithin pb
Cochin University of Sciecne and Technolgy
Department of electronics

Copyright and licenses

Copyright (C) 2000-2018, Intel Corporation, all rights reserved.
Copyright (C) 2009-2011, Willow Garage Inc., all rights reserved.
Copyright (C) 2009-2016, NVIDIA Corporation, all rights reserved.
Copyright (C) 2010-2013, Advanced Micro Devices, Inc., all rights reserved.
Copyright (C) 2015-2016, OpenCV Foundation, all rights reserved.
Copyright (C) 2015-2016, Itseez Inc., all rights reserved.
Third party copyrights are property of their respective owners.

setup.py

'''
import luciserial
from time import sleep

#global variable declarations
#servo timings

ini=0


def servotime(): #servo clovk width min and max

	head = [0,180]	#servo1 maximum and minimum time period
	neck = [0,50]	#servo2 maximum and minimum time period
	hand = [40,0]	#servo3 maximum and minimum time period !!!!!!!!!!!!!!!rotating in reverse direction compared to another
	leg = [0,100]	#servo4 maximum and minimum time period
	foot = [0,180]	#servo5 maximum and minimum time period



def servoini():
	#initial positions
	x=90
	y=50
	h=0
	l=0
	f=0
	data="X{0:d}Y{1:d}H{2:d}L{3:d}F{4:d}".format(x,y,h,l,f)
	luciserial.servorotate2(data)
	try:
		x=90
		y=50
		h=0
		l=0
		f=0
		data="X{0:d}Y{1:d}H{2:d}L{3:d}F{4:d}".format(x,y,h,l,f)
		luciserial.servorotate2(data)
	except:
		print("Error! no serial module attached(Check setup.py for debug) ")
	sleep(.5)
	print("[INFO]reached initial position of servo")
	print("[INFO]reset complete!")

# length values
def lucilength():
	L1=5
	L2=27.7
	L3=18.7
	L4=8.5
	L5=0

	print("joint lenths are"+str(L1)+str(L2)+str(L3)+str(L4)+str(5))

#kinamatic parameters
#lengths fro equations
if __name__=='__main__':
	servotime()
	servoini()
