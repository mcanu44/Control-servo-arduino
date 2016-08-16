# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:31:56 2016

@author: olinero
"""

import serial 


class qubeArduino:
    """A Qube Arduino object, with encoders, motor, serial comunication port and baudrate"""
    def __init__(self, port='com8', baud=9600):
        self.port = port
        self.baud = baud 
        self.encQty = 2-1
        #self.splitChar = '240'
        self.splitChar = '`'
        self.motQty = 1
        self.SerialData = ''
        
        
    def serialOpen(self):
        # Open serial comunicarion with arduino
        self.SerialData = serial.Serial(self.port, self.baud)     

    def serialClose(self):
        self.SerialData.close()
 
class readEncoder:
    def __init__(self, hil, encNo):
        self.hil = hil
        self.encNo = encNo
        self.encCount = ''
   
    def readEnc(self):
        if self.encNo<=self.hil.encQty:
            count=1
            while (count!=25):  #Create a loop that continues to read and display the data
                if (self.hil.SerialData.inWaiting()>0):  #Check to see if a data point is available on the serial port
                    messageIn = self.hil.SerialData.readline().strip()
                    a=self.hil.splitChar.encode('utf-8')
                    self.encCount = messageIn.split(a)[self.encNo]
                    print(self.encCount)
                    count=count+1
           
        else:
            print('Harware only has 2 encoders')






