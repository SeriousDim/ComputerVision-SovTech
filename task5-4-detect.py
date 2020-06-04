import cv2 as cv
import numpy as np
import os

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('lykov.yml')

faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv.FONT_HERSHEY_PLAIN

id = 0
names = ['unknown','Dima', 'Ilon Musk']

cam = cv.VideoCapture(0)
camW = cam.get(3)
camH = cam.get(4)
while 1:
    _, img = cam.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=3,
        minSize=(int(camW)//10, int(camH)//10)
    )
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 1)
        id, conf = recognizer.predict(gray[y:y+h, x:x+w])
        if (conf < 100):
            id = names[id]
            conf = "{0}%".format(round(100 - conf))
        else :
            id = names[0]
            conf = "{0}%".format(round(100 - conf))
        cv.putText(img, str(id), (x,y), font, 1, (255, 255, 255), 2)
        cv.putText(img, str(conf), (x, y+h), font, 1, (255, 255, 255), 1)

    cv.imshow('cam', img)
    key = cv.waitKey(20)
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()