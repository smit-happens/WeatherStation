#!/usr/bin/env python

import RPi.GPIO as GPIO
import time, sys
from pubnub import Pubnub

pubnub = Pubnub(publish_key="pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b",
                subscribe_key="sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe")

channelW = "weather"
channelC = "command"

GPIO.setmode(GPIO.BCM)

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
        
    lightVal = lightVal/40
    
    print('Sending light value of ' + str(lightVal) + ' onto weather channel')
    text = 'Current light level is ' + str(lightVal)
    
    pubnub.publish(channel = channelW, message = text)
