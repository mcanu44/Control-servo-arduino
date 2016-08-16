import serial
from tkinter import *
from time import sleep
arduinoSerialData = serial.Serial('com8', 9600)

def update():
    while (1==1):  #Create a loop that continues to read and display the data
        if (arduinoSerialData.inWaiting()>0):#Check to see if a data point is available on the serial port
            reading.set(arduinoSerialData.readline().strip()) #Read the encoder, convets the data into and integer and remove the  \r=carriage return and \n=new line characters
            root.update()
            #sleep(1)
            
def click():
    mesy.set(entry.get())
    txtr=entry.get()+'\n'
    texttoarduion=txtr.encode('utf-8')
    arduinoSerialData.write(texttoarduion)
    #return mes
root=Tk()
mesy = StringVar()
mesy.set('')

reading = StringVar()
spe = StringVar()
button = Button(root, text='Click', command=click)
button.pack()
w = Label(root, textvariable = reading)
w.pack()
label = Label(root, textvariable=mesy)
label.pack()
entry = Entry(root, textvariable=spe)
entry.pack()


root.after(1,update)    
root.mainloop()
