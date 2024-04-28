import cv2
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
MOTER_B_A1=20
MOTER_B_B1=21
GPIO.setup(MOTER_B_A1,GPIO.OUT)
GPIO.setup(MOTER_B_B1,GPIO.OUT)
#DC모터 1개당 두개씩 사용해야함 
MOTER_B_A1_PWM=(MOTER_B_A1,20)
MOTER_B_A1_PWM.start(0)
GPIO.output(MOTER_B_B1,GPIO.LOW)

camera=cv2.VideoCapture(0)
camera.set(3,320)
camera.set(4,240)
print("durl")
def MAINomnidirectional()#전방향
    MOTER_B_A1_PWM.ChangeDutyCycle(60)
    time.sleep(4)
    MOTER_B_A1_PWM.ChangeDutyCycle(0)
def MAINReverse #역방향
    MOTER_B_A1_PWM.ChangeDutyCycle(60)
    time.sleep(4)
    MOTER_B_A1_PWM.ChangeDutyCycle(0)

def SUBomnidirectional()#전방향 
    MOTER_B_A1_PWM.ChangeDutyCycle(60)
    time.sleep(1.5)
    MOTER_B_A1_PWM.ChangeDutyCycle(0)

def SUBReverse #역방향
    MOTER_B_A1_PWM.ChangeDutyCycle(60)
    time.sleep(1.5)
    MOTER_B_A1_PWM.ChangeDutyCycle(0)


while(1):
  ret, frame=camera.read()
  hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  cv2.imshow('frame',frame)
  
  lower_Red=(150,50,50)
  upwer_Red=(180,255,255)
  
  lower_Green=(50,150,50)
  upwer_Green=(80,255,255)
  
  lower_Blue=(100,100,120)
  upwer_Blue=(150,255,255)
  
  lower_Yellow=(19,77,0)
  upwer_Yellow=(45,255,255)

  redMask=cv2.inRange(hsv,lower_Red,upwer_Red)
  greenMask=cv2.inRange(hsv,lower_Green,upwer_Green)
  blueMask=cv2.inRange(hsv,lower_Blue,upwer_Blue)
  yellowMask=cv2.inRange(hsv,lower_Yellow,upwer_Yellow)
  
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
      print("red on");
      
    elif maxPos == 1:
      print("green on");
      
    elif maxPos == 2:
      print("blue on");
      
    elif maxPos == 3:
      print("yellow on");
    
  else:
    MOTER_B_A1_PWM.ChangeDutyCycle(0)
    
  if cv2.waitKey(1)&0xFF == ord('q'):
    break
cv2.destroyAllWindows()
MOTER_B_A1_PWM.stop()
GPIO.cleanup()
