import cv2 as cv
#thresholding is a binarization of an image. pixels are either 0(black) or 255(white)
#take an image and a thresholding value and compare each pixel to it. if it is > then set it to 255 if it is < set it to 0
img = cv.imread('Photos/1.jpeg')
cv.imshow('Cat', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#simple thresholding
#returns threshold(threshold value) and thresh(binarized image), params: img, thresholding value, max, type
threshold, thresh = cv.threshold(gray, 150, 255,cv.THRESH_BINARY)
cv.imshow('simple thresh', thresh)

#inversed threshold
threshold, thresh_inv = cv.threshold(gray, 150, 255,cv.THRESH_BINARY_INV)
cv.imshow('inverse thresh', thresh_inv)

#adaptive threshold
#computer finds optimum threshold value
adaptive= cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,3 )
cv.imshow('adaptive thresh', adaptive)

cv.waitKey(0)