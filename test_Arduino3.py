import serial
import time

ser = serial.Serial("com6",9600)
time.sleep(3)
n=5
dataList=[0]*n
stop_read ='Sr'
# while True:
#     while (ser.inWaiting ==0):
#         pass
#     data = ser.readline()
#     data = str(data, 'utf-8')
#     data = data.strip('\r\n')
#     print(data)        -

# while True:
#     #ser.write('W'.encode('utf-8'))
#     ser.write(bytes('A', 'UTF-8'))
#     #time.sleep(1)
#     #print("Data sent")
#     data =ser.readline()
#     print(data)

# while True:
#     UserInput=input("Enter the input")
#     if UserInput=='y':
#         for i in range (0,n):
#             ser.write(b'g')
#             data = ser.readline().decode().split('\r\n')
#             dataList[i]=data
#         print(dataList)
while True:
    ser.write(b'g')
    ser.write('W'.encode('utf-8'))
    ser.write(stop_read.encode('utf-8'))
    print('Data sent')
    time.sleep(1)
    data=ser.readline().decode('ascii')
    print(data)