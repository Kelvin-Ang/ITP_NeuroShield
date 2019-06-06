import sys
# import fake_rpi
from fake_picamera import PiCamera

# sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi (GPIO)
# sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)

# sys.modules['picamera'] = fake_picamera


# import RPi.GPIO as GPIO
# import FakeRPi.GPIO as GPIO
import GPIO as GPIO
from time import sleep
# from picamera.array import PiRGBArray
# from picamera import PiCamera

# GPIO.setmode(GPIO.BCM)

# sleepTime = .1

# #GPIO Pin of the component
# lightPin = 4
# buttonPin = 17

# GPIO.setup(lightPin, GPIO.OUT)
# GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# i=0

# try:
#     # while True:
#     while i < 10:
#         GPIO.output(lightPin, GPIO.input(buttonPin))
#         sleep(.1)
#         i+=1
# finally:
#     GPIO.output(lightPin, False)
#     GPIO.cleanup()





camera = PiCamera()
GPIO.setmode(GPIO.BCM)

sleepTime = .1

#GPIO Pin of the component
lightPin = 4
buttonPin = 17

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

i=0

try:
    # while True:
    while i<10:
        #GPIO.output(lightPin, not GPIO.input(buttonPin))
        #sleep(.1)
        
        if (not GPIO.input(buttonPin)):
            camera.capture('/home/pi/slave_image.jpg')
            print('input from master on gpio 23, Picture taken!') 
            GPIO.output(lightPin, True)
            
        
        else:
            GPIO.output(lightPin, False)

        i+=1

finally:
    GPIO.output(lightPin, False)
    GPIO.cleanup()