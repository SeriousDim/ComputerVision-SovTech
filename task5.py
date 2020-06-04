import cv2 as cv
import time as t
import numpy as np

faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

cam = cv.VideoCapture(0)
cam.set(3, 960)
cam.set(4, 720)

time_var = t.time()
faces = []
eyes = []

border = 30
a = 1.3
b = 40

while 1:
    r, f = cam.read()

    gray = cv.cvtColor(f, cv.COLOR_BGR2GRAY)
    if (t.time() - time_var) >= 0.1 or len(faces) == 0:
        faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.2,
                                         minNeighbors=5,
                                         minSize=(20, 20))
        # eyes = eyeCascade.detectMultiScale(gray,
        #                                    scaleFactor=1.05,
        #                                    minNeighbors=7,
        #                                    minSize=(20, 20))
        time_var = t.time()
    for (x, y, w, h) in faces:
        # cv.putText(f, 'Human', (x, y-5), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv.LINE_AA)
        cv.rectangle(f, (x-border, y-border), (x+w+border, y+h+border), (0, 255, 0), 2)

    # for (x, y, w, h) in eyes:
    #     # cv.putText(f, 'Human', (x, y-5), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv.LINE_AA)
    #     cv.rectangle(f, (x, y), (x+w, y+h), (255, 0, 0), 1)

    cv.imshow('out', f)

    k = cv.waitKey(10) & 0xff
    if k == 27: break

cam.release()
cv.destroyAllWindows()