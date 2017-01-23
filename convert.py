
# Image Converter

import cv2
import numpy as np
#from matplotlib import pyplot as plt
imagePath="char.jpg"
img = cv2.imread(imagePath)
temp_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# equ = cv2.equalizeHist(temp_img)
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(equ)
gray = cv2.bilateralFilter(temp_img, 11, 30, 30)
cl2=cv2.Canny(gray, 10, 50)
kernel = np.ones((8,8),np.uint8)
dilation = cv2.dilate(cl2,kernel,iterations = 1)
cv2.imwrite( "cl2.jpg", dilation)

im2, contours, hierarchy = cv2.findContours(dilation.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=sorted(contours, key = cv2.contourArea, reverse = True)[:70]
print(contours)

for i in range(0, len(cnts)):
	cnt = cnts[i]
	x,y,w,h = cv2.boundingRect(cnt)
	m=max(w,h)
	# if(w==m):
	# 	y-=int((w-h)/2)
	# 	h+=(w-h)
	# else:
	# 	x-=int((h-w)/2)
	# 	w+=(h-w)
	cv2.imwrite( "bw"+str(i)+".jpg", dilation[y:y+h,x:x+w])
