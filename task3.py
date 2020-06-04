import cv2 as cv

img = cv.imread("pics\\sea.jpg")
img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

print(img.shape)
cv.imshow("sea", img)
cv.imshow("hsv", img_hsv)

b, g, r = cv.split(img)
h, s, v = cv.split(img_hsv)

# cv.imshow('b',b)
# cv.imshow('g',g)
# cv.imshow('r',r)
# cv.imshow('h',h)
# cv.imshow('s',s)
# cv.imshow('v',v)

for i in range(0, img.shape[1]):
    for j in range(0, img.shape[0]):
        if 65 <= h[j, i] <= 135:
            img[j, i] = (0, 255, 0)
        else:
            img[j, i] = (0, 255, 255)

cv.imshow("edit", img)

cv.waitKey(0)
cv.destroyAllWindows()