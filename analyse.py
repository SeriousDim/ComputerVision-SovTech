import cv2 as cv
import os

path = "pics\\roads"
images = [os.path.join(path, f) for f in os.listdir(path)]
img = cv.imread(images[10])

del_c = int(img.shape[1]/480)
if del_c == 0: del_c = 1
img = cv.resize(img, (img.shape[1]//del_c, img.shape[0]//del_c))

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)

canny = cv.Canny(img, 300, 600)


cv.imshow('img', img)
cv.imshow('h', h)
cv.imshow('s', s)
cv.imshow('v', v)
cv.imshow('gray_thres', gray_thres)
cv.imshow('canny', canny)

cv.waitKey(0)
cv.destroyAllWindows()
