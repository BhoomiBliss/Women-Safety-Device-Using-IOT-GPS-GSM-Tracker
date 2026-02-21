#!/usr/bin/env python
import serial
import time
import urllib.request
ser = serial.Serial(
   port='/dev/ttyUSB0',  #ttyAMA0 ttyS0 ttyUSB0
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)

while True:
    x=ser.readline() # ser.readline to read row
    x = x.decode('UTF-8','ignore')
    if x:
        print(x)
        f = open('location.txt', 'w')
        f.write(x)
        f.close()
        lat, long = x.split(',')
        api_key = "Y7DSN6SAR9YHIO4U"
        URL='https://api.thingspeak.com/update?api_key={}&field5={}&field6={}'.format(api_key,lat, long)
        data=urllib.request.urlopen(URL)
        print(data)
    time.sleep(1)

