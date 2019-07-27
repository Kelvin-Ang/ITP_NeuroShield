from button import *
from neuroshield import *
from imageProcessing import *
import testing as test


neuroShield = NeuroShield()
ip = ImageProcessor()

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
	ip.captureImage('recog/recog.png')
	dist,cat,nid = neuroShield.recogn('recog/recog.png')
	print(dist,cat,nid)
	recognizingLED(cat)
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
		redLight.turnOn()
	elif(category == 2):
		blueLight.turnOn()
	elif(category == 3):
		yellowLight.turnOn()
	elif(category == 4):
		greenLight.turnOn()
	
	whiteLight.turnOn()
		
	
	
#test.trainModel_GS_WC()
print('done')
greenLight.turnOn()	
	
mode = 1	
hold_time = 2

while(True):
	if(mode == 1):
		if(redBtn.isTriggered()):
			redLight.turnOn()
			ip.captureImage('image/capture.png')
			neuroShield.train_GS_WC('image/capture.png',1,0)
			print("cat 1")
		
		if(blueBtn.isTriggered()):
			blueLight.turnOn()
			ip.captureImage('image/capture.png')
			neuroShield.train_GS_WC('image/capture.png',2,0)
			print("cat 2")
			
		if(yellowBtn.isTriggered()):
			yellowLight.turnOn()
			ip.captureImage('image/capture.png')
			neuroShield.train_GS_WC('image/capture.png',3,0)
			print("cat 3")
			
		if(greenBtn.isTriggered()):
			greenLight.turnOn()
			ip.captureImage('image/capture.png')
			neuroShield.train_GS_WC('image/capture.png',4,0)		
			print("cat 4")
						
		offAllLED()	
		
	else:
		recognMode()
		
				
	
	if(toggleBtn.isTriggered()):
		start_time = time.time()
		diff = 0
		while(toggleBtn.isTriggered()):
				now_time = time.time()
				diff=-start_time + now_time
				print('DIFFFF')
				print(diff)
				if(diff>hold_time):
					onAllLED()
					print('Clearing data...')
					neuroShield.clearData()
							
		if(mode==0):
			mode = 1			
			whiteLight.turnOff()
			print("Training...")

		else:		
			mode = 0
			whiteLight.turnOn()
			print("Recognizing...")

			
			
	
		
		
		
		
