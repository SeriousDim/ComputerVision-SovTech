import cv2 as cv
import numpy as np
import os

recognizer = cv.face.LBPHFaceRecognizer_create()
path = "pics\\me"

# NEED LEARNING ALSO FOR UNKNOWN PEOPLE
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []
    for p in imagePaths:
        img = cv.imread(p)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces.append(img)
        id = os.path.split(p)[-1].split('.') # (user, id, num, jpg)
        # print(id)
        ids.append(int(id[1])) # 1 - Dima
    return faces, ids

faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
recognizer.write('lykov.yml')
