from textwrap import fill
from tkinter import *
from PIL import ImageTk, Image
import PIL.Image
import Rec_Draw
#import Full_scren_window


##Operation Buttons frames
def Op_window():
    global F4
    F4= Frame(root, bg='gray')
    F4.place(x=0, y=90, height=250, width=765)
    ##Restart Button
    B2= Button(F4, text="RE-START", bg='green', font='bold, 12',relief=RAISED,borderwidth=10, command=lambda:[b1_place(), RESET()])
    B2.place(x=320, y=210,width=120, height=40)
    
    B3= Button(F4, text="Manual Detection", bg="yellow", font="bold, 12", relief=RAISED, borderwidth=10, command=lambda:[app1.pack_forget(),Roi_msg.pack_forget(),ROI(), Imgae_display.pack_forget(), B4.destroy()])
    B3.place(x=30, y=10, height=50, width=200)
    global B4
    B4= Button(F4, text="Automatic Detection", bg="yellow", font="bold, 12", relief=RAISED, borderwidth=10)
    B4.place(x=535, y=10, height=50, width=200)

###ROI draw
def ROI():
    #Display_Image.destroy()
    global app1
    app1= Rec_Draw.ExampleApp1(root)
    app1.pack()
    global Roi_msg
    Roi_msg= Label(root, text="Draw the ROI of Ingot", bg='red',borderwidth=5, font='bold, 15')
    Roi_msg.pack()

def RESET():
    F4.destroy()
    Imgae_display.destroy()
    cam_msg.destroy()
    app1.pack_forget()
    Roi_msg.destroy()

####Display Image
def disp_img():
    global Camera_image
    Camera_image= PhotoImage(file="E:\Amit\Ingot_images\RS_camera/1_Color.png")
    # Camera_image= PhotoImage(file="E:\Amit\GUI_Python\Images/2_Color.png")
    global cam_msg
    cam_msg=Label(root, text="The camera is ready", bg='green', font='bold, 15')
    cam_msg.pack(side=TOP, fill='x')
    global Imgae_display
    Imgae_display=Label(root, image=Camera_image)
    Imgae_display.pack()






root= Tk()
#Full_scren_window.FullScreenApp(root)
root.geometry('1200x1000')
root.title('GUI')

##CONTROL WINDOW FRAME AND LABEL
F1= Frame(root, bg='cyan', height=40, width=700, borderwidth=10, relief=SUNKEN)
F1.pack(side=LEFT,anchor=NW)
L1=Label(F1, text='Control Window', bg='cyan', fg="magenta", font='bold, 15')
L1.pack(padx=300)



##OPERATION WINDOW FRAME AND LABEL
F2= Frame(root, bg='yellow', height=40, borderwidth=10, relief=SUNKEN)
F2.pack(side=TOP,anchor=NE, fill= 'x')
L2=Label(F2, text='Operation Window', bg='yellow', fg="magenta", font='bold, 15')
L2.pack()

##Start FRAME and BUTTON



##Operation chart Head
# F5 = Frame(root, bg='yellow',relief=SUNKEN, borderwidth=10)
# #F5.place(x=0, y=351,  height=50, width=765)
# F5.pack(side=LEFT)
# L3=Label(F5, text='Control Chart', bg='yellow', fg="magenta", font='bold, 15')
# L3.pack()

# F6 = Frame(root, bg='green',relief=SUNKEN, borderwidth=10)
# #F6.place(x=765, y=351,  height=50)
# F6.pack(side=RIGHT)
# L4=Label(F6, text='Result', bg='green', fg="magenta", font='bold, 15')
# L4.pack()

def b1_place():
    F3= Frame(root, bg='gray')
    F3.place(x=0, y=50, height=300, width=765)
    B1= Button(F3, text="START", bg='green', font='bold, 12', relief=RAISED, borderwidth=10,command=lambda:[Op_window(), B1.destroy(), disp_img()])
    B1.place(x=340, y=0,width=80, height=40)
b1_place()





##Operation Chart Frame
# F6= Frame(root, bg='red', width=765,height=500)
# F6.pack(side=LEFT, anchor=SW, fill='x')

## ASSIGNED NAME
app1= Rec_Draw.ExampleApp1(root)
Roi_msg= Label(root, text="Draw the ROI of Ingot", bg='red',borderwidth=5, font='bold, 15')
##################


root.bind('<Control-x>', quit)
root.mainloop()