import cv2 as cv

b = cv.imread("pics\\emir\\b.jpg", cv.IMREAD_GRAYSCALE)
g = cv.imread("pics\\emir\\g.jpg", cv.IMREAD_GRAYSCALE)
r = cv.imread("pics\\emir\\r.jpg", cv.IMREAD_GRAYSCALE)

pic = cv.merge((b, g, r))
cv.imshow("emir", pic)
cv.waitKey(0)
cv.destroyAllWindows()
