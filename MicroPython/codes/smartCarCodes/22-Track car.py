'''
Function description: car follows black line
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *
from smartCar import *

smartcar = smartCar()
val_l = 0
val_r = 0

while True:
    # read the line tracking sensor values
    val_l = pin12.read_digital()
    val_r = pin13.read_digital()
    #determine whether both val_l and val_r equal 0. if yes, car goes forward
    if val_l == 0 and val_r == 0:
        smartcar.Motor_L(1, 150)
        smartcar.Motor_R(1, 150)
    # determine whether val_l = 0 and val_r = 1. if yes, car turns left
    elif val_l == 0 and val_r == 1:
        smartcar.Motor_L(0, 200)
        smartcar.Motor_R(1, 200)
    #determine whether val_l = 1 and val_r = 0. if yes, car turns right
    elif val_l == 1 and val_r == 0:
        smartcar.Motor_L(1, 200)
        smartcar.Motor_R(0, 200)
    # if none of the above conditions are satisfied, the car stops
    else:
        smartcar.Motor_L(0, 0)
        smartcar.Motor_R(1, 0)
