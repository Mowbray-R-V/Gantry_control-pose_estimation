from os import X_OK
import cv2 as cv
import numpy as np
from numpy.lib.npyio import savetxt
import open3d as o3d
from realsense_camera import*
#import pyrealsense2 as rs
import matplotlib.pyplot as plt
import pickle
import math
from decimal import Decimal, ROUND_HALF_UP


net = cv.dnn.readNet('/home/amit/yolov3/backup/yolov3_custom_last.weights', '/home/amit/yolov3/darknet/cfg/yolov3_custom.cfg')
classes = []
with open('/home/amit/yolov3/darknet/data/classes.names') as f:
    classes = f.read().splitlines()

print(classes)

#Camera cordinate and world cordinate offset
theta = math.radians(30)
X_trans = 0
Y_trans = -2
Z_trans = 3

#Load realsense camera

rs = RealsenseCamera()
ret, bgr_frame, depth_frame, intrinsics, depth =rs.get_frame_stream()

#cv.imshow("BGR frame", bgr_frame)
#img = cv.imread('D455/24-09-2021/1_Color.png')
height, width, _ = bgr_frame.shape
blob = cv.dnn.blobFromImage(bgr_frame, 1/255, (416,416), (0,0,0), swapRB=True , crop=False)

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
for i in indexs.flatten():
    x, y, w, h = boxes[i]
    label = str(classes[class_ids[i]])
    confidence = str(round(confidences[i],2))
    color = colors[i]
    cv.rectangle(bgr_frame, (x,y), (x+w, y+h), color, 2)
    cv.putText(bgr_frame, label + " " + confidence, (x, y-10), font, 1, (255,255,255),1)
    
    x_center = int(x + w/2 )
    y_center = int(y + h/2 )
    dist = depth.get_distance(x_center, y_center)*100 # convert to cm
    print("The center distance is ",dist, "cm")
    # WRT camera cordinate
    X_c = dist*(x_center -intrinsics.ppx)/intrinsics.fx
    Y_c = dist*(y_center -intrinsics.ppy)/intrinsics.fy
    Z_c = dist
    print("The cordinates X_c, Y_c, Z_c are:", X_c, Y_c, Z_c)

    #Cordinates wit respect to world
    X_w = -X_c  #3.5cm is RGB camera module offset
    Y_w = -(Y_c*math.cos(theta)+Z_c*math.sin(theta)) + Y_trans
    Z_w = (-Y_c*math.sin(theta)+ Z_c*math.cos(theta))- Z_trans

    Coordinates = np.array([round(X_w), round(Y_w), round(Z_w)])
    
    print("The real world cordinates X, Y, Z are: ", Coordinates, " in cm")
    #crop with accurate bounding box
    Cropped_bgr = bgr_frame[y:y+h, x:x+w]
    Cropped_depth = depth_frame[y:y+h, x:x+w]
    #Crop with reduced bounding box
    # Cropped_bgr = bgr_frame[y+25:y+h-15, x+20:x+w-25]
    # Cropped_depth = depth_frame[y+25:y+h-15, x+20:x+w-25]
    #cv.imshow('Image', img)
    # cv.imshow('Cropped image', Cropped_bgr)
    # cv.imshow('Cropped depth', Cropped_depth)
    cv.imwrite('Cropped_bgr.jpg', Cropped_bgr)
    cv.imwrite('Cropped_depth.png', Cropped_depth)
    
color_raw = o3d.io.read_image("Cropped_bgr.jpg")
depth_raw = o3d.io.read_image("Cropped_depth.png")
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw)
print(rgbd_image)

# point cloud with camera intrinsic parameters
#pinhole_camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(intrinsics.width, intrinsics.height, intrinsics.fx, intrinsics.fy, intrinsics.ppx, intrinsics.ppy)
pinhole_camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(intrinsics.width, intrinsics.height, intrinsics.fx, intrinsics.fy, w, h)
#print(pinhole_camera_intrinsic.intrinsic_matrix)
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image, pinhole_camera_intrinsic)

pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
#Point cloud with default intrinsic parameters
# pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
#     rgbd_image,
#     o3d.camera.PinholeCameraIntrinsic(
#         o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))

# pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
#pcd.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([pcd])
o3d.io.write_point_cloud("Cropped_point_cloud.pcd", pcd)
print(pcd)
#print(np.asarray(pcd.points))
data= np.asarray(pcd.points)
savetxt('data.csv',np.asarray(pcd.points), delimiter=',')
#data = np.array([pcd])
# print(data)

#print(Cropped_depth, Cropped_bgr)
#rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(Cropped_bgr, Cropped_depth)
#rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(bgr_frame, depth_frame)
#print(rgbd_image)
# x_min = x
# x_max = x+w
# y_min = y
# y_max = y+h



#cv.imshow('Image', cv.resize(img, (1500,800), interpolation=cv.INTER_LINEAR_EXACT))
# print(height, width, w, h)

# print(x_min, x_max, y_min, y_max)

#Cropped = img[x:x+w, y:y+h]

cv.imshow('BGR_frame', bgr_frame)
cv.imwrite('Detection.jpg',bgr_frame)
cv.waitKey(0)
cv.destroyAllWindows
