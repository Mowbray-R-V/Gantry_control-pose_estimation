
import serial
import time
from tkinter import *


def Quit():
    ser.write(bytes('L', 'UTF-8'))
    

def set_button1_UP():
        #varLabel.set("MOVE FORWARD ")
        ser.write(bytes('U', 'UTF-8'))

def set_button2_Down():
        #varLabel.set("MOVE BACKWARD ")
        ser.write(bytes('D', 'UTF-8'))


# Change the COM PORT to whatever it shows in Arduino
ser = serial.Serial('COM4', 9600)
print("Reset Arduino")
time.sleep(3)
ser.write(bytes('L', 'UTF-8'))

# root=Tk()
# root.geometry("1000x1000")
# Z_Minus= Button(root, text="UP", bg="gold", font="bold, 15", relief=RAISED, borderwidth=10, command=set_button1_UP)
# Z_Minus.place(x=400, y=180, height=50, width=80)
# Z_Plus= Button(root, text="DOWN", bg="gold", font="bold, 15", relief=RAISED, borderwidth=10, command=set_button2_Down)
# Z_Plus.place(x=400, y=300, height=50, width=80)
# root.mainloop()