#!/usr/bin/env python3.4

import RPi.GPIO as GPIO
import time, sys, json
from pubnub import Pubnub
#import DHT11 as reader         #soon(TM)

pubnub = Pubnub(publish_key="pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b",
                subscribe_key="sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe")

channelW = "weather"
channelC = "command"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

while True:
    lightVal = 0
    
    for i in range (0 , 40):
        lightVal += RCtime(18)
        
    lightVal = .1/((lightVal/40) +1)
    humidity, temperature = read(DHT11, 17)
    
    print('Sending light value of ' + str(lightVal) + ' onto weather channel')
    #print('Temperature should be ' + str(temperature))
    #print('Humidity should be ' + str(humidity))

    data = {
        'light': lightVal
        }
    
    
    pubnub.publish(channel = channelW,
                   message = data)
