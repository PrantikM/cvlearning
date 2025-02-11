import cv2 as cv 

img = cv.imread("D:\github\cvlearning\cat_large.jpg")

#live video,img,video
def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

#live video only
def changeres(width, height):
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture("D:\github\cvlearning\dog.mp4")

resized_image = rescaleframe(img, scale=0.2)

cv.imshow("Img", resized_image)

cv.waitKey(0)
