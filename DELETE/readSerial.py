import serial #Import Serial Library
import tkinter

arduinoSerialData = serial.Serial('com8', 9600) #Create an object for the Serial

while (1==1):  #Create a loop that continues to read and display the data
    
    if (arduinoSerialData.inWaiting()>0):  #Check to see if a data point is available on the serial port
        data =(int(arduinoSerialData.readline().strip())) #Read the encoder, convets the data into and integer and remove the  \r=carriage return and \n=new line characters
        print (data) #Print the measurement to confirm things are working
        
