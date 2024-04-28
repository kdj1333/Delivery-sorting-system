#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
print("Setup")
GPIO.output(19,True)
sleep(2)

for i in range(1,3):
    GPIO.output(19,False)
    print("LED켜짐 - 릴레이 연결처리됨")
    sleep(2)
    GPIO.output(19,True)
    print("LED꺼짐 - 릴레이 연결안됨")
    sleep(2)
    
GPIO.cleanup()
print("cleanup")
sleep(2)
