import cv2
import time 

camera=cv2.VideoCapture(-1)
camera.set(3,320)
camera.set(4,240)

while(1):
	ret, frame=camera.read()
	qrDecoder = cv2.QRCodeDetector()
	data,bbox,recti = qrDecoder.detectAndDecode(frame)
	ll=""
	if recti is not None:
		try:
			with open('qrcode1.txt','r') as f:
				ll=f.readlines()[-1]
		except:
			print("no file")
		if data in ll:
			print("same data")
		else:
			print("save data")
			f=open('Deliverylocation.txt','a')
			f.write(data+ ' \r\n')
			f.close()
			time.sleep(3)
	if cv2.waitKey(1) == ord('q'):
		break
cv2.destroyAllWindows()
