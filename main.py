#buttonInput.py
import RPi.GPIO as GPIO
from time import sleep
from picamera.array import PiRGBArray
from picamera import PiCamera

camera = PiCamera()
GPIO.setmode(GPIO.BCM)

sleepTime = .1

#GPIO Pin of the component
lightPin = 4
buttonPin = 17

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        #GPIO.output(lightPin, not GPIO.input(buttonPin))
        #sleep(.1)
        
        if (not GPIO.input(buttonPin)):
            camera.capture('/home/pi/slave_image.jpg')
            print('input from master on gpio 23, Picture taken!') 
            GPIO.output(lightPin, True)
            
        
        else:
            GPIO.output(lightPin, False)
finally:
    GPIO.output(lightPin, False)
    GPIO.cleanup()

