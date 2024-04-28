#-*-coding: utf-8-*-
import PRi,GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
count = 0
try:
   while 1:
           if GPIO.input(4):
                count +=1
                if count == 3:
                    t = time.localtime()
                    print "%d:%d:%d 움직임이 감지 됨" % (t.tm_hour, t.tm_min, t.tm_sec)
                    count = 0    
            else:
                print "------"
            time.sleep(0.2)
                
except KeyboardInterrup:
        GPIO.cleanup()
