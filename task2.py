import cv2 as cv
# mush[:,:,3]

def f(x):
    return x/100

path = "pics\\task2\\"

forest = cv.imread(path+"forest.jpg", cv.IMREAD_UNCHANGED)
mush = cv.imread(path+"mush.png", cv.IMREAD_UNCHANGED)

forest = cv.resize(forest, (int(forest.shape[1]*0.75), int(forest.shape[0]*0.75)), cv.INTER_CUBIC)
mush = cv.resize(mush, (int(mush.shape[1]*0.08), int(mush.shape[0]*0.08)), cv.INTER_CUBIC)

cv.namedWindow("settings")
cv.createTrackbar('alpha', 'settings', 0, 1000, f)
cv.createTrackbar('beta', 'settings', 0, 1000, f)
cv.createTrackbar('gamma', 'settings', 0, 1000, f)

channels = cv.split(mush)
mush_3 = cv.merge((channels[0], channels[1], channels[2]))

point = (250, 460)
r, c, s = mush_3.shape

part = forest[point[1]:point[1]+r,
              point[0]:point[0]+c]

total = cv.addWeighted(part, 0.5, mush_3, 0.5, 0.5)
forest[point[1]:point[1]+r, point[0]:point[0]+c] = total

cv.imshow("out", forest)

cv.waitKey(0)
cv.destroyAllWindows()
