from button import *
from neuroshield import *
from imageProcessing import *

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



#toggleBtn = 7
button1 = 11
button2 = 13
button3 = 15
button4 = 16

snake1 = snake("hellosssss")

print(snake1.snaken())



imgtest = ip.captureImage('image/capture.png')
img = cv.imread('image/capture.png')
#cv.imshow('test1',ip.convertGrayScale(img))
#cv.imshow('test2',ip.cropROI('image/capture.png', 'image/capture.png'))
#cv.imshow('test3',ip.edgeDetection('image/capture.png'))
#cv.imshow('test4',ip.cropROI('image/grayscale.png','image/capture.png'))

#img2 = cv.imread('image/capture.png')
#img2 = ip.convertGrayScale(img2)
#p,vector = (ip.convertToVector(img2))
#print(p)

#cv.waitKey(0)


#ip.cropROI('image/capture.png','image/capture.png')

#ip.edgeDetection('image/capture.png')


neuroShield.train('image/capture.png',1)
neuroShield.recogn('image/capture.png')


while(True):
	if(toggleBtn.isTriggered()):
		print("hshhshsh")
		whiteLight.turnOn()
	if(redBtn.isTriggered()):
		print("ererere")
		redLight.turnOn()
	if(blueBtn.isTriggered()):
		print("tytyty")
		blueLight.turnOn()
	if(yellowBtn.isTriggered()):
		print("ioioioio")
		yellowLight.turnOn()
	if(greenBtn.isTriggered()):
		print("popopopo")
		greenLight.turnOn()
		
		


		
		
		
		
		
		
