'''
Function description: read the IR remote control button values to control the car
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *
from smartCar import *

smartcar = smartCar()
ir = 0
while True:
    #read the IR receiver values
    ir = smartcar.ir_data()
    #determine whether ir equals 70. if yes, car goes forward
    if ir == 70:
        smartcar.Motor_L(1, 200)
        smartcar.Motor_R(1, 200)
    #determine whether ir equals 21. if yes, car goes back
    elif ir == 21:
        smartcar.Motor_L(0, 200)
        smartcar.Motor_R(0, 200)
    #determine whether ir equals 68. if yes, car turns left
    elif ir == 68:
        smartcar.Motor_L(0, 200)
        smartcar.Motor_R(1, 200)
    #determine whether ir equals 67. if yes, car turns right
    elif ir == 67:
        smartcar.Motor_L(1, 200)
        smartcar.Motor_R(0, 200)
    #determine whether ir equals 64. if yes, car stops
    elif ir == 64:
        smartcar.Motor_L(1, 0)
        smartcar.Motor_R(1, 0)

