import cv2 as cv
import numpy as np
#contours are boundaries of objects, lines that joints points

img = cv.imread('Photos/1.jpeg')

cv.imshow('Cat', img)

blank = np.zeros(img.shape,dtype='uint8')

#first convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#method 1 
# #blur it
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# #grab edges
# canny= cv.Canny(img, 125, 175)
# cv.imshow('Cat', canny)

#method 2
#threshold binarizes the image
#if value is less than 125 it is set to 0 or black and if it above it is set to 1 or white
ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)

#contours is a list of all coords of contours and heirarchies are heirarchal rep of contours
#retr_tree for heirachal contours, retr_external for external contours, retr_list for all contours
contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')

#drawing contours on blank image
#since we want all contours we set it to -1
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Cat', blank)

cv.waitKey(0)
