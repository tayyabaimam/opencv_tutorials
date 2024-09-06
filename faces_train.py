import os
import cv2 as cv
import numpy as np

people = ['Ben Affleck', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling'] 

p= []

DIR = 'C:\Users\tayya\OneDrive\Desktop\object_detection\Photos\Faces\train'

haar_cascade= cv.CascadeClassifier('haar_face.xml')
  
#face
features = []
#person
labels=[]

def create_train():
    for person in people:
        #GRABBING PATH OF EACH FOLDER
        path= os.path.join(DIR, person)
        #label = person
        label = people.index(person)

        #looping over eveyr image
        for img in os.listdir(path):
            #extracting path from every image
            img_path = os.path.join(path,img)
            #reading image from path
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x,y,w,h) in faces_rect:
                #grab faces region of interest
                faces_roi = gray[y:y+h, x:x+w]
                #adding face and person
                features.append(faces_roi)
                labels.append(label)



create_train()

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer= cv.face.LBPHFaceRecognizer_create()

#train the recognizer on the features and labels
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy',labels)

