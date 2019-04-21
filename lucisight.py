'''
luci project final codes
nithin pb
Cochin University of Sciecne and Technolgy
department of electronics
'''
#lucisight.py
#camera initialization and processing
import cv2
import numpy as np
from imutils.video import VideoStream
from PIL import Image
import argparse
import imutils
import time
import os 
import pickle
import socket


#user defined call

import lucitrajectroy
import lucitrajectroy1
import setup
import lucitrajectroypattern
import fabric
from fabric import *


tframe=[]
tframeColor=[]
facearray=[]
iindex=[]
s = socket.socket()
port = 12345
#s.bind(('', port))
#s.listen(5)
def videoProcessing(frameColor,net,confidence1):
	facearray2=[]

	conf=0
	numface=0
	test="no face found!"
	global tframe
	global tframeColor
	found=0

	#frameColor=cv2.imread("test5.jpg")
	frame = imutils.resize(frameColor, width=400)
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0)) #pass color image
	net.setInput(blob)
	detections = net.forward()
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e.q, probability) associated with the
		# prediction
		confidence = detections[0, 0, i, 2]
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence < confidence1:
			continue
		# compute the (x, y)-coordinates of the bounding box for the
		# object
		found=1 #passing to pattern generator, a face is found
		lucitrajectroypattern.passi(found)
		#print(i)
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")

		height=startY-endY
		heightabs=abs(height)
		facearray2.append(heightabs)
		iindex.append(i)
		facelarge=facearray2.index(max(facearray2))
		larface=iindex[facelarge]
		box = detections[0, 0, larface, 3:7] * np.array([w, h, w, h])
		(startX1, startY1, endX1, endY1) = box.astype("int")
		conf = detections[0,0,larface,2]
		xmid=(endX-startX)/2
		ymid=(endY-startY)/2
		lenx=endX-startX
		leny=endY-startY
		xaxis=xmid+startX
		yaxis=ymid+startY
		x1=str(xaxis)
		y1=str(yaxis)
		axis=x1+" "+y1

		#servo coordinates to lucitrajectory	
		#lucitrajectroy.servoDecision5(xaxis)
		#lucitrajectroy.servoDecision4(lenx)
		#lucitrajectroy.servoDecision3(yaxis)
		#lucitrajectroy.servoDecision2(yaxis)
		#lucitrajectroy.servoDecision1(xaxis)
	try:
		numface=len(facearray2)
		text = "{:.2f}%".format(conf * 100)
		cv2.rectangle(frame, (startX1, startY1), (endX1, endY1),
			(0, 0, 255), 2)
		cv2.putText(frame, text, (startX1, startY1),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

		cv2.putText(frame, ("hey, I found "+str(numface))+" face!", (220, 15),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
	except:
		cv2.putText(frame, "hey, i can't see you !", (220, 15),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)


	if found==0:
		lucitrajectroypattern.passi(found)

	# show the output frame
	cv2.imshow("Frame", frame)

def socket(axis):
        c, addr = s.accept()
        print 'Got connection from', addr
        c.send(axis)
        #c.close() 

def videoCapture(cap):
	confidence1=0.7
	prototxt="deploy.prototxt.txt"
	model="res10_300x300_ssd_iter_140000.caffemodel"
	print("[INFO]model loaded")
	net = cv2.dnn.readNetFromCaffe(prototxt,model)
	time.sleep(2.0)
	print("[INFO]camera open")
	while (True):
		ret,frame=cap.read()
		#cv2.imshow('frame',frame)
		reFrame=cv2.resize(frame,(320,240))
		#frameGray=cv2.cvtColor(reFrame,cv2.COLOR_BGR2GRAY)
		videoProcessing(reFrame,net,confidence1) #videoProcesing block
		key = cv2.waitKey(1) & 0xFF
	
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break


	#sent servos to initial positions
	cv2.destroyAllWindows()
	#socket('socket closed!')
	setup.servoini()
	#funtion call 



def main():
	
	if __name__=='__main__':
		videoCapture(cap)

if __name__=='__main__' or __name__=='lucisight':

	num=input("\n[INFO] Device ID ?\n")	#camera number
	print(__name__)
	cap=cv2.VideoCapture(num)	#camera variable
	main()