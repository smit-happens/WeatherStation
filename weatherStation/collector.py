#!/usr/bin/env python3.4

import time, sys, json
from pubnub import Pubnub
import tempHumidity

print ('Testing importing tempHumidity')


tempVal, HumidVal =
tempHumidity.read(17)

'''
pubnub = Pubnub(publish_key="pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b",
                subscribe_key="sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe")

channelW = "weather"
channelC = "command"


data = {
    'humidity': Humidity,
    'temperature': Temperature
}

pubnub.publish(channel = channelW,
               message = data)
'''

