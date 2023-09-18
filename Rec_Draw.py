import PIL.Image
from PIL import Image, ImageTk
from tkinter import *
import numpy as np


class ExampleApp1(Frame):
    def __init__(self,master):
        #Frame.__init__(self,master=None)
        Frame.__init__(self,master=0)
        self.x = self.y = 0
        self.canvas = Canvas(self, height=500, width=650, cursor="cross")
        self.canvas.pack()
        
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.rect = None

        self.start_x = None
        self.start_y = None

        self.im = PIL.Image.open("E:\Amit\GUI_PYTHON\GUI/bgr_frame_raw.jpg")
        #self.wazil,self.lard=self.im.size
        #self.canvas.config(scrollregion=(0,0,self.wazil,self.lard))
        self.tk_im = ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)   


    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        # create rectangle if not yet exist
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')
            #print(self.start_x, self.start_y)

    def on_move_press(self, event):
        curX = self.canvas.canvasx(event.x)
        curY = self.canvas.canvasy(event.y)

        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if event.x > 0.9*w:
            self.canvas.xview_scroll(1, 'units') 
        elif event.x < 0.1*w:
            self.canvas.xview_scroll(-1, 'units')
        if event.y > 0.9*h:
            self.canvas.yview_scroll(1, 'units') 
        elif event.y < 0.1*h:
            self.canvas.yview_scroll(-1, 'units')

        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)
        
        
        
    


    def on_button_release(self, event):
        endX=self.canvas.canvasx(event.x)
        endY=self.canvas.canvasx(event.y)
        print(self.start_x, self.start_y, endX, endY)
        f= open('ROI.txt', 'a')
        f.truncate(0)
        f.write(f"{self.start_x}" + ' ')
        f.write(f"{self.start_y}"+ ' ')
        f.write(f"{endX}"+ ' ')
        f.write(f"{endY}"+ ' ')
        pass



if __name__ == "__main__":
    root=Tk()
    app = ExampleApp1(root)
    app.pack()

    root.mainloop()