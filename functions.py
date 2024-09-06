import cv2 as cv

img = cv.imread('Photos/1.jpeg')

#converting an image to grayscale 
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#blurring an image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

#edge cascade
canny = cv.Canny(img, 125, 175)
 
#dilating the image
#structuring element, kernel size, iterations
dilated= cv.dilate(canny, (3,3), iterations=1)

#eroding 
#sme params and get back same cascading
eroded= cv.erode(dilated, (3,3), iterations=1)

#resize
#source and output size
#default interpolation= interarea for making it smaller and inter_cubic is for enlarging
resized= cv.resize(img, (500,500))

#cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)
