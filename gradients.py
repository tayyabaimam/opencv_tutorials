import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/1.jpeg')

cv.imshow('Cat', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#laplacian 
lap= cv.Laplacian(gray,cv.CV_64F)
lap= np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#sobel - computes gradients in x and y coords
sobelx = cv.Sobel(gray, cv.CV_64F, 1 , 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0 , 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel', combined_sobel)

#canny
canny= cv.Canny(img, 125, 175)
cv.waitKey(0)