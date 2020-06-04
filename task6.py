import cv2 as cv
import numpy as np
import os

def f(x):
    pass

# SEARCH OTHER FUNCTIONS: ADAPTIVE THRESHOLDS
path = "pics\\roads"
images = [os.path.join(path, f) for f in os.listdir(path)]
img = cv.imread(images[6])
del_c = int(img.shape[1]/700)
if del_c == 0: del_c = 1
img = cv.resize(img, (img.shape[1]//del_c, img.shape[0]//del_c))
img_orig = img.copy()

cv.namedWindow('set')
cv.createTrackbar('min', 'set', 0, 1500, f)
cv.setTrackbarPos('min', 'set', 300)
cv.createTrackbar('max', 'set', 0, 1500, f)
cv.setTrackbarPos('max', 'set', 560)

lines = [] # (x, width)
lines_2 = []
while 1:
    v1 = cv.getTrackbarPos('min', 'set')
    v2 = cv.getTrackbarPos('max', 'set')
    img = img_orig.copy()
    can = cv.Canny(img, v1, v2)
    lines = []
    lines_2 = []

    #lines
    line_y = 0
    found = 0
    for x in range(can.shape[1]):
        if found: break
        for y in range(can.shape[0]-1, can.shape[1]//2, -1):
            if can[y, x] == 255:
                y -= 40
                cv.line(img, (0, y), (can.shape[1], y), (0, 211, 255))
                line_y = y
                found = 1
                break

    found = 0
    point = [0, 0]
    for x in range(0, can.shape[1]):
        if can[line_y, x] == 255:
            if not found:
                point[0] = x
            else:
                point[1] = x - point[0]
                lines.append(point)
                point = [0, 0]
            found = not found

    #lines_2
    found = 0
    line_y_2 = 0

    for x in range(can.shape[1]):
        if found: break
        for y in range(line_y-1, can.shape[1]//2, -1):
            if can[y, x] == 255:
                y -= 50
                cv.line(img, (0, y), (can.shape[1], y), (0, 211, 255))
                line_y_2 = y
                found = 1
                break

    found = 0
    point = [0, 0]
    for x in range(0, can.shape[1]):
        if can[line_y_2, x] == 255:
            if not found:
                point[0] = x
            else:
                point[1] = x - point[0]
                lines_2.append(point)
                point = [0, 0]
            found = not found

    #print(lines)
    cv.line(img, (lines[0][0], line_y), (lines[-1][0] + lines[-1][1], line_y), (0, 0, 255), 2)
    cv.line(img, (lines_2[0][0], line_y_2), (lines_2[-1][0] + lines_2[-1][1], line_y_2), (0, 0, 255), 2)

    cv.line(img, (((lines[0][0]+lines[-1][0]+lines[-1][1])//2), line_y), (((lines_2[0][0]+lines_2[-1][0]+lines_2[-1][1])//2), line_y_2), (0, 255, 0), 3)

    cv.imshow('orig', img)
    cv.imshow('canny', can)
    key = cv.waitKey(20)
    if key == 27:
        break

cv.destroyAllWindows()
