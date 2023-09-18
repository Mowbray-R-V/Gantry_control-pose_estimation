from tkinter import *
from PIL import Image, ImageTk
import cv2 as cv
import test
# Create an instance of TKinter Window or frame
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create a Label to capture the Video frames
label =Label(win)
#label.grid(row=0, column=0)
label.pack()

cam1= cv.VideoCapture(2)
cam2= cv.VideoCapture(2)
# Define function to show frame
# def show_frames():
#    # Get the latest frame and convert into Image
#    cv2image= cv.cvtColor(cam1.read()[1],cv.COLOR_BGR2RGB)
#    img = Image.fromarray(cv2image)
#    # Convert image to PhotoImage
#    imgtk = ImageTk.PhotoImage(image = img)
#    label.imgtk = imgtk
#    label.configure(image=imgtk)
#    # Repeat after an interval to capture continiously
#    label.after(10, show_frames)
# #global cam1_label

cam1_label =Label(win)
cam1_label.pack()
def show_cam1():
    
   # Get the latest frame and convert into Image
    cv2image= cv.cvtColor(cam1.read()[1],cv.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    cam1_label.imgtk = imgtk
    cam1_label.config(image=imgtk)
   # Repeat after an interval to capture continiously
    cam1_label.after(10, show_cam1)

# def test_cam():
#     img=test.show_frames()
#     cam1_label =Label(win)
#     cam1_label.pack()
#     imgtk = ImageTk.PhotoImage(image = img)
#     cam1_label.imgtk = imgtk
#     cam1_label.config(image=imgtk)
#     cam1_label.after(10, test_cam)
#show_frames()
show_cam1()
#test_cam()
win.mainloop()