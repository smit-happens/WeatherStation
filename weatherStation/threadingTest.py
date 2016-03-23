#!/usr/bin/env python3.4

import RPi.GPIO as GPIO
import time, sys, threading, queue
from pubnub import Pubnub

pubnub = Pubnub(publish_key="pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b",
                subscribe_key="sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe")

channelW = "weather"
channelC = "command"


GPIO.setmode(GPIO.BCM)

def callback(message, channel):
    print('[' + channel + ']: ' + str(message))

#sys.stdout.write("\r%i" % RCtime(18))
def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.2)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

################################
def console(q, lock):
    while True:
        input("Press enter")
        with lock:
            cmd = input('> ')

        q.put(cmd)
        if cmd == 'exit':
            break

def weather(lock):
    with lock:
        print('weather Test confirm')

def command(lock):
    with lock:
        print('command Test confirm')

def text(lock):
    with lock:
        print('text entered doesn\'t match any actions')

def main():
    cmdActions = {'weather': weather, 'command': command}
    cmdQueue = queue.Queue()
    threadLock = threading.Lock()

    stack = threading.Thread(target=console, args=(cmdQueue, threadLock))
    stack.start()

    while True:
        cmd = cmdQueue.get()
        if cmd == 'exit':
            break
        action = cmdActions.get(cmd, text)
        action(threadLock)
    
################################
        pubnub.subscribe(
            channelW,
            callback = callback)

        pubnub.subscribe(
            channelC,
            callback = callback)

main()
