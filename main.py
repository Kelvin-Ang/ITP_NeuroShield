import sys
import ctypes
import NeuroMem as nm
import GVcomm_SPI as comm
import cv2 as cv
import function as func
import RPi.GPIO as GPIO
import time
#from PIL import ImageEnhance
import picamera


GPIO.setmode(GPIO.BOARD)
#GPIO Pin of the component
toggleLight = 18
light1 = 22
light2 = 32
light3 = 36
light4 = 37

toggleBtn = 7
button1 = 11
button2 = 13
button3 = 15
button4 = 16

# button light setup

GPIO.setup(toggleLight, GPIO.OUT)
GPIO.setup(toggleBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(light1, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(light2, GPIO.OUT)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(light3, GPIO.OUT)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(light4, GPIO.OUT)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#-------------------------------------------------------
# Select a NeuroMem platform
# 0=simu, 1=NeuroStack, 2=NeuroShield, 4=Brilliant
#-------------------------------------------------------
if (comm.Connect() != 0):
	print ("KNS! Check your NeuroShield connection la BODOH!!!\n")
	sys.exit()
else:
	print ("Win liao loh! NeuroShield connected, need do work liao...")
	
nm.ClearNeurons()

#func.learn()

try:
	func.compare()

	while True:
		if (not GPIO.input(toggleBtn)):
			GPIO.output(toggleLight, True)
			func.cam()
			#func.test2()
			time.sleep(1)
		GPIO.output(toggleLight, False)
		if (not GPIO.input(button1)):
			GPIO.output(light1, True)			
			func.cat1()
		
			#func.adjust_brightness('111.jpg', '222.jpg', 1.7)
			#func.extractObject('222.jpg')
			#for i in range(7):
			func.learn1()
				
			#print("CAT 1 LIAO")
		GPIO.output(light1, False)
		if (not GPIO.input(button2)):
			GPIO.output(light2, True)
			func.cat2()
			#for i in range(7):
			func.learn2()
			#print("CAT 2 LIAO!")
		GPIO.output(light2, False)
		if (not GPIO.input(button3)):
			GPIO.output(light3, True)
			func.cat3()
			#for i in range(7):
			func.learn3()
			#print("CAT 2 LIAO!")
		GPIO.output(light3, False)
		if (not GPIO.input(button4)):
			GPIO.output(light4, True)
			func.cat4()
			#for i in range(7):
			func.learn4()
			#print("CAT 2 LIAO!")
		GPIO.output(light4, False)
		
		

		
finally:
	
	GPIO.output(toggleLight, False)
	GPIO.output(light1, False)
	GPIO.output(light2 , False)
	GPIO.output(light3 , False)
	GPIO.output(light4 , False)
	GPIO.cleanup()


