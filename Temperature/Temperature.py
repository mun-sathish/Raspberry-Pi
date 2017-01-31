# Import all the libraries we need to run
import sys
import RPi.GPIO as GPIO
import os
from time import sleep
import Adafruit_DHT
#import urllib2



DEBUG = 1
# Setup the pins we are connect to
DHTpin = 4


GPIO.setmode(GPIO.BCM)

def getSensorData():
    Humidity, Temp_C = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
    
    #Convert from Celius to Farenheit
    Temp_F = 9/5*Temp_C+32
   
    # return values
    return (str(Humidity), str(Temp_C),str(Temp_F))

    
print 'starting...'
while 1:
	hum, cel, far = getSensorData()
	print ("Humidity = " + hum + "%, Celsius = " + cel + ", Farhenhiet = " + far)  
	sleep(1)
