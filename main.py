#!/usr/bin/env python
from button import *
from neuroshield import *

logger.debug("Start debugging")
neuroShield = NeuroShield()
camera = Camera()

#Button declaration
toggleBtn = Button(7)  
blueBtn = Button(11) 
redBtn = Button(13) 
yellowBtn = Button(15) 
greenBtn = Button(16) 

#LED declaration
whiteLight = LED(18)
blueLight = LED(22)
redLight = LED(32)
yellowLight = LED(36)
greenLight = LED(37)

def recognMode():
	logger.debug("recognMode on!!!")
	camera.captureImage('recog/recog.png')
	logger.debug("image captured")
	dist,cat,nid = neuroShield.recogn_W_crop('recog/recog.png')
	print(dist,cat,nid)
	logger.debug("results here")
	#log = str(dist) + "," +  str(cat) + "," + str(nid)
	#writeToFile(log)
	recognizingLED(cat)
	logger.debug("recognizing LED")
	if(toggleBtn.isTriggered()):
		whiteLight.turnOff()
		return
			
			
def offAllLED():
	whiteLight.turnOff()
	redLight.turnOff()
	blueLight.turnOff()
	yellowLight.turnOff()
	greenLight.turnOff()
	
def onAllLED():
	whiteLight.turnOn()
	redLight.turnOn()
	blueLight.turnOn()
	yellowLight.turnOn()
	greenLight.turnOn()	
	
def recognizingLED(category):
	offAllLED()
	
	if(category == 1):
		print('im here')
		logger.debug("im here")
		redLight.turnOn()
	elif(category == 2):
		blueLight.turnOn()
	elif(category == 3):
		yellowLight.turnOn()
	elif(category == 4):
		greenLight.turnOn()
	
	whiteLight.turnOn()
		
#erase file content on start up		
#open('log.txt', 'w').close()
		
		
def writeToFile(log):
	f = open("log.txt","a")
	f.write(log + "\n")		
	f.close()
	
def readFile():
	#open and read file
	f = open("log.txt","r")
	print(r.read())	
	f.close()
		
	

	
mode = 1	
hold_time = 2


neuroShield.clearData()

while(True):
	if(mode == 1):
		if(redBtn.isTriggered()):
			redLight.turnOn()
			camera.captureImage('image/capture.png')
			neuroShield.train_GS_WC_brightness('image/capture.png',1)
			print("cat 1")
			logger.debug("cat 1")
			#writeToFile("cat 1")
			offAllLED()	
			
		if(blueBtn.isTriggered()):
			blueLight.turnOn()
			camera.captureImage('image/capture.png')
			neuroShield.train_GS_WC_brightness('image/capture.png',2)
			print("cat 2")
			logger.debug("cat 2")
			#writeToFile("cat 2")
			offAllLED()	
			
		if(yellowBtn.isTriggered()):
			yellowLight.turnOn()
			camera.captureImage('image/capture.png')
			neuroShield.train_GS_WC_brightness('image/capture.png',3)
			print("cat 3")
			logger.debug("cat 3")
			#writeToFile("cat 3")
			offAllLED()	
			
		if(greenBtn.isTriggered()):
			greenLight.turnOn()
			camera.captureImage('image/capture.png')
			neuroShield.train_GS_WC_brightness('image/capture.png',4)		
			print("cat 4")
			logger.debug("cat 4")
			#writeToFile("cat 4")
			offAllLED()	
						
		offAllLED()	
		#writeToFile("lights off")
		
	else:
		logger.debug("MODE = " + str(mode))
		recognMode()
		
				
	
	if(toggleBtn.isTriggered()):
		start_time = time.time()
		diff = 0
		logger.debug("Entering while loop...")
		while(toggleBtn.isTriggered()):
			logger.debug("Entered while loop")
			now_time = time.time()
			diff=-start_time + now_time
			print('DIFFFF')
			print(diff)
			if(diff>hold_time):
				onAllLED()
				print('Clearing data...')
				logger.debug("Clearing data...")
				#writeToFile("Clearing data...")
				neuroShield.clearData()
							
		if(mode==0):
			mode = 1			
			whiteLight.turnOff()
			print("Training...")
			logger.debug("Training...")
			#writeToFile("Training...")
		else:		
			mode = 0
			whiteLight.turnOn()
			print("Recognizing...")
			logger.debug("Recognizing...")
			#writeToFile("Recognizing...")
			
			
	
		
		
		
		
