import cv2
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
m_1_1 = 17
m_1_2 = 18
m_2_1 = 4
m_2_2 = 14
m_3_1 = 22
m_3_2 = 23

GPIO.setup(m_1_1,GPIO.OUT)
GPIO.setup(m_1_2,GPIO.OUT)
camera=cv2.VideoCapture(0)
ret, frame=camera.read()
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

lower_Red=(150,50,60)
upwer_Red=(180,255,255)
lower_Green=(36,50,70)
upwer_Green=(89,255,255)
lower_Blue=(90,50,70)
upwer_Blue=(128,255,255)
lower_Yellow=(25,40,130)
upwer_Yellow=(40,150,255)

redMask=cv2.inRange(hsv, lower_Red, upwer_Red)
greenMask=cv2.inRange(hsv, lower_Green, upwer_Green)
blueMask=cv2.inRange(hsv, lower_Blue, upwer_Blue)
yellowMask=cv2.inRange(hsv, lower_Yellow, upwer_Yellow)

redPixels=cv2.countNonZero(redMask)
greenPixels=cv2.countNonZero(greenMask)
bluePixels=cv2.countNonZero(blueMask)
yellowPixels=cv2.countNonZero(yellowMask)

colorList=[redPixels, greenPixels, bluePixels, yellowPixels]
maxValue = max(colorList)
maxPos = colorList.index(maxValue)
if maxValue >= 500:
	if maxPos == 0:
		print("red check");
		GPIO.output(m_1_1, True)
		GPIO.output(m_1_2, False)
		sleep(2)
		GPIO.output(m_2_1, True)
		GPIO.output(m_2_2, False)
		sleep(1)
	elif maxPos == 1:
		print("greenled on");
		GPIO.output(m_1_1, True)
		GPIO.output(m_1_2, False)
		sleep(2)
		GPIO.output(m_2_1, False)
		GPIO.output(m_2_2, True)
		sleep(1)
	elif maxPos == 2:
		print("blueled on");
		GPIO.output(m_1_1, False)
		GPIO.output(m_1_2, True)
		sleep(2)
		GPIO.output(m_3_1, False)
		GPIO.output(m_3_1, True)
		sleep(1)
	elif maxPos == 3:
		print("yellow on");
		GPIO.output(m_1_1, False)
		GPIO.output(m_1_2, True)
		sleep(2)
		GPIO.output(m_3_1, True)
		GPIO.output(m_3_1, False)
		sleep(1)
GPIO.cleanup()
cv2.destroyAllWindows()
