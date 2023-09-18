# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from token import OP
from turtle import update
import cv2 as cv
from PIL import ImageTk, Image
 

class NewWindow(Toplevel):
     
    def __init__(self, master = None, Video_source=2):
         
        super().__init__(master = master)
        self.Video_source=Video_source
        self.vid=MyVideoCapture(Video_source=2)
        self.title("New Window")
        #self.geometry("200x200")
        self.label = Label(self, text ="This is a new Window", background='red')
        self.label.pack()
        #Create Canvas to fit the video
        self.canvas=Canvas(self, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()
        self.exit_button = Button(self, text="Exit", command=self.close)
        self.exit_button.pack(pady=20)
        self.update()
    def update(self):
        isTrue, frame= self.vid.getFrame()
        if isTrue:
            #self.img= Image.fromarray(frame)
            self.photo=ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0,0,anchor='nw', image=self.photo)
        self.after(10, self.update)
    
    def close(self):
        self.destroy()

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


def Open():
    global aap
    aap=NewWindow(master)

def Close():
    aap.close()
# creates a Tk() object
master = Tk()
 
# sets the geometry of
# main root window
master.geometry("200x200")
 
label = Label(master, text ="This is the main window")
label.pack(side = TOP, pady = 10)


#aap.close()
# a button widget which will
# open a new window on button click
btn = Button(master,
             text ="Click to open a new window", command=Open)
 
# Following line will bind click event
# On any click left / right button
# of mouse a new window will be opened
#btn.bind("<Button>",
         #lambda e: NewWindow(master))
 
btn.pack(pady = 10)

b2= Button(master, text="Quit", command=Close)
# b2.bind("<Button>", lambda e: NewWindow.destroy())
b2.pack()
# mainloop, runs infinitely
master.mainloop()