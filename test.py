import PIL.Image
from PIL import Image, ImageTk
from tkinter import *
import numpy as np
import cv2 as cv
#import test_camera_live_class
import time


class App(Toplevel):
    def __init__(self, master=None,Video_source=2):
       
       super().__init__(master=master)
       #self.appName="My Cam"
       #self.window=Tk()
       #self.title(self.appName)
       self['bg']='black'
       self.Video_source= Video_source
       self.vid=MyVideoCapture(self.Video_source)
       self.label=Label(self, text="my cam", font=15, bg='blue', fg='white').pack(side=TOP, fill=BOTH)

       #Create Canvas to fit the video
       self.canvas=Canvas(self, width=self.vid.width, height=self.vid.height)
       self.canvas.pack()
       self.update()
    
       
    def update(self):
        isTrue, frame= self.vid.getFrame()
        if isTrue:
            #self.img= Image.fromarray(frame)
            self.photo=ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0,0,anchor='nw', image=self.photo)
        
        self.after(10, self.update)


###Calss for capturing Video
 
class MyVideoCapture:
    def __init__(self, Video_source=2):
        self.vid=cv.VideoCapture(Video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open this camera", Video_source)
        ##get video height and width
        self.width=self.vid.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height=self.vid.get(cv.CAP_PROP_FRAME_HEIGHT )
    
    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame=self.vid.read() 
            if isTrue:
                return(isTrue, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return(isTrue, None)
        else:
            return(isTrue, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()





root = Tk()
root.geometry("500x500")
b=Button(root, text="Cam")
b.bind("<Button>", lambda e: App(root))
b.pack()

#test_camera_live_class.App()

root.mainloop()
