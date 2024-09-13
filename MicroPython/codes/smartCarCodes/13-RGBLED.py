'''
Function description: RGB LED light up in red green blue
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *  # import microbit module to control micro:bit development board
from smartCar import *  # import smartCar module. This module may be customized to control the smart car

smartcar = smartCar()  # create a smartCar object to operate the smart car

while True: # loop. RGB LED continuously display red, green and blue
    smartcar.left_red(0)  # Set R value of the left LED to its maximum, note that here 0 is the maximum while 255 is the darkest
    smartcar.right_red(0)  # Set R value of the right LED to its maximum
    sleep(1000)  # delay 1000 ms (1s) for better observation
    smartcar.led_off()  # turn off all LED to prevent the previous display from affecting the current display
    smartcar.left_green(0)  # Set G value of the left LED to its maximum
    smartcar.right_green(0) # Set G value of the right LED to its maximum
    sleep(1000)
    smartcar.led_off()
    smartcar.left_blue(0) # Set B value of the left LED to its maximum
    smartcar.right_blue(0)# Set B value of the right LED to its maximum
    sleep(1000)
    smartcar.led_off()
    sleep(1000)
