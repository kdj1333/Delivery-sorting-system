#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
gpio_pin = 12
scale=[523,587,659,699,784,880,988,1047]
GPIO.setup(gpio_pin,GPIO.OUT)
list=[4,4,5,5,4,4,2,4,4,2,2,1]

try:
    p=GPIO.PWM(gpio_pin,100)
    p.start(100)
    p.ChangeDutyCycle(90)

    for i in range(12):
        print(i+1)
        p.ChangeFrequency(scale[list[i]])
        if i == 6:
            time.sleep(1)
        else:
            time.sleep(0.5)
    p.stop()


finally:
    GPIO.cleanup()
