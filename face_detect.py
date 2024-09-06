import cv2 as cv

img = cv.imread('Photos/people.jpeg')

cv.imshow('Group', img)

#haar cascade does not need color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Group gray', gray)

haar_cascade= cv.CascadeClassifier('haar_face.xml')

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

# print(f'Number of faces found = {len(faces_rect)}')

# #since faces_rect is coords of the rectangle of the face

# for(x,y,w,h) in faces_rect:
#     cv.rectangle(img,(x,y), (x+w,y+h), (0,255,0), thickness=2 )
# cv.imshow('Faces', img)
# cv.waitKey(0)

#detecting faces on a video
#reading videos
capture= cv.VideoCapture('test1.MP4')

#reading the video frame by frame
while True:
    #returns frame and bool of whether it was successfully read or not
    isTrue, frame= capture.read()
    cv.imshow('Video',frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=1)
    for(x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y), (x+w,y+h), (0,255,0), thickness=2 )
    cv.imshow('Faces', frame)
    #if letter d is pressed break
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#release capture device
capture.release()
#closes window
cv.destroyAllWindows()

