'''
Function description: RGB LED dimming and lighting up
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *  # import microbit module to control micro:bit development board
from smartCar import *  # import smartCar module. This module may be customized to control the smart car

smartcar = smartCar()  # create a smartCar object to operate the smart car

while True:  # loop. LED dims and lights up
    for num in range(0 , 255):  # for loop. range from 0 to 254 (range excluds endpoint)
        num += 1  # num adds 1: num = num + 1
        smartcar.left_red(255 - num)  # set the R value of left LED to decrease with the increase of num
        smartcar.right_red(255 - num)  # set the R value of right LED to decrease with the increase of num
        sleep(10)  # delay 10ms

    for num in range(0 , 255):  # one more for loop: LED from off to on
        num += 1  # num adds 1
        smartcar.left_red(num)  # set the R value of left LED to increase with the increase of num
        smartcar.right_red(num)  # set the R value of right LED to increase with the increase of num
        sleep(10)  # delay 10ms
