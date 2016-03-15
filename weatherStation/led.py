#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from pubnub import Pubnub

pubnub = Pubnub(publish_key="pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b",
                subscribe_key="sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe")

channelW = "weather"
channelC = "command"

GPIO.setmode(GPIO.BCM)
led = 18
GPIO.setup(led,GPIO.OUT)

def callback(message, channel):
    print('[' + channel + ']: ' + str(message))

    if(channel == channelC):
        if(message == "on"):
            GPIO.output(led,True)
            pubnub.publish(
                channel = channelW,
                message = "Turning LED on")
            
        if(message == "off"):
            GPIO.output(led,False)
            pubnub.publish(
                channel = channelW,
                message = "Turning LED off")
        

pubnub.subscribe(
    channelW,
    callback = callback)

pubnub.subscribe(
    channelC,
    callback = callback)
