import serial
import time
import tkinter

n=5
def RotateCW():
    for i in range(0,n):
        #set_button1_state()
        ser.write(bytes('W', 'UTF-8'))
        #time.sleep(0.1)
        i+=1
        
def RotateCCW():
    for i in range(0,n):
        #set_button1_state()
        ser.write(bytes('S', 'UTF-8'))
        #time.sleep(0.1)
        i+=1

def quit():
    global tkTop
    ser.write(bytes('L', 'UTF-8'))
    tkTop.destroy()

def set_button1_state():
        varLabel.set("MOVE FORWARD ")
        ser.write(bytes('W', 'UTF-8'))
        time.sleep(3)
        ser.write(bytes('W', 'UTF-8'))
        time.sleep(3)
        ser.write(bytes('W', 'UTF-8'))
        time.sleep(3)
        #ser.write(bytes(N3.encode('UTF-8')))
        #ser.write(N3)
        # Step_value = ser.readline()
        # return Step_value

def set_button2_state():
        varLabel.set("MOVE BACKWARD ")
        ser.write(bytes('S', 'UTF-8'))

def set_button3_state():
        varLabel.set("MOVE LEFT ")
        ser.write(bytes('A', 'UTF-8'))

def set_button4_state():
        varLabel.set("MOVE RIGHT ")
        ser.write(bytes('D', 'UTF-8'))

# Change the COM PORT to whatever it shows in Arduino
#ser = serial.Serial('com5', 9600)
ser = serial.Serial('com5', 9600)
print("Reset Arduino")
time.sleep(3)
#ser.write(bytes('L', 'UTF-8'))


#ser.write(bytes(N3, 'UTF-8'))


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
    #command= set_button1_state,
    command= RotateCW,
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
    #command=set_button2_state,
    command=RotateCCW,
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
    command=set_button3_state,
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
    command=set_button4_state,
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