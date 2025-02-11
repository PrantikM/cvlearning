import cv2 as cv

img = cv.imread("D:\github\cvlearning\cat.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)

canny = cv.Canny(blur , 125, 175)

dilated = cv.dilate(canny , (7,7), iterations=3)

eroded = cv.erode(dilated , (7,7), iterations=3)

resized = cv.resize(img , (500,500), interpolation=cv.INTER_CUBIC)

cv.imshow("resized", resized)

cropped = img[50:200 , 200:400]

cv.imshow("cropped", cropped)

#cv.imshow("eroded", eroded)

#cv.imshow("dilated", dilated )

# cv.imshow("canny", canny)
#cv.imshow("blur", blur)


#cv.imshow('gray', gray)

cv.waitKey(0)