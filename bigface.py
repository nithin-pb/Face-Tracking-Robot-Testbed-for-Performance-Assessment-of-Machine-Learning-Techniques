'''
		#width
		width=startX-endX
		widthabs=abs(width)

		#height
		height=startY-endY
		heightabs=abs(height)
		facearray2.append(heightabs)	
		facearray.append([heightabs,i])
		#print(facearray)
		facelarge=facearray2.index(max(facearray2))
		#print(facelarge)
		box = detections[0, 0, facelarge, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")

		#print("face"+str(i)+"    "+str(heightabs)+"  "+str(widthabs)+"  " +str(confidence*100))
		

		# draw the bounding box of the face along with the associated
		# probability
		text = "{:.2f}%".format(confidence * 100)
		y = startY - 10 if startY - 10 > 10 else startY + 10
		#print(i)
		#face recognition

		frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		roi=frameGray[startX:endX, startY:endY]
		#print(roi)
		try:
			id_, conf=recognizer.predict(roi)
			if conf>=45 and conf<=80:
				print(id_)
				print(labels[id_])
				font=cv2.FONT_HERSHEY_SIMPLEX
				name=labels[id_]
				cv2.putText(frame,name+" "+str(conf),(startX+20,startY+20),font, .5,(266,150,12),1,cv2.LINE_AA)

		except:
			print("[INFO]can't run recognition size is zero")'''

