import cv2 as cv
#histogram allows you to visualize the pixel distribution in an image
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/1.jpeg')
blank = np.zeros(img.shape[:2], dtype='uint8')

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cat', img)

circle=cv.circle(blank, (img.shape[1]//2 , img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray,gray,mask=circle)

# cv.imshow('Mask', mask)

#grayscale histogram
#list of images, no of channels(index of channel we wanna compute ist for), mask, hist size( no of bins), range of all possible pixels
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# plt.figure()
# plt.title("grayscale Histogram")
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#colour histogram
mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow('Mask', mask)
plt.figure()
plt.title("Color Histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i, col in enumerate(colors):
    hist= cv.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)