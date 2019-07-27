import sys
import ctypes
import NeuroMem as nm
import GVcomm_SPI as comm
import cv2 as cv
env = 1
if(env == 1):
	import fake_rpi	as GPIO
else:
	# import RPi.GPIO as GPIO
	print("cannot import RPI.GPIO")

import time
# import picamera
from fake_picamera import PiCamera


GPIO.setmode(GPIO.BOARD)

class Button:
	
	def __init__(self,buttonPin):
		GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		self.buttonPin = buttonPin

	def isTriggered(self):
		if (not GPIO.input(self.buttonPin)):
			return True			

			
			
class snake:
	def __init__(self,name):
		self.name = name
		
	def snaken(self):
		return self.name
		
		
		
class LED:
	def __init__(self,lightPin):
		GPIO.setup(lightPin, GPIO.OUT)
		self.lightPin = lightPin
		
	def turnOn(self):
		GPIO.output(self.lightPin, True)
		
	def turnOff(self):
		GPIO.output(self.lightPin, False)
		
	
	
	
#toggleLight = 18
#light1 = 22
#light2 = 32
#light3 = 36
#light4 = 37

#def setupLED(LEDpin):
#	GPIO.setup(LEDpin, GPIO.OUT)
#
#def toggleWhiteLight(isOn,duration):		
#	setupLED(toggleLight)
#	GPIO.output(toggleLight, isOn)
	
#def toggleRedLight(isOn,duration):		
#	setupLED(toggleLight)
#	GPIO.output(toggleLight, isOn)	
	
#def toggleBlueLight(isOn,duration):		
#	setupLED(toggleLight)
#	GPIO.output(toggleLight, isOn)
	
#def toggleYellowLight(isOn,duration):		
#	setupLED(toggleLight)
#	GPIO.output(toggleLight, isOn)
	
	
#def toggleGreenLight(isOn,duration):		
#	setupLED(toggleLight)
#	GPIO.output(toggleLight, isOn)							
	



#GPIO.setup(toggleBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


