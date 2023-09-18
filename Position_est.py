from cv2 import imread
import numpy as np
import open3d as o3d
import cv2 as cv
from realsense_camera import *


rs = RealsenseCamera()
ret, bgr_frame, depth_frame, intrinsics, depth =rs.get_frame_stream()
def save_frames():
    cv.imwrite("bgr_frame_raw.jpg", bgr_frame)
    cv.imwrite("depth_frame_raw.png", depth_frame)
    return ret, intrinsics , depth
##Bounding box coordinates in pixels


def detect_Yolov3():
    yolo_bgr_frame=imread("E:\Amit\GUI_PYTHON\GUI/bgr_frame_raw.jpg")
    net = cv.dnn.readNet("E:\\Amit\\YOLOv3_Custom_Training\\2nd\yolov3\\backup\\yolov3_custom_last.weights", "E:\\Amit\\YOLOv3_Custom_Training\\2nd\yolov3\\darknet\\cfg\\yolov3_custom.cfg")
    classes = []
    with open('E:\\Amit\\YOLOv3_Custom_Training\\2nd\\yolov3\\darknet\\data\\classes.names') as f:
        classes = f.read().splitlines()

    print(classes)
    height, width, _ = yolo_bgr_frame.shape
    blob = cv.dnn.blobFromImage(yolo_bgr_frame, 1/255, (416,416), (0,0,0), swapRB=True , crop=False)

    # for b in blob:
    #     for n, img_blob in enumerate(b):
    #         cv.imshow(str(n), img_blob)

    net.setInput(blob)

    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)


    boxes = []
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]* width)
                center_y = int(detection[1]* height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
            
                x = int(center_x - w/2)
                y = int(center_y - h/2)


                boxes.append([x,y,w,h])
                confidences.append((float(confidence))) 
                class_ids.append(class_id)



    #print(len(boxes))
    indexs = cv.dnn.NMSBoxes(boxes,confidences, 0.5, 0.4) #Threshold =0.5, maximum supression=0.4
    # print("indexes: ",indexs)
    # print("Flatten: ",indexs.flatten())

    font = cv.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0,255, size=(len(boxes), 3))
    #directory= '/home/mds/Pose_Estimation'
    ID=0
    for i in indexs.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str(round(confidences[i],2))
        color = colors[i]
        cv.rectangle(yolo_bgr_frame, (x,y), (x+w, y+h), color, 2)
        cv.putText(yolo_bgr_frame, label + " " + confidence, (x, y-10), font, 1, (255,255,255),1)
        ID=i
    print(ID)
    cv.imwrite('Detection.jpg',yolo_bgr_frame)
    #cv.imshow('BGR_frame', yolo_bgr_frame)
    cv.waitKey(0)
    cv.destroyAllWindows
    return ID, class_ids, boxes, confidence

def crop():
    cord= np.loadtxt("ROI.txt").astype(np.int64)
    #print(ROI[0])
    x1=cord[0]
    y1=cord[1]
    x2=cord[2]
    y2=cord[3]
    w= x2-x1
    h= y2-y1
    #print(w,h)
    pt1=(x1,y1)
    pt2=(x1+w,y1+h)
    color = (0, 0, 255)
    ###READ Images
    bgr_frame=cv.imread("E:\Amit\GUI_PYTHON\GUI/bgr_frame_raw.jpg")
    depth_frame=cv.imread("E:\Amit\GUI_PYTHON\GUI/depth_frame_raw.png")
    Cropped_bgr = bgr_frame[y1:y1+h, x1:x1+w]
    #Cropped_depth = depth_frame[y1:y1+h, x1:x1+w]
    cv.imwrite('Cropped_bgr.jpg', Cropped_bgr)
    #cv.imwrite('Cropped_depth.png', Cropped_depth)
    cv.rectangle(bgr_frame, pt1,pt2, color, thickness=2)
    cv.imwrite('M_Detection.jpg',bgr_frame)
    #cv.imshow("RGB", bgr_frame)
    #cv.imshow("Cropped BGR", Cropped_bgr)
    cv.waitKey(0)
    cv.destroyAllWindows


#save_frames()
#detect_Yolov3()
#crop()