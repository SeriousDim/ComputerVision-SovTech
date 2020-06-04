import os
import cv2 as cv
import time as t

# creating dataset for learning
cam = cv.VideoCapture(0)
cam.set(3, 960)
cam.set(4, 720)

faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

face_id = input("Enter user id: ")

tm = t.time()
faces = []
count = 0
n = 100
border = 35

while True:
    _, f = cam.read()
    gray = cv.cvtColor(f, cv.COLOR_BGR2GRAY)
    if (t.time() - tm) >= 0.5:
        faces = faceCascade.detectMultiScale(gray,
                                             scaleFactor=1.2,
                                             minNeighbors=5,
                                             minSize=(100,100))
        for (x, y, w, h) in faces:
            if count <= n:
                cv.imwrite("pics\\me\\user."+str(face_id)+"."+str(count)+".jpg", gray[y: y+h, x:x+w])
                count += 1
                if count%50 == 0: print(count)
        tm = t.time()
    for (x, y, w, h) in faces:
        cv.rectangle(f, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.imshow('cam', f)
    key = cv.waitKey(20)
    if key==27:
        break
    if count > n:
        print("Photos are created")
        break

cam.release()
cv.destroyAllWindows()