'''
Function description: motor drive
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *
from smartCar import *

smartcar = smartCar()

while True:
    #Forward
    smartcar.Motor_L(1, 200)
    smartcar.Motor_R(1, 200)
    sleep(2000)
    #back
    smartcar.Motor_L(0, 200)
    smartcar.Motor_R(0, 200)
    sleep(2000)
    #turn left
    smartcar.Motor_L(0, 200)
    smartcar.Motor_R(1, 200)
    sleep(2000)
    #turn right
    smartcar.Motor_L(1, 200)
    smartcar.Motor_R(0, 200)
    sleep(2000)
