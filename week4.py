# SID : 500481905
# STUDENT : ETHAN SUSANTO

import cv2
import numpy

# First get the image
image = cv2.imread('Photos\snooooop.jpg')

# Show original image
cv2.imshow('Original', image)

# Rescale to be half the original size
height = image.shape[0]
width = image.shape[1]
print(height, width)

image2 = cv2.resize(image,(int(width/2), int(height/2)),interpolation =cv2.INTER_AREA)

# Show resized image
cv2.imshow('Resized', image2)

# Draw a shape on the original image (circle in the centre)
# Get new dimensions
height = image2.shape[0]
width = image2.shape[1]
cv2.circle(image2, (int(width/2),int(height/2)), 100, (00, 255, 255), thickness = 2 )
cv2.imshow('Circle', image2) # Show circled image

# Greyscale, Blur then Canny
#convert to greyscale  # we will learn more about this lata
image2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey',image2)

#blur
image2=cv2.GaussianBlur(image2,(9,9),cv2.BORDER_DEFAULT)
cv2.imshow('Blur',image2)

#canny
#determines edges using built-in algorithm
image2=cv2.Canny(image2,125,200)
cv2.imshow('Canny',image2)

# Rotate image 45 degrees
def rotate(img, angle, height, width):
    rotatePoint = (int(width/2), int(height/2))
    rotMat = cv2.getRotationMatrix2D(rotatePoint,angle,scale=1.0)
    dimensions =(width,height)

    return cv2.warpAffine(img,rotMat,dimensions)

image2 = rotate(image2, 45, height, width)
cv2.imshow('rotated', image2)

cv2.waitKey(0)