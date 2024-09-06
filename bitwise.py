import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370),255,-1)

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

#bitwise AND
#returns intersection
bitwise_and= cv.bitwise_and(rectangle,circle)

#bitwise OR
#returns both intersecting and non-intersecting
bitwise_or = cv.bitwise_or(rectangle,circle)

#bitwise XOR
#returns non-intersecting
bitwise_xor= cv.bitwise_xor(rectangle,circle)

#bitwise NOT
#returns the opposite region
bitwise_not = cv.bitwise_not(rectangle)

cv.waitKey(0)