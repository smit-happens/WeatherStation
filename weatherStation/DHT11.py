#!/usr/bin/env python3.4

import RPi.GPIO as GPIO
import time, sys, json
from pubnub import Pubnub

def bin2dec(string_num): # define a function to convert a binary number to a decimal.
    if string_num == '':
        decVal = 999
    else :
        decVal = int(string_num, 2) # return the int representing the 
    return decVal          #value of the string passed to this function in base 2 (binary)

pubnub = Pubnub(publish_key="pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b",
                subscribe_key="sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe")

channelW = "weather"
channelC = "command"

GPIO.setmode(GPIO.BCM) # use Broadcom numbers instead of the WiringPi numbers
GPIO.setwarnings(False)


while True :
    data = []       # define a data array
    
    GPIO.setup(17,GPIO.OUT)  # Set it as an output to:
    GPIO.output(17,GPIO.HIGH) # write a 1
    time.sleep(0.025)       # for 25 ms
    GPIO.output(17,GPIO.LOW) # then write a 0
    time.sleep(0.02)        # for 20 ms.
    #the preceding sequence is the method to get the DHT sensor 
    #to respond with the current data.

    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Change the pin to read 
                                                    #mode, with a pullup resistor

    for i in range(0,500):      # 501 times
        data.append(GPIO.input(17))  # read a bit from the GPIO, as fast as 
                                    #possible (no wait)

    bit_count = 0
    tmp = 0
    count = 0
    HumidityBit = ""
    TemperatureBit = ""
    crc = ""

    try: # do this unless there's an error. If there's an error jump to "Except:"
       while data[count] == 1: # as long a 1 is read
          tmp = 1
          count = count + 1 # count how many 1s have been read

       for i in range(0, 32): #do this 33 times
          bit_count = 0       #reset the bit count each time

          while data[count] == 0: # as long as a 0 is read
             tmp = 1
             count = count + 1 # move on to the next bit

          while data[count] == 1:    # as long as a 1 is read
             bit_count = bit_count + 1 # count how many 1s in a row
             count = count + 1      # move on to the next bit

          if bit_count > 3:         # if there were mote than 3 * 1-bits in a row
             if i>=0 and i<8:       # if we're in the first byte
                HumidityBit = HumidityBit + "1" # append a 1 to the humidity bitstring
             if i>=16 and i<24:                 # if we're in the 3rd byte
                TemperatureBit = TemperatureBit + "1" # add a 1 to the temperature bitstring
          else:                             # if there weren't at least 3 * 1-bits
             if i>=0 and i<8:               # if we're in the first byte
                HumidityBit = HumidityBit + "0" # append a 0 to the humidity bitstring
             if i>=16 and i<24:                 # if we're in the 3rd byte
                TemperatureBit = TemperatureBit + "0"   #append a 0 to the 
                                                        #temperature bitstring

    except: # if there was an error in the "try:" block
       print ("Measurement_RANGE") # report it

    try: # do this unless there's an error. If there's an error jump to "Except:"
       for i in range(0, 8): # do this 9 times
          bit_count = 0 # reset the bit counter

          while data[count] == 0: # as long as a 0 was read
             tmp = 1
             count = count + 1 # move on to the next bit

          while data[count] == 1:       # as long as a 1 was read
             bit_count = bit_count + 1  # count how many 1s
             count = count + 1          # move on to the next bit

          if bit_count > 3: # if there were at least 3 * 1-bits
             crc = crc + "1" # add a 1 to the crc (Cyclic redundancy check) bitstring
          else:                  # if there were less than 3* 1-bits
             crc = crc + "0" # add a 0 to the crc bitstring
    except:                 # if the "try:" block failed
       print ("CRC_RANGE") # report it

    Humidity = int(bin2dec(HumidityBit)) # convert the binary bitstring to a decimal 
                                    #variable for humidity
    Temperature = int(bin2dec(TemperatureBit))   #convert the binary bitstring to a 
                                            #decimal variable for temperature
    errorVal = Humidity + Temperature - bin2dec(crc)

    if errorVal != 0 : # test whether the CRC indicates that the reading was good
        print ("CRC: ", str(errorVal), str(crc)) # report crc error
    elif Humidity != 999 & Temperature != 999:
        print (str(Humidity), '\t', str(crc))
        print (str(Temperature))

        data = {
            'humidity': Humidity,
            'temperature': Temperature
        }

        pubnub.publish(channel = channelW,
                       message = data)
       
    else:
        print ('Null error')
       
    time.sleep(.25)
