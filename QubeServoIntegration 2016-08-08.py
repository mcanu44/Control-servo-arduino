import serial
from tkinter import *
from time import sleep
# Part 1

# ---HIL initialize

#Identifies all addresable components in this harware, encoder1, encoder2, motor

serialPort = 'com8'
serialBoud = 9600

# Open serial comunicarion with arduino
arduinoSerialData = serial.Serial(serialPort, serialBoud)

# reads the serial port and interprets the encoder
def update():
    #encoder2 = 'M'.encode('utf-8') #assigns and encode the prefix of encoder1
    encoder2 = '`'.encode('utf-8') #assigns and encode the prefix of encoder2
    while (1==1):  #Create a loop that continues to read and display the data
        if (arduinoSerialData.inWaiting()>0):  #Check to see if a data point is available on the serial port
            #Read the serial port, remove the  \r=carriage return and \n=new line characters
            messageIn = arduinoSerialData.readline().strip()
            encoderCount1 = messageIn[0:messageIn.find(encoder2)] 
            encoderCount2 = messageIn[messageIn.find(encoder2)+1:]
                        
            motorSpeedEnc.set(encoderCount1) #updates ecoder1 lable
            root.update() # Updates root window to display encoders
            #sleep(1)





# ---HIL read encoder
# reads the serial port and extract the specified encoder information



# Part 2 Function attached to widgets

            
def motorClick():
    motorSpeedCom.set(motorEntry.get())
    txtr=motorEntry.get()+'\n'
    texttoarduino=txtr.encode('utf-8')
    arduinoSerialData.write(texttoarduino)
    #return mes

def quitClick():
    arduinoSerialData.close()# Closes the serial port
    root.destroy()#closes the window

root=Tk()#creates the main window

# variable initialization for widgets
motorSpeedCom = StringVar() #current motor speed command
motorSpeedEnc = StringVar() #motor encoder speed
#motorSpeedReq = StringVar() #motor speed request

#buttons
#motor speed update
motorUpdate = Button(root, text='motor speed update', command=motorClick)
motorUpdate.pack()
#safe quit, closes the serial port before closing the window
destroy = Button(root, text='safe quit', command=quitClick)
destroy.pack()

#lables
# encoder 1 read
encoder1 = Label(root, textvariable = motorSpeedEnc)
encoder1.pack()
root.after(1,update) 


#current motor speed command
motorIn = Label(root, textvariable=motorSpeedCom)
motorIn.pack()
#motor speed request
motorEntry = Entry(root)
#, textvariable=motorSpeedReq
motorEntry.pack()


   
root.mainloop()
