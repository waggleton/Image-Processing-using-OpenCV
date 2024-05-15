import cv2 as cv
import numpy as np


#Original Image
img = cv.imread('deadline-meme.jpg')

cv.imshow('meme', img)



# Blurred
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)

cv.imshow('blurred-meme', blur)

#Image transformation

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img,0,100)
cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -90)
cv.imshow('Rotated', rotated)


#Color Space
#Grayscale
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', grayimg)

#HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

cv.waitKey(0)

