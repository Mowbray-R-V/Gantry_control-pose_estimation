from tkinter import *
import Rec_Draw
def Op_window():
    global F5
    F5= Frame(F1, bg='gray')
    F5.place(x=0, y=90, height=400, width=600)
    ##Restart Button
    B2= Button(F5, text="RE-START", bg='green', font='bold, 12',relief=RAISED,borderwidth=10, command=lambda:[b1_place(), RESET()]) #
    B2.place(x=240, y=350,width=120, height=40)
    global B3
    B3= Button(F5, text="Manual Detection", bg="yellow", font="bold, 12", relief=RAISED, borderwidth=10, command=lambda:[ app1.pack_forget(),Roi_msg.pack_forget(),Imgae_display.pack_forget(), ROI(),B4.destroy()]) #app1.pack_forget(),Roi_msg.pack_forget(),ROI(),
    B3.place(x=20, y=20, height=50, width=200)
    global B4
    B4= Button(F5, text="Automatic Detection", bg="yellow", font="bold, 12", relief=RAISED, borderwidth=10)
    B4.place(x=360, y=20, height=50, width=200)

## RESET BUTTON
def RESET():
    F5.destroy()
    Imgae_display.destroy()
    cam_msg.destroy()
    app1.pack_forget()
    Roi_msg.destroy()

###ROI draw
def ROI():
    #Display_Image.destroy()
    global app1
    app1= Rec_Draw.ExampleApp1(root)
    app1.pack()
    global Roi_msg
    Roi_msg= Label(root, text="Draw the ROI of Ingot", bg='red',borderwidth=5, font='bold, 15')
    Roi_msg.pack()

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

root=Tk()
root.geometry('1200x1000')

##LEFT SIDE FRAME
F1= Frame(root, bg='gray', width=600)
F1.pack(side=LEFT,fill='both')
L1=Label(F1, text='Control Window', bg='cyan', fg="red", font='bold, 15', borderwidth=10, relief=SUNKEN, width=50).pack(side=TOP,fill='x')
L3=Label(F1, text='Control Chart', bg='coral', fg="black", font='bold, 15', borderwidth=10, relief=SUNKEN, width=50).pack(side=LEFT, fill='x')

#RIGHT SIDE TOP OPRATION WINDOW FRAME
F2 = Frame(root, bg='pink' ,height=50)
F2.pack(side=TOP, fill='both')
L2=Label(F2, text='Operation Window', bg='yellow', fg="magenta", font='bold, 15',borderwidth=10, relief=SUNKEN, width=50).pack(fill='x')


## RIGHT SIDE BOTTOM RESULT WINDOW FRAME
F3= Frame(root, bg='white', height=700)
F3.pack(side=BOTTOM, anchor=SE,fill='x', expand=TRUE)
L4=Label(F3, text='Result', bg='gold', fg="magenta", font='bold, 15', borderwidth=10, relief=SUNKEN).pack(fill='x')
L6= Label(F3, text="The problem is that at the start of "'\n'"the program the canvas height is equal to 1." '\n'"After that the tkinter window is rendered it changes the value", bg='white').pack(padx=30)


Res_img=PhotoImage(file="E:\Amit\GUI_Python\Images/2_Color_crop.png")
Res_display=Label(F3, image=Res_img)
Res_display.pack()
F4=Frame(F3,bg='white', height=200)
F4.pack(fill='x')

def b1_place():
    
    B1= Button(F1, text="START", bg='green', font='bold, 12', relief=RAISED, borderwidth=10,command=lambda:[ Op_window(), B1.destroy(), disp_img()])
    B1.place(x=260, y=50,width=80, height=40)
b1_place()


## ASSIGNED NAME
app1= Rec_Draw.ExampleApp1(root)
Roi_msg= Label(root, text="Draw the ROI of Ingot", bg='red',borderwidth=5, font='bold, 15')
##################

root.bind('<Control-x>', quit)
root.mainloop()




