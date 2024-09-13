'''
Function description: serial monitor prints photoresistor value
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *  # import microbit module to control micro:bit development board 

ldr_R = 0  # initialize the right photoresistor value
ldr_L = 0  # initialize the left photoresistor value

while True:  # loop. print the values all the time
    ldr_L = pin1.read_analog()  # read the analog value of the photoresistor connected to pin1, and assign to ldr_L
    ldr_R = pin0.read_analog()  # read the analog value of the photoresistor connected to pin0, and assign to ldr_R
    print("ldr_L:", ldr_L, "ldr_R:", ldr_R)  # print the two photoresistor values
    sleep(500)  # delay 500ms
