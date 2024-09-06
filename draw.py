import cv2 as cv
import numpy as np

#creaating a blank image
blank = np.zeros((500,500,3), dtype='uint8')

img = cv.imread('Photos/1.jpeg')
cv.imshow('Cat', img)

#painting the image a color
#you can specify a range and color
# blank[:]= 0,255,0
# cv.imshow('Green', blank)

#drawing a rectangle
#params: image, origin coord, end coord, color and thickness
cv.rectangle(blank, (0,0), (250,250),(0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

#drawing a circle 
#extra param is radius
cv.circle(blank,(250,250), 40,(0,0,255), thickness=1)
cv.imshow('Circle',blank)

#drwing a line
cv.line(blank, (100,250), (250,250),(255,255,255), thickness=3)
cv.imshow('Line',blank)

#writing text
#image, text, origin, font, fontscale, color
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)
