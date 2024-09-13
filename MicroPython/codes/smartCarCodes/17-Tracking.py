'''
Function description: serial monitor prints the line tracking sensor values
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *  # import microbit module to control micro:bit development board

val_R = 0   #initialize the right line tracking sensor value
val_L = 0   #initialize the left line tracking sensor value

while True:
    val_L = pin12.read_digital()    #read the digital value connected to pin pin12, and assign it to val_L
    val_R = pin13.read_digital()    #read the digital value connected to pin pin13, and assign it to val_R
    print("val_L:" ,val_L ,"val_R:" ,val_R) # print the two line tracking sensors’ values on the serial monitor 
    sleep(500)  # delay 500ms
