from tkinter import *

import cv2 as cv
from PIL import Image, ImageTk
import time

####################

class App(Frame):
    def __init__(self,master,Video_source=1):
       Frame.__init__(self,master=0)
       self.Video_source= Video_source
       self.vid=MyVideoCapture(self.Video_source)
       self.label=Label(self, text="Live Streaming: Camera-1", font=15, bg='blue', fg='white').pack(side=TOP, fill=BOTH)

       #Create Canvas to fit the video
       self.canvas=Canvas(self, width=self.vid.width, height=self.vid.height)
       self.canvas.pack()
       self.update()
    
       
    def update(self):
        isTrue, frame= self.vid.getFrame()
        if isTrue:
            self.img= Image.fromarray(frame)
            self.photo=ImageTk.PhotoImage(image=self.img)
            self.canvas.create_image(0,0,anchor='nw', image=self.photo)
        
        self.after(10, self.update)
    def close(self):
        self.destroy()

         
    

###Calss for capturing Video
 
class MyVideoCapture:
    def __init__(self, Video_source=1):
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

# if __name__== "__main__":
#     App()

if __name__ == "__main__":
    root=Tk()
    app = App(root)
    app.pack()

    root.mainloop()