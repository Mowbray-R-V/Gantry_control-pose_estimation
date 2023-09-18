from cmath import log10
from csv import QUOTE_ALL
from sunau import AUDIO_FILE_ENCODING_ADPCM_G721
from tkinter import *
from PIL import ImageTk, Image
from pyparsing import White
import Rec_Draw
from realsense_camera import *
import cv2 as cv
import Position_est
import EOT_Manu_Move
import Electric_Hoist
import test_camera_live_class1
import test_camera_live_class2
#import Flow_chart

def Load_camera():
    global F5
    F5= Frame(F1, bg='gray')
    F5.place(x=0, y=90, height=400, width=600)
    B_Cam=Button(F5, text="Load Camera", bg='yellow', activebackground="green",font='bold, 12', relief=RAISED, borderwidth=10, command=lambda:[Op_window(), disp_img(),ld_cam_col_chng(), B_Cam.destroy()])
    B_Cam.place(x=240, y=50,width=120, height=40)
    ##Restart Button
    B2= Button(F5, text="RE-START", bg='red', font='bold, 12',relief=RAISED,borderwidth=10, command=lambda:[b1_place(), RESET(), Chart()]) #
    B2.place(x=240, y=350,width=120, height=40)

#SAVE RGB and depth Images from Camera
def Save_bgr_depth():
    
    Position_est.save_frames()
    # ret, bgr_frame, depth_frame, intrinsics, depth =cam.get_frame_stream()
    # cv.imwrite("bgr_frame.jpg", bgr_frame)
    # cv.imwrite("depth_frame.png", depth_frame)
    global intrinsics
    global depth
    ret, intrinsics , depth=Position_est.save_frames()
    if ret==True:
        global L_msg
        L_msg=Label(F3, text="The camera is ready.", fg="green", font="Times, 15", bg="white")
        L_msg.pack()
    

def Op_window():
    
    global B3
    B3= Button(F5, text="Manual Detection", bg="yellow", activebackground="green",font="bold, 12", relief=RAISED, borderwidth=10, command=lambda:[ app1.pack_forget(),Roi_msg.pack_forget(),Imgae_display.pack_forget(),B5.destroy(), ROI(),MD_col_chng(),B4.destroy()]) 
    B3.place(x=20, y=20, height=50, width=200)
    global B4
    B4= Button(F5, text="Automatic Detection", bg="yellow", activebackground="green",font="bold, 12", relief=RAISED, borderwidth=10, command=lambda:[B3.destroy(),AD_col_chng(), B4.destroy(), AD_Verify()])
    B4.place(x=360, y=20, height=50, width=200)

#AUTOMATIC DETECTION Verification
def AD_Verify():
    global ID
    ID, class_ids, boxes, confidence=Position_est.detect_Yolov3()
    if ID>0 and ID<=2:
        Imgae_display.pack_forget()
        cam_msg.pack_forget()
        global Detect_image
        Detect_image= ImageTk.PhotoImage(Image.open("E:\Amit\GUI_PYTHON\GUI/Detection.jpg"))
        global Detect_msg
        Detect_msg=Label(F3, text=" \n The Ingot is detected successfully.", fg='green', font='bold, 15', bg="white")
        Detect_msg.pack(side=TOP, fill='x')
        global Detect_Imgae_display
        Detect_Imgae_display=Label(root, image=Detect_image)
        Detect_Imgae_display.pack()

        global L7
        L7=Label(F5, text='Is the ingot detected correctly?', bg='gray',fg='white', font='bold, 20')
        L7.pack()
        global B7
        B7= Button(F5, text="YES", bg='green', font='bold, 12', relief=RAISED, borderwidth=10,command=lambda:[B7.destroy(),L7.pack_forget(),B8.destroy(), Pose_est()])
        B7.place(x=150, y=50,width=70, height=40)
        global B8
        B8= Button(F5, text="NO", bg='red', font='bold, 12', relief=RAISED, borderwidth=10,command=lambda:[L7.pack_forget(),Detect_msg.pack_forget(),B7.destroy(),B8.destroy(), manu_detec()])
        B8.place(x=280, y=50,width=70, height=40)
    else:
        cam_msg.pack_forget()
        global No_dect_msg
        No_dect_msg=Label(F3, text="The Ingot is not detected successfully. \n Please go for manual detection", bg='green', font='bold, 15')
        No_dect_msg.pack(side=TOP, fill='x')
        #B9.place(x=200, y=50,width=200, height=40)
        manu_detec()

