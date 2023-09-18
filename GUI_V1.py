

from tkinter import *
import cv2 as cv
from PIL import ImageTk, Image
import PIL.Image
import Rec_Draw
import test4
import os



def ROI():
    #Display_Image.destroy()
    global app1
    app1= Rec_Draw.ExampleApp1(root)
    app1.pack()
    L1= Label(root, text="Draw the ROI of Ingot", bg='red',borderwidth=5, font='bold, 15').pack()

def Del():
    app1.pack_forget()

def dest_buttons():
    B2.destroy()
    B3.destroy()


def Detect_option():
    global B2
    B2=Button(F1, text='Manual Detection', bg='yellow', font='bold, 15', command= lambda: [ROI(),  L1.pack_forget(), B3.destroy()])#test4.ROI_draw())   #.grid(row=1, column=0)
    #B2.pack(side= LEFT)
    B2.place(x=10, y=60)
    global B3
    B3=Button(F1, text='Automatic Dtection', bg='yellow', font='bold, 15', command=lambda:[B2.destroy(), L1.pack_forget(), Del()])#command=test4.ExampleApp.on_close)    #.grid(row=1, column=2)
    #B3.pack(side=RIGHT)
    B3.place(x=400, y=60)
    

    ####Display Image
    # global Camera_image
    # Camera_image= PhotoImage(file="E:\Amit\Ingot_images\RS_camera/1_Color.png")
    # # Camera_image= PhotoImage(file="E:\Amit\GUI_Python\Images/2_Color.png")
    # Imgae_display=Label(F2, image=Camera_image)
    # Imgae_display.pack()

# def Display_Image():
#     #new=Toplevel(root)
#     #new=Tk()
#     #app = Rec_Draw.ExampleApp(root)
#     app=test4.ExampleApp(root)
#     app.pack()
#     #new.mainloop()


    


root = Tk()
root.geometry('1200x1000')
root.title('Ingot Handling GUI')
F1= Frame(root, bg='gray', height=800, width=600, relief=RAISED)
F1.pack(side=LEFT,fill='both')
#F2 = Frame(root, bg='pink' ,height=400, relief=RAISED)
#F2.pack(side=TOP, fill='both')
#F3= Frame(root, bg='white', height=400 ,relief=RAISED)
#F3.pack(side=BOTTOM, fill='both')
# L1= Label(F1, text='START')
# L1.pack(side= TOP, padx=300)
L1 =Label(root, text="The camera is ready", font='bold, 15', fg='green')
B1=Button(F1, text='START', bg='green', font='bold, 15', command=lambda: [Detect_option(), L1.pack()])#Detect_option)   #.grid(row=0, padx=300)
#B1.pack(side=TOP, padx=300)
B1.place(x=260, y=10, width=80, height=40)
B_reset= Button(F1, text="Reset", bg='red', font='bold, 15', borderwidth=10, command= dest_buttons).place(x=500, y=200, width=80, height=40)

root.bind('<Control-x>', quit)
root.mainloop()