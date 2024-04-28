#-*-coding: utf-8-*-
import PRi,GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
camera=PiCamera()
count = 0
counter = 1
try:
   while 1:
           if GPIO.input(4):
                count +=1
                if count == 3:
                    t = time.localtime()
                    print "%d:%d:%d 움직임이 감지 됨" % (t.tm_hour, t.tm_min, t.tm_sec)
                    count = 0
                    camera.start_preview()
                    time.sleep(1)
                    camera.start_recoding('/home/pt/Desktop/video%s.h264')
                    #camera.capture('/home/pt/Desktop/image%s.jpg' % counter)
                    counter += 1
                    time.sleep(5)
                    camera.stop_recording()
                    camera.stop_preview()
            else:
                print "------"
            time.sleep(0.2)
                
except KeyboardInterrup:
        GPIO.cleanup()
        camera.stop_preview()
