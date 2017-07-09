import I2C_LCD_driver
import urllib2
import RPi.GPIO as GPIO
from time import *
import os
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_UP)
mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_clear()
mylcd.lcd_display_string("Welcome to ",1)
mylcd.lcd_display_string("your doorbell",2)
sleep(1)

def internet_on():
    try:
        response=urllib2.urlopen('http://www.google.com',timeout=10)
        return True
    except urllib2.URLError as err: pass
    return False
        

if internet_on()==True:
    print("Internet is set\nup :)")
else:
    print("No internet use\nDoorbell wifi")

while True:
    inputValue = GPIO.input(27)
    if(inputValue == False):
        print "Button press at", strftime("%d-%m-%Y %H:%M:%S")
        mylcd.lcd_display_string("Ding Dong at\n", 1)
        mylcd.lcd_display_string(strftime("%d-%m-%Y %H:%M:%S"), 2)
        os.system("sudo python tweet.py ")
        sleep(0.2)
    #else:
        #mylcd.lcd_clear()
