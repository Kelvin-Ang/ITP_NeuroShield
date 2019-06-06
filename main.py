# import sys
# import fake_rpi

# sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi (GPIO)
# sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)


# import RPi.GPIO as GPIO
import FakeRPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleepTime = .1

#GPIO Pin of the component
lightPin = 4
buttonPin = 17

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        GPIO.output(lightPin, GPIO.input(buttonPin))
        sleep(.1)
finally:
    GPIO.output(lightPin, False)
    GPIO.cleanup()


    # test