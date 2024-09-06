import cv2 as cv
#masking allows us to focus on certain parts of the image
import numpy as np
img = cv.imread('Photos/1.jpeg')

blank = np.zeros(img.shape[:2], dtype='uint8')

cv.imshow('Cat', img)

mask=cv.circle(blank, (img.shape[1]//2 , img.shape[0]//2), 100, 255, -1)

masked_img = cv.bitwise_and(img,img,mask=mask)
cv.waitKey(0)