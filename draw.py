import cv2 as cv
import numpy as np

img = cv.imread("D:\github\cvlearning\cat.jpg")

blank = np.zeros((500,500,3), dtype="uint8")

#blank[200:300, 300:400]= 0,255,0

cv.rectangle(blank, (0,0), (blank.shape[0]//2,250), (0,0,255) , thickness=cv.FILLED)

cv.circle(blank , (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=-1)

cv.putText(blank, "hello", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)

cv.imshow("blank", blank)
cv.waitKey(0)