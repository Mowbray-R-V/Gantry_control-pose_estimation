import serial.tools.list_ports
import time

## Defining the variables to be sent
data1 = "800"
data2 = "900"
data3 = "12.12546"
data4 = "1234.129"
data5 = "YouTube"
data6 = "Google"

indexA = "A"
indexB = "B"
indexC = "C"
indexD = "D"
indexE = "E"
indexF = "F"

newLine = "\n"

#Defining the port

ser = serial.Serial('com6', 9600)
print("Reset Aurduino")
time.sleep(3)
#ser.open()
while True:
    ser.write(data1.encode('utf-8'))
    ser.write(indexA.encode('utf-8'))

    ser.write(data2.encode('utf-8'))
    ser.write(indexB.encode('utf-8'))

    ser.write(data3.encode('utf-8'))
    ser.write(indexC.encode('utf-8'))

    ser.write(data4.encode('utf-8'))
    ser.write(indexD.encode('utf-8'))

    ser.write(data5.encode('utf-8'))
    ser.write(indexE.encode('utf-8'))

    ser.write(data6.encode('utf-8'))
    ser.write(indexF.encode('utf-8'))

    ser.write(newLine.encode('utf-8'))

    time.sleep(0.5)
    print("Data Sent")
    data=ser.readline().decode('ascii')
    print(data)
# ser.write(data1.encode('utf-8'))
# ser.write(indexA.encode('utf-8'))

# ser.write(data2.encode('utf-8'))
# ser.write(indexB.encode('utf-8'))

# ser.write(data3.encode('utf-8'))
# ser.write(indexC.encode('utf-8'))

# ser.write(data4.encode('utf-8'))
# ser.write(indexD.encode('utf-8'))

# ser.write(data5.encode('utf-8'))
# ser.write(indexE.encode('utf-8'))

# ser.write(data6.encode('utf-8'))
# ser.write(indexF.encode('utf-8'))

# ser.write(newLine.encode('utf-8'))

# #time.sleep(0.5)
# print("Data Sent")