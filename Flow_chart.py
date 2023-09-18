from tkinter import *
from turtle import color
#import GUI_V4

def st_col_chng():
    T1.config(bg='green')
def ld_cam_col_chng():
    T2.config(bg='green')
def MD_col_chng():
    T3.config(bg='green')
    T4.config(bg='red')
def AD_col_chng():
    T3.config(bg='red')
    T4.config(bg='green')

def Chart(F1):
    global F6
    F6= Canvas(F1, bg='gray')
    F6.place(x=0, y=500, height=500, width=600)
    global T1
    T1= Label(F6, text='START', bg='orange', fg='blue',font='bold, 10', relief=RIDGE, borderwidth=10)
    T1.place(x=250, y=5, height=40, width=100)
    F6.create_line(300, 45,300,80, arrow=LAST, fill='blue', width=5)
    
    global T2
    T2= Label(F6, text='LOAD CAMERA', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T2.place(x=225, y=80, height=40, width=150)
    F6.create_line(300, 120, 170,150, arrow=LAST, fill='blue', width=5)

    global T3
    T3= Label(F6, text='MANUAL DETECTION', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T3.place(x=80, y=155, height=40, width=180)
    F6.create_line(300, 120, 430,150, arrow=LAST, fill='blue', width=5)
    global T4
    T4= Label(F6, text='AUTOMATIC DETECTION', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T4.place(x=340, y=155, height=40, width=180)
    global T5
    T5= Label(F6, text='LOCATE', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T5.place(x=250, y=230, height=40, width=100)
    global T6
    T6= Label(F6, text='HORIZONTAL GRIPPER', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T6.place(x=70, y=305, height=40, width=195)
    global T7
    T7= Label(F6, text='VERTICAL GRIPPER', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T7.place(x=335, y=305, height=40, width=195)
    global T8
    T8= Label(F6, text='MANUAL EOT', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T8.place(x=70, y=390, height=40, width=195)
    global T9
    T9= Label(F6, text='AUTOMATE EOT', bg='orange', fg='blue', font='bold, 10', relief=RIDGE, borderwidth=10)
    T9.place(x=335, y=390, height=40, width=195)



# root= Tk()
# root.geometry('1200x1000')
# #Chart()
# #b1= Button(root, text='click', command=color_change)
# #b1.pack()
# root.bind('<Control-x>', quit)
# root.mainloop()