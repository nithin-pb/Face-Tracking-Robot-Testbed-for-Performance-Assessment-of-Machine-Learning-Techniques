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

main.py

'''

#global declarations and function calls

import serial
import numpy as np
import cv2
from PIL import Image
import os
import threading
import sys

#user defined calls
import luciserial
import lucisight
import setup
import lucitrajectroypattern
import fabric

def main():
	print("Do you want to retrain the data with your own face ? \n")
	luciserial.luciserialmain()
	lucisight.videoCapture(lucisight.cap)
	print("[INFO] exiting now!")
	sys.exit()

if __name__=='__main__':
	main()

	#t1 = threading.Thread(target=main,args=()) 
	#t2 = threading.Thread(target=lucisight.videoCapture, args=(lucisight.cap,) 
		
	#t1.start()
	#t2.start()

	#t1.join()
	#t2.join()

	

