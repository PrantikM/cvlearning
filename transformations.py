import cv2 as cv
import numpy as np 

img = cv.imread("D:\github\cvlearning\cat.jpg")

def translate(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img,100,100)
#cv.imshow("translated", translated)

def rotate(img,angle,rotpoint=None):
    (height,width) = img.shape[:2]

    rotpoint = (width//2 , height//2)

    dimensions = (width, height)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,180)

cv.imshow("rotated", rotated)

cv.waitKey(0)