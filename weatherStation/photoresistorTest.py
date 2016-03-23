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
    time.sleep(0.2)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

while True:
    sys.stdout.write("\r%i" % RCtime(18))
    sys.stdout.flush()
