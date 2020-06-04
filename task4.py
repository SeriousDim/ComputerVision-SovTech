import cv2 as cv
import numpy as np

low_H = 22
high_H = 50

low_S = 49
high_S = 164

low_V = 123
high_V = 255

cam = cv.VideoCapture(0)

while 1:
    r, f = cam.read()
    hsv = cv.cvtColor(f, cv.COLOR_BGR2HSV)
    threshold = cv.inRange(hsv, (low_H, low_S, low_V), (high_H, high_S, high_V))
    con, hie = cv.findContours(threshold.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in con:
        x, y, w, h = cv.boundingRect(cnt)
        area = int(w*h)
        if area > 2000 and (abs(w-h) <= 20):
            f = cv.rectangle(f, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.imshow('out', f)
    cv.imshow('thres', threshold)

    key = cv.waitKey(10)
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()