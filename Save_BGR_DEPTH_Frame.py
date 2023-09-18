#import pyrealsense2 as rs
import numpy as np
import cv2 as cv
from realsense_camera import *

cam = RealsenseCamera()
ret, bgr_frame, depth_frame, intrinsics, depth =cam.get_frame_stream()
def save_frames():
    cv.imwrite("bgr_frame.jpg", bgr_frame)
    cv.imwrite("depth_frame.png", depth_frame)
    return ret, intrinsics , depth
# print(depth)
# print(ret)
# print(intrinsics)
# cv.imshow("Colormap", bgr_frame)
# cv.imshow("depth img", depth_frame)
# cv.waitKey(0)
# cv.destroyAllWindows
