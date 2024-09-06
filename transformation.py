import cv2 as cv
import numpy as np

img = cv.imread('Photos/1.jpeg')
cv.imshow('cropped', img)

#translation ( shifting image up or down)
def translate(img, x, y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
   
#rotation
def rotate(im, angle, rotPoint=None):
    (height,width)= img.shape[:2]

#if rotation point is none rotate it around the center
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat= cv.getRotationMatrix2D(rotPoint,angle, 1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img, 45)

#resizing
resized = cv.resize(img, (50,500),interpolation=cv.INTER_CUBIC)

#flipping
#0 is vertical flip , 1 is horizontal, -1 both vert and hor
flip = cv.flip(img, )

#cropping
cropped = img[200:400, 300:400]

cv.waitKey(0)
