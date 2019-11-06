import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, numGPIO):
        self.numGPIO = numGPIO
        GPIO.setup(numGPIO, GPIO.OUT)

    def on(self):
        print('Led {} on'.format(self.numGPIO))
        GPIO.output(self.numGPIO, GPIO.HIGH)

    def off(self):
        print('Led {} off'.format(self.numGPIO))
        GPIO.output(self.numGPIO, GPIO.LOW)

    @classmethod
    def initialize(cls):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    @classmethod
    def clean(cls):
        GPIO.cleanup()
