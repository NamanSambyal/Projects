import cv2 as cv
import numpy as np

# cap=cv.VideoCapture(0)
font = cv.FONT_HERSHEY_COMPLEX 
# while True:
img = cv.imread("shapes4.png" , cv.IMREAD_GRAYSCALE)
# _,imgini = cap.read()
# img=cv.cvtColor(imgini,cv.COLOR_BGR2GRAY)
_, threshold = cv.threshold(img,110,255,cv.THRESH_BINARY)

contours,_ = cv.findContours(threshold,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
	print("DONE WITH THIS\n\n\n\n")
	# print(cnt)
	approx = cv.approxPolyDP(cnt,0.09*cv.arcLength(cnt, True),  True)
	# cv.fitEllipse(approx) 
	cv.drawContours(img, [approx] , 0, 1)

	n = approx.ravel()  
	i = 0
  
	for j in n : 
		if(i % 2 == 0): 
		    x = n[i] 
		    y = n[i + 1] 

		    # String containing the co-ordinates. 
		    string = str(x) + " " + str(y)  

		    if(i == 0): 
		        # text on topmost co-ordinate. 
		        cv.putText(img, "Arrow tip", (x, y), 
		                        font, 0.5, (255, 0, 0))  
		    else: 
		        # text on remaining co-ordinates. 
		        cv.putText(img, string, (x, y),  
		                  font, 0.5, (0, 255, 0))
		    print(x,y)  
		i = i + 1


cv.imshow("shapes" , img)
cv.imshow("thresh" , threshold)
cv.waitKey(0)
# key=cv.waitKey(0)
# if key==27:
# 	break;

# cap.release()
cv.destroyAllWindows()