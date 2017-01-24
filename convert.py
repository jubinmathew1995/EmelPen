
# Image Converter

import cv2
import numpy as np
#from matplotlib import pyplot as plt
imagePath="charsa3.jpg"
img = cv2.imread(imagePath)
temp_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
equ = cv2.equalizeHist(temp_img)
gray = cv2.bilateralFilter(temp_img, 11, 30, 30)

thresh=128
im_bw = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]

# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(equ)
#gray = cv2.bilateralFilter(temp_img, 11, 30, 30)
cl2=cv2.Canny(gray, 10, 50)
kernel = np.ones((9,9),np.uint8)
dilation = cv2.dilate(cl2,kernel,iterations = 3)
cv2.imwrite( "cl2.jpg", dilation)

im2, contours, hierarchy = cv2.findContours(dilation.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=sorted(contours, key = cv2.contourArea, reverse = True)[:70]
# print(contours)

for i in range(0, len(cnts)):
	cnt = cnts[i]
	x,y,w,h = cv2.boundingRect(cnt)
	im=im_bw[y:y+h,x:x+w]
	border=im;
	m=max(w,h)
	if(w==m):
	 	border=cv2.copyMakeBorder(im, top=int((w-h)/2), bottom=int((w-h)/2), left=0, right=0, borderType= cv2.BORDER_CONSTANT, value=[255,255,255] )
	else:
		border=cv2.copyMakeBorder(im, top=0, bottom=0, left=int((h-w)/2), right=int((h-w)/2), borderType= cv2.BORDER_CONSTANT, value=[255,255,255] )

	border=cv2.resize(border, (128,128), interpolation = cv2.INTER_AREA)
	cv2.imwrite( "bw"+str(i)+".jpg",border)
