import cv2 as cv

#reads image from path and returns a matrix of pixels
img = cv.imread('Photos/1.jpeg')

#displays image
cv.imshow('Cat', img)

def rescaleFrame(frame,scale=0.75):
    #0 is height 1 is width
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    #initializing a tuple of width nd height
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #will only work on live videos
    #3 references width and 4 references height
    capture.set(3,width)
    capture.set(4,height)

capture= cv.VideoCapture('test1.MP4')

while True:
    isTrue, frame= capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
