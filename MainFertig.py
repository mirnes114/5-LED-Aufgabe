from machine import Pin
from dht import measure, temperature, humidity
from time import delay

LED_Cold = Pin(33, Pin.OUT)
LED_Hot = Pin(34, Pin.OUT)
LED_Wet = Pin(24, Pin.OUT)
LED_Good = Pin(25, Pin.OUT)
LED_Dry = Pin(26, Pin.OUT)

class LED:
    def __init__(self, pin):
        self.sPin = pin
        self.sVal = 0
        self.LED = Pin(self.sPin, Pin.OUT)
        
    def ifAbove(self, Activ):
        if self.sVal > Activ:
            self.LED.value(1)
        else:
            self.LED.value(0)
               
    def ifBelow(self, Activ1):
        if self.sVal < Activ1:
            self.LED.value(1)
        else:
            self.LED.value(0)
            
    def ifBetween(self, Activ1, Activ2):
        if self.sVal < Activ2 and self.sVal > Activ1:
            self.LED.value(1)
        else:
            self.LED.value(0)
        
def Main():
    while True:
        measure()
        LED_Cold.Val = temperature()
        LED_Hot.Val = DHT11.temperature()
        
        LED_Wet.Val = humidity()
        LED_Good.Val = humdity()
        LED_Dry.Val = humidity()
        
        print(temperature())
        print(humidty))
        
        LED_Cold.ifBelow(20)
        LED_Hot.ifAbove(20)
         
        LED_Dry.ifBelow(25)
        LED_Good.ifBetween(25, 70)
        LED_Wet.ifAbove(70)
        
        time.delay(100)

         
Main() 
        
   
        