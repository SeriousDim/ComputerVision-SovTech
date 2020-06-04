import cv2
import numpy as np

cap = cv2.VideoCapture(0)

segment = [(0, 0)]


def calc(begin_seg, end_seg):
    lenght_line = end_seg - begin_seg
    center_line = end_seg - lenght_line // 2
    segment.append((center_line, lenght_line))
    print(center_line, lenght_line)
    return 0


def find_max():
    if np.shape(segment)[0] > 1:
        segment.sort(key=lambda r: r[1])
        coordinate_center = (segment[np.shape(segment)[0] - 1][0] + segment[np.shape(segment)[0] - 2][0]) // 2
        cv2.circle(frame, (coordinate_center * 3, frame.shape[0] - 60), 20, (255, 0, 255))


while 1:
    _, frame = cap.read()
    size = (frame.shape[1] // 3, frame.shape[0] // 3)

    frame_small = cv2.resize(frame, size)
    hsv_temp = cv2.cvtColor(frame_small, cv2.COLOR_BGR2HSV)
    bw = cv2.inRange(hsv_temp, (0, 0, 0), (180, 255, 84))
    line = bw[bw.shape[0] - 20]
    line_zoom = cv2.resize(line, (100, line.shape[0]))
    # print(line)
    segment = []
    f_begin = 0
    for i in range(len(line)):
        if (line[i] == 255) and (f_begin == 0):
            f_begin = 1
            begin = i
        elif (line[i] == 0) and (f_begin == 1):
            f_begin = 0
            end = i
            calc(begin, end)
    for i in range(np.shape(segment)[0]):
        temp_circle = segment[i]
        # print( temp_circle) 
        cv2.circle(frame, (temp_circle[0] * 3, frame.shape[0] - 60), temp_circle[1], (255, 255, 255))
    find_max()
    cv2.imshow('CAM0', frame)
    cv2.imshow('B\W', bw)
    cv2.imshow('Zoom', line_zoom.T)
    key = cv2.waitKey(20)
    if (key == 27):
        break

cv2.destroyAllWindows()