### MANUAL OPTIOn AFTER FAILUER OF AD
def manu_detec():
    global L7
    L7=Label(F5, text='Please go for manual detection', bg='gray', fg='white', font='bold, 15')
    L7.pack()
    global B9
    B9= Button(F5, text="Manual Detection", bg="yellow", font="bold, 12", relief=RAISED, borderwidth=10, command=lambda:[ app1.pack_forget(),Roi_msg.pack_forget(),Imgae_display.pack_forget(),B5.destroy(), Detect_Imgae_display.pack_forget(),ROI(),MD_col_chng_B9(),B4.destroy(), L7.pack_forget()])
    B9.place(x=200, y=50,width=200, height=40)
##### MANUAL ROI DRAW
def Manu_ROI_draw():
    Position_est.crop()
    global Manual_Detect_image
    Manual_Detect_image= ImageTk.PhotoImage(Image.open("E:\Amit\GUI_PYTHON\GUI/M_Detection.jpg"))
    global Manual_Detect_Imgae_display
    Manual_Detect_Imgae_display=Label(root, image=Manual_Detect_image)
    Manual_Detect_Imgae_display.pack()
#### POSE ESTIMATION
def Pose_est():
    global B6
    B6= Button(F5, text="Pose Estimation", bg='yellow', font='bold, 12', relief=RAISED, borderwidth=10,command=lambda:[Pose_col_chng(),B6.destroy(), pose_verify()])
    B6.place(x=180, y=50,width=250, height=40)


#### POSE VERIFICATION
def pose_verify():
    global L8
    L8=Label(F5, text="The system suggested to use V-Gripper.\n Is it right?", bg='gray',fg='white', font='bold, 20')
    L8.pack()
    global L9
    L9= Label(F5, text=" Please attach Vertical Gripper to EOT hook. \n Finished?", bg='gray', fg='white', font='bold, 20')
    global L10
    L10= Label(F5, text="Please attach Horizontal gripper to EOT hook. \n Finished?",bg='gray', fg='white', font='bold, 20')
    global B10
    B10= Button(F5, text="YES", bg='green', font='bold, 12', relief=RAISED, borderwidth=10,command=lambda:[VG_col_chng(),B10.destroy(),L8.pack_forget(),L9.pack(), B11.destroy(), L9.pack(),grip_attach()])
    B10.place(x=150, y=80,width=70, height=40)
    global B11
    B11= Button(F5, text="NO", bg='red', font='bold, 12', relief=RAISED, borderwidth=10,command=lambda:[HG_col_chng(),L8.pack_forget(),B11.destroy(),B10.destroy(),L10.pack(), grip_attach() ])
    B11.place(x=320, y=80,width=70, height=40)

### GRIPPER ATTACH 
def grip_attach():
    
    global B14
    B14= Button(F5, text="YES", bg="yellow", font="bold, 12", relief=RAISED, borderwidth=10, command=lambda:[ B14.destroy(), L9.pack_forget(), L10.pack_forget(), EOT_Option()]) 
    B14.place(x=260, y=80, height=50, width=80)

### EOT OPERATION OPTION
def EOT_Option():
    
    global B12
    B12= Button(F5, text="Manual EOT", bg="yellow", font="bold, 12", relief=RAISED, borderwidth=10, command=lambda:[ B13.destroy(), MEOT_col_chng(), M_EOT_Buttons(), Live_camera_1_open(), Live_camera_2_open()]) 
    B12.place(x=20, y=20, height=50, width=200)
    global B13
    B13= Button(F5, text="Automatic EOT", bg="yellow", font="bold, 12", relief=RAISED, borderwidth=10, command=lambda:[B12.destroy(), AEOT_col_chng()])
    B13.place(x=360, y=20, height=50, width=200)

