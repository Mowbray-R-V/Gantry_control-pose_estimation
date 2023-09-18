
import serial
import time
from tkinter import *


def Quit():
    ser.write(bytes('L', 'UTF-8'))
    

def set_button1_state():
        #varLabel.set("MOVE FORWARD ")
        ser.write(bytes('W', 'UTF-8'))

def set_button2_state():
        #varLabel.set("MOVE BACKWARD ")
        ser.write(bytes('S', 'UTF-8'))

def set_button3_state():
        #varLabel.set("MOVE LEFT ")
        ser.write(bytes('A', 'UTF-8'))

def set_button4_state():
        #varLabel.set("MOVE RIGHT ")
        ser.write(bytes('D', 'UTF-8'))

# Change the COM PORT to whatever it shows in Arduino
ser = serial.Serial('com5', 9600)
print("Reset Arduino")
time.sleep(3)
ser.write(bytes('L', 'UTF-8'))

