#버튼으로 제어해서 한번씩 찍어서 실행
import cv2
from gpiozero import Button

bu=Button(18)
camera=cv2.VideoCapture(0)
camera.set(3,320)
camera.set(4,240)

def ca():
	ret, frame=camera.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	cv2.imshow('frame',frame)

	lower_Red=(150,50,60)
	upwer_Red=(180,255,255)

	lower_Green=(36,50,70)
	upwer_Green=(89,255,255)

	lower_Blue=(90,50,70)
	upwer_Blue=(128,255,255)

	lower_Yellow=(25,50,70)
	upwer_Yellow=(35,255,255)

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
	print(maxValue, maxPos)

	if maxValue >= 500:
		if maxPos == 0:
			print("redled on");
		elif maxPos == 1:
			print("greenled on");
		elif maxPos == 2:
			print("blueled on");
	if cv2.waitKey(1)&0xFF == ord('q'):
		#GPIO.cleanup()
		exit()
	
	
while(1):
    bu.when_pressed = ca
    cv2.destroyAllWindows()
    #GPIO.cleanup()