#### Manual EOT BUTTONS
def M_EOT_Buttons():
    #varLabe=IntVar()
    global X_Plus
    X_Plus= Button(F5, text="X+", bg="red", font="bold, 15", relief=RAISED, borderwidth=10, command=EOT_Manu_Move.set_button1_state)
    X_Plus.place(x=300, y=20, height=50, width=80)
    global X_Minus
    X_Minus= Button(F5, text="X-", bg="red", font="bold, 15", relief=RAISED, borderwidth=10, command=EOT_Manu_Move.set_button2_state)
    X_Minus.place(x=400, y=20, height=50, width=80)

    global Y_Plus
    Y_Plus= Button(F5, text="Y+", bg="green", font="bold, 15", relief=RAISED, borderwidth=10, command=EOT_Manu_Move.set_button3_state)
    Y_Plus.place(x=300, y=100, height=50, width=80)
    global Y_Minus
    Y_Minus= Button(F5, text="Y-", bg="green", font="bold, 15", relief=RAISED, borderwidth=10,command=EOT_Manu_Move.set_button4_state)
    Y_Minus.place(x=400, y=100, height=50, width=80)

    global Z_Plus
    Z_Plus= Button(F5, text="Z+", bg="gold", font="bold, 15", relief=RAISED, borderwidth=10, command=Electric_Hoist.set_button2_Down)
    Z_Plus.place(x=300, y=180, height=50, width=80)
    global Z_Minus
    Z_Minus= Button(F5, text="Z-", bg="gold", font="bold, 15", relief=RAISED, borderwidth=10, command=Electric_Hoist.set_button1_UP)
    Z_Minus.place(x=400, y=180, height=50, width=80)

    global Quit
    Quit=Button(F5, text="QUIT", bg="red",font="bold, 15", relief=RAISED, borderwidth=10, command=lambda:[EOT_Manu_Move.Quit, X_Plus.destroy(),X_Minus.destroy(), Y_Plus.destroy(), 
    Y_Minus.destroy(), Z_Plus.destroy(), Z_Minus.destroy(), B12.destroy(), Quit.destroy(), EOT_Option(), Live_camera_2_close()] )
    Quit.place(x=350, y=250, height=50, width=80)
    Detect_Imgae_display.pack_forget()
    Manual_Detect_Imgae_display.pack_forget()
    aap2.destroy()
    
    
##### COLOR CHANGE FUNCTIONS
def st_col_chng():
    T1.config(bg='green')
def ld_cam_col_chng():
    T2.config(bg='green')
def MD_col_chng():
    T3.config(bg='green')
    T4.config(bg='red')
    F6.delete("Ta4")
    F6.delete("Ta5B")
def AD_col_chng():
    T3.config(bg='red')
    T4.config(bg='green')
    F6.delete("Ta3")
    F6.delete("Ta5A")
def MD_col_chng_B9():
    T3.config(bg='green')
    T4.config(bg='red')
    F6.create_line(300, 120, 170,150, arrow=LAST, fill='blue', width=5, tags="Ta3")
    F6.create_line(170, 190, 300,230, arrow=LAST, fill='blue', width=5, tags="Ta5A")
    F6.delete("Ta4")
    F6.delete("Ta5B")
def Pose_col_chng():
    T5.config(bg='green')
def HG_col_chng():
    T6.config(bg='green')
    T7.config(bg='red')
    F6.delete("Ta7")
    F6.delete("Ta9A")
    F6.delete("Ta9B")
def VG_col_chng():
    T7.config(bg='green')
    T6.config(bg='red')
    F6.delete("Ta6")
    F6.delete("Ta8A")
    F6.delete("Ta8B")
def MEOT_col_chng():
    T8.config(bg='green')
    T9.config(bg='red')
    F6.delete("Ta8B")
    F6.delete("Ta9B")
def AEOT_col_chng():
    T9.config(bg='green')
    T8.config(bg='red')
    F6.delete("Ta8A")
    F6.delete("Ta9A")

