import cv2
import numpy

#reading images
# img = cv2.imread('../Photos/cat.jpg')
# cv2.imshow('Cat', img)

# print(cv2.__file__)


# reading videos

# capture = cv2.VideoCapture('../Videos/dog.mp4')
# VideoCapture(0) = Webcam input

#capture=cv2.VideoCapture(0)
capture = cv2.VideoCapture('../Videos/kitten.mp4')

while True:
    isTrue,frame=capture.read()
    #show frame
    cv2.imshow('',frame)

    #if the d key is pressed, kill screen
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()


cv2.waitKey(1)
