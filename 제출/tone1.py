#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
gpio_pin = 12
scale=[523,587,659,699,784,880,988,1047]
GPIO.setmode(gpio_pin,GPIO.OUT)

try:
    p=GPIO.PWM(gpio_pin,100)
    p.start(100)
    p.ChangeDutyCycle(90)

    for i in range(8):
        print(i+1)
        print(scale[i])
        p.ChangeFrequency(scale[i])
        time.sleep(2)
    p.stop()


finally:
    GPIO.cleanup()
