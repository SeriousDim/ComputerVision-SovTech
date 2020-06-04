import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

def f(x):
    pass

path = "pics\\roads"
images = [os.path.join(path, f) for f in os.listdir(path)]
img = cv.imread(images[0])
del_c = int(img.shape[1]/700)
if del_c == 0: del_c = 1
img = cv.resize(img, (img.shape[1]//del_c, img.shape[0]//del_c))
img_orig = img.copy()

cv.namedWindow('set')
cv.createTrackbar('block', 'set', 0, 50, f)
cv.setTrackbarPos('block', 'set', 5)
cv.createTrackbar('c', 'set', 0, 100, f)
cv.setTrackbarPos('c', 'set', 15)

while 1:
    v1 = cv.getTrackbarPos('min', 'set')
    v2 = cv.getTrackbarPos('max', 'set')
    img = img_orig.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    block_size = cv.getTrackbarPos('block', 'set')
    block_size = block_size+1 if block_size % 2 == 0 else block_size
    out = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv.THRESH_BINARY,
                               block_size,
                               cv.getTrackbarPos('c', 'set'))

    cv.imshow('orig', img)
    cv.imshow('threshold', out)

    key = cv.waitKey(20)
    if key == 27:
        break

cv.destroyAllWindows()
