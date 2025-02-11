import cv2 as cv

#img = cv.imread(r"C:\Users\DELL\Desktop\photos\cat_large.jpg")

#cv.imshow("cat", img)

capture = cv.VideoCapture(r"C:\Users\DELL\Desktop\photos\dog.mp4")

while True:
    isTrue, frame = capture.read()

    cv.imshow("video", frame)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()