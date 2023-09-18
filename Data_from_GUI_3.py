import serial.tools.list_ports
from tkinter import *
import time
import tkinter

#Defining the variables that will be used in our script
motRun ="1"
indexA = "A"
indexB = "B"
indexC = "C"
indexD = "D"

newline = "S"

N1 = 90
N2 = 1000

#Defing the serail port

ser = serial.Serial('com6', 9600)
print("Reset Arduino")
time.sleep(3)
ser.write(bytes('L', 'UTF-8'))

def sendData(motDir):
    StepN1=str(N1)
    ser.write(StepN1.encode('utf-8'))
    ser.write(indexA.encode('utf-8'))

    ser.write(motDir.encode('utf-8'))
    ser.write(indexB.encode('utf-8'))

    ser.write(newline.encode('utf-8'))

def RotateClockwise():
    motDir = "CW"
    sendData(motDir)
    data= ser.read().decode('ascii')
    print(data)

def RotateCounterClockwise():
    motDir = "CCW"
    sendData(motDir)

tkTop = tkinter.Tk()
tkTop.geometry('300x200')
tkTop.title("MotorControl")
label3 = tkinter.Label(text = 'Python GUI,'
                      '\n Stepper Motor controller',font=("Arial", 12,'bold')).pack()

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()

varLabel2 = tkinter.IntVar()
tkLabel2 = tkinter.Label(textvariable=varLabel2, )
tkLabel2.pack()

varLabel3 = tkinter.IntVar()
tkLabel3 = tkinter.Label(textvariable=varLabel3, )
tkLabel3.pack()

varLabel4 = tkinter.IntVar()
tkLabel4 = tkinter.Label(textvariable=varLabel4, )
tkLabel4.pack()

button1 = tkinter.IntVar()
button1state = tkinter.Button(tkTop,
    text="Move Forward",
    command=RotateClockwise,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button1state.pack(side='top', ipadx=10, padx=10, pady=15)

button2 = tkinter.IntVar()
button2state = tkinter.Button(tkTop,
    text="Move Backward",
    command=RotateCounterClockwise,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button2state.pack(side='top', ipadx=10, padx=10, pady=15)

button3 = tkinter.IntVar()
button3state = tkinter.Button(tkTop,
    text="Move Left",
    #command=set_button3_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button3state.pack(side='top', ipadx=10, padx=10, pady=15)

button4 = tkinter.IntVar()
button4state = tkinter.Button(tkTop,
    text="Move Right",
    #command=set_button4_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button4state.pack(side='top', ipadx=10, padx=10, pady=15)

tkButtonQuit = tkinter.Button(
    tkTop,
    text="Quit",
    command=quit,
    height = 4,
    fg = "black",
    width = 8,
    bg = 'yellow',
    bd = 5,
)
tkButtonQuit.pack(side='top', ipadx=10, padx=10, pady=15)

tkinter.mainloop()