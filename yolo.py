import cv2 as cv
import numpy as np

# USING YOLOv3-416, so blobFromImage get arg (416, 416)

def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    color = COLORS[class_id]
    cv.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
    cv.putText(img, label, (x-10,y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

classes = None
with open('yolo\\yolo.txt', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
net = cv.dnn.readNet('yolo\\yolo.weights', 'yolo\\yolo.cfg')

image = cv.imread('yolo\\1.jpg')
w = image.shape[1]
h = image.shape[0]

scale = 0.00329
blob = cv.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)

net.setInput(blob)
outs = net.forward(get_output_layers(net))

class_ids = []
conf = []
boxes = []
conf_threshold = 0.5
nms_threshold = 0.4

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > conf_threshold:
            center_x = int(detection[0] * w)
            center_y = int(detection[1] * h)
            bw = int(detection[2] * w)
            bh = int(detection[3] * h)
            x = center_x - bw / 2
            y = center_y - bh / 2
            class_ids.append(class_id)
            conf.append(float(confidence))
            boxes.append([x, y, bw, bh])

indices = cv.dnn.NMSBoxes(boxes, conf, conf_threshold, nms_threshold)

print(len(indices))

for i in indices:
    i = i[0]
    box = boxes[i]
    x = box[0]
    y = box[1]
    w = box[2]
    h = box[3]
    draw_prediction(image, class_ids[i], conf[i], round(x), round(y), round(x + w), round(y + h))

cv.imshow('out', image)
cv.waitKey(0)
cv.destroyAllWindows()
