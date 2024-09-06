import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/1.jpeg')

cv.imshow('Cat', img)

# #libraries other than opencv use rgb
# plt.imshow(img)
# plt.show()

#bgr to grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#bgr to hsv(how humans interpret color)
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)

#bgr to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

#bgr to rgb
rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)

#hsv to bgr
hsv_bgr= cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
 
cv.waitKey(0)
