import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
m1 = 4
m2 = 14
GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)

try:
	while(1):
		GPIO.output(m1, True)
		GPIO.output(m2, False)
		sleep(1)

except KeyboardInterrupt:
	print("KeyboardInterrupt")
	GPIO.cleanup()
    