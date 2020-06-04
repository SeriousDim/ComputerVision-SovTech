import os
import cv2 as cv

# creating dataset for learning
faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

path = "pics\\ilon"
face_id = input("Enter user id: ")

faces = []
count = 0
border = 35

imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
for p in imagePaths:
    f = cv.imread(p)
    gray = cv.cvtColor(f, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                             scaleFactor=1.2,
                                             minNeighbors=5,
                                             minSize=(100,100))
    for (x, y, w, h) in faces:
        cv.imwrite("pics\\me\\user."+str(face_id)+"."+str(count)+".jpg", gray[y: y+h, x:x+w])
        count += 1
        if count%5 == 0: print(count)
    for (x, y, w, h) in faces:
        cv.rectangle(f, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.imshow(p, f)

key = cv.waitKey(0)
cv.destroyAllWindows()