import cv2 as cv
import numpy as np
import os

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('lykov.yml')

faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv.FONT_HERSHEY_PLAIN

id = 0
names = ['unknown','Dima', 'Ilon Musk']

path = "pics\\people"
imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
for p in imagePaths:
    img = cv.imread(p)
    img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
    camW = img.shape[0]
    camH = img.shape[1]
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=3,
        minSize=(int(camW) // 10, int(camH) // 10)
    )
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
        id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        if (conf < 100):
            id = names[id]
            conf = "{0}%".format(round(100 - conf))
        else:
            id = names[0]
            conf = "{0}%".format(round(100 - conf))
        cv.putText(img, str(id), (x, y), font, 1, (0, 255, 0), 2)
        cv.putText(img, str(conf), (x, y + h), font, 1, (0, 255, 0), 1)

    cv.imshow('cam', img)
    key = cv.waitKey(0)
    cv.destroyWindow('cam')