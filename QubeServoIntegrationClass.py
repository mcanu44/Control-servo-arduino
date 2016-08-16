import serial
from tkinter import *
from time import sleep
import raven as ra

hil0=ra.qubeArduino()
enc0=ra.readEncoder(hil0, 0)

hil0.serialOpen()



enc0.readEnc()


hil0.serialClose()