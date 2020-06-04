import cv2 as cv

cam = cv.VideoCapture(0)
sea = cv.imread("pics\\sea-cut.jpg")

alpha = 100
a = 0
b = 1.0 - a

def change(x):
    global a
    global b
    a = x/alpha
    b = 1.0 - a

cv.namedWindow("set")
cv.createTrackbar('Alpha', 'set', 0, alpha, change)

while(1):
    r, f = cam.read()
    out = cv.addWeighted(f, a, sea, b, 0)
    cv.imshow('out', out)
    key = cv.waitKey(10)
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()