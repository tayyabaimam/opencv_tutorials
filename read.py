import cv2 as cv

#reads image from path and returns a matrix of pixels
img = cv.imread('Photos/1.jpeg')

#displays image
cv.imshow('Cat', img)

#waits for some time for a key to be pressed
cv.waitKey(0)

#reading videos
capture= cv.VideoCapture('test1.MP4')

#reading the video frame by frame
while True:
    #returns frame and bool of whether it was successfully read or not
    isTrue, frame= capture.read()
    cv.imshow('Video',frame)
    #if letter d is pressed break
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#release capture device
capture.release()
#closes window
cv.destroyAllWindows()