from tkinter import *

import cv2 as cv
from PIL import Image, ImageTk
import time
####################

class App:
    def __init__(self, Video_source=2):
       self.appName="My Cam"
       self.window=Tk()
       self.window.title(self.appName)
       self.window['bg']='black'
       self.Video_source= Video_source
       self.vid=MyVideoCapture(self.Video_source)
       self.label=Label(self.window, text=self.appName, font=15, bg='blue', fg='white').pack(side=TOP, fill=BOTH)

       #Create Canvas to fit the video
       self.canvas=Canvas(self.window, width=self.vid.width, height=self.vid.height)
       self.canvas.pack()
       self.update()
    
       self.window.mainloop()
    def update(self):
        isTrue, frame= self.vid.getFrame()
        if isTrue:
            self.img= Image.fromarray(frame)
            self.photo=ImageTk.PhotoImage(image=self.img)
            self.canvas.create_image(0,0,anchor='nw', image=self.photo)
        
        self.window.after(10, self.update)


         
    

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

if __name__== "__main__":
    App()