###########
def Chart():
    global F6
    F6= Canvas(F1, bg='gray')
    F6.place(x=0, y=550, height=500, width=600)
    global T1
    T1= Label(F6, text='START', bg='orange', fg='blue',font='bold, 10', relief=RIDGE, borderwidth=10)
    T1.place(x=250, y=5, height=40, width=100)
    
    global T2
    F6.create_line(300, 45,300,80, arrow=LAST, fill='blue', width=5)
    T2= Label(F6, text='LOAD CAMERA', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T2.place(x=225, y=80, height=40, width=150)
    
    global T3
    F6.create_line(300, 120, 170,150, arrow=LAST, fill='blue', width=5, tags="Ta3")
    T3= Label(F6, text='MANUAL DETECTION', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T3.place(x=80, y=155, height=40, width=180)
    
    global T4
    F6.create_line(300, 120, 430,150, arrow=LAST, fill='blue', width=5, tags="Ta4")
    T4= Label(F6, text='AUTOMATIC DETECTION', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T4.place(x=340, y=155, height=40, width=180)
    
    global T5
    F6.create_line(170, 190, 300,230, arrow=LAST, fill='blue', width=5, tags="Ta5A")
    F6.create_line(430, 190, 300,230, arrow=LAST, fill='blue', width=5, tags="Ta5B")
    T5= Label(F6, text='POSE ESTIMATION', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T5.place(x=200, y=230, height=40, width=200)

    global T6
    F6.create_line(300, 270, 167.5,300, arrow=LAST, fill='blue', width=5, tags="Ta6")
    T6= Label(F6, text='HORIZONTAL GRIPPER', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T6.place(x=70, y=305, height=40, width=195)

    global T7
    F6.create_line(300, 270, 432.5,300, arrow=LAST, fill='blue', width=5, tags="Ta7")
    T7= Label(F6, text='VERTICAL GRIPPER', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T7.place(x=335, y=305, height=40, width=195)

    global T8
    F6.create_line(167.5, 345, 167.5,390, arrow=LAST, fill='blue', width=5, tags="Ta8A")
    F6.create_line(167.5, 345, 432.5,387, arrow=LAST, fill='blue', width=5,tags="Ta8B")
    T8= Label(F6, text='MANUAL EOT', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T8.place(x=70, y=390, height=40, width=190)

    global T9
    F6.create_line(432.5,345, 167.5,387, arrow=LAST, fill='blue', width=5, tags="Ta9A")
    F6.create_line(432.5,345, 432.5,390, arrow=LAST, fill='blue', width=5,tags="Ta9B")
    T9= Label(F6, text='AUTOMATIC EOT', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T9.place(x=335, y=390, height=40, width=195)


## RESET BUTTON
def RESET():
    F5.destroy()
    Imgae_display.destroy()
    cam_msg.destroy()
    app1.pack_forget()
    Roi_msg.destroy()
    F6.destroy()
    B5.destroy()
    L_msg.destroy()
    Detect_msg.pack_forget()
    No_dect_msg.pack_forget()
    Detect_Imgae_display.pack_forget()
    Manual_Detect_Imgae_display.pack_forget()
    aap2.pack_forget()
    if camera_2==True:
        Live_camera_2_close()
    #F4.destroy()
###ROI draw
def ROI():
    #Display_Image.destroy()
    global app1
    app1= Rec_Draw.ExampleApp1(root)
    app1.pack()
    global Roi_msg
    Roi_msg= Label(root, text="Draw the ROI of Ingot", bg='red',borderwidth=5, font='bold, 15')
    Roi_msg.pack()
    global B5
    B5= Button(root, text="SAVE",font='bold, 12', bg='yellow', relief=RAISED, borderwidth=10, command=lambda:[B3.destroy(), B9.destroy(),Pose_est(), app1.pack_forget(),Roi_msg.pack_forget(),cam_msg.pack_forget(),Manu_ROI_draw(),B5.destroy()])
    B5.pack()
#### LIVE CAMERA
def Live_camera_1_open():
    global camera_1
    camera_1=True
    global aap2
    aap2=test_camera_live_class1.App(root)
    aap2.pack()
def Live_camera_1_close():
    aap2.close()

def Live_camera_2_open():
    global camera_2
    camera_2=True
    global aap3
    aap3= test_camera_live_class2.NewWindow(root)
def Live_camera_2_close():
    aap3.close()
#####################
def disp_img():
    global Camera_image
    #Camera_image= PhotoImage(file="E:\Amit\GUI_PYTHON\GUI/depth_frame.png")
    Camera_image= ImageTk.PhotoImage(Image.open("E:\Amit\GUI_PYTHON\GUI/bgr_frame_raw.jpg"))
    global cam_msg
    cam_msg=Label(root, text="The camera is ready", bg='green', font='bold, 15')
    cam_msg.pack(side=TOP, fill='x')
    global Imgae_display
    Imgae_display=Label(root, image=Camera_image)
    Imgae_display.pack()

### CAMERA LIVE





root=Tk()
root.geometry('1200x1000')
root.title("INGOT HANDLING SYSTEM")
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
F3= Frame(root, bg='white', height=300)
F3.pack(side=BOTTOM, anchor=SE,fill='x', expand=TRUE)
F3.pack_propagate(False)
L4=Label(F3, text='Result', bg='skyblue4', fg="magenta", font='bold, 15', borderwidth=10, relief=SUNKEN).pack(fill='x')
#L6= Label(F3, text="The problem is that at the start of "'\n'"the program the canvas height is equal to 1." '\n'"After that the tkinter window is rendered it changes the value", bg='white').pack(padx=30)


# Res_img=PhotoImage(file="E:\Amit\GUI_Python\Images/2_Color_crop.png")
# Res_display=Label(F3, image=Res_img)
# Res_display.pack()
# F4=Frame(F3,bg='white', height=400)
# F4.pack(fill='x')

def b1_place():
    
    B1= Button(F1, text="START", bg='green', font='bold, 12', relief=RAISED, borderwidth=10,command=lambda:[Load_camera() , B1.destroy(),st_col_chng(), Save_bgr_depth()])
    B1.place(x=250, y=50,width=80, height=40)

b1_place()

##LOADING THE CHART

Chart()
###############



## ASSIGNED NAME

F5= Frame(F1, bg='gray')
#cam1_label =Label(root)
Detect_image= ImageTk.PhotoImage(Image.open("E:\Amit\GUI_PYTHON\GUI/Detection.jpg"))
Detect_Imgae_display=Label(root, image=Detect_image)
Manual_Detect_image= ImageTk.PhotoImage(Image.open("E:\Amit\GUI_PYTHON\GUI/M_Detection.jpg"))
Manual_Detect_Imgae_display=Label(root, image=Manual_Detect_image)
Detect_msg=Label(F3, text=" \n The Ingot is detected successfully.", fg='green', font='bold, 15', bg="white")
No_dect_msg=Label(F3, text="The Ingot is not detected successfully. \n Please go for manual detection", bg='green', font='bold, 15')
L9= Label(F5, text=" Please attach Vertical Gripper to EOT hook. \n Finished?", bg='gray', fg='white', font='bold, 20')
L10= Label(F5, text="Please attach Horizontal gripper to EOT hook. \n Finished?",bg='gray', fg='white', font='bold, 20')
B9= Button(F5, text="Manual Detection", bg="yellow", font="bold, 12", relief=RAISED, borderwidth=10, command=lambda:[ app1.pack_forget(),Roi_msg.pack_forget(),Imgae_display.pack_forget(),B5.destroy(), ROI(),MD_col_chng(),B4.destroy(), L7.pack_forget()])
app1= Rec_Draw.ExampleApp1(root)
aap2=test_camera_live_class1.App(root)
camera_1=False
camera_2=False
#aap3= test_camera_live_class2.NewWindow(root)
cam_msg=Label(root, text="The camera is ready", bg='green', font='bold, 15')
Camera_image= PhotoImage(file="E:\Amit\Ingot_images\RS_camera/1_Color.png")
Imgae_display=Label(root, image=Camera_image)
Roi_msg= Label(root, text="Draw the ROI of Ingot", bg='red',borderwidth=5, font='bold, 15')
B5= Button(root, text="SAVE",font='bold, 12', bg='yellow', relief=RAISED, borderwidth=10, command=lambda:[B3.destroy(), Pose_est(), app1.pack_forget(),Roi_msg.pack_forget(),cam_msg.pack_forget(),disp_img(),B5.destroy()])
##################

root.bind('<Control-x>', quit)
root.mainloop()




