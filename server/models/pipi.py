from models.GPIO import GPIO_initialize
from models.light import LightSensor
from models.led import Led
from threading import Thread
import time

GPIO_initialize()
redLed = Led(24)
blueLed = Led(18)
Led.initialize()
lightSensor = LightSensor(27)

class Pipi: 

    def Occupipi(self) : 
        self.status = ""
        while self.running :
            
            if lightSensor.read_light() > 100 :
                print(str(lightSensor.read_light()))
                blueLed.off()
                redLed.on()
                time.sleep(1)
                self.status = "Libres"

            elif lightSensor.read_light() < 101 :
                print(str(lightSensor.read_light()))
                redLed.off()
                blueLed.on()
                time.sleep(1)
                self.status = "Occupées"

    def startDetection(self):
        self.running = True
        thread = Thread(target=self.Occupipi)
        thread.start()
        return thread

    def stopDetection(self):
        self.running = False
  


