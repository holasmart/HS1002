'''
Function description: car follows light
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *
from smartCar import *

smartcar = smartCar()
ldr_l = 0
ldr_r = 0

while True:
    # read the two photoresistors values
    ldr_l = pin1.read_analog()
    ldr_r = pin0.read_analog()
    #determine whether both ldr_l and ldr_r are both greater than 650. If yes, car goes forward
    if ldr_l > 650 and ldr_r > 650:
        smartcar.Motor_L(1, 150)
        smartcar.Motor_R(1, 150)
    #determine whether ldr_l  is greater than 650 and ldr_r is less than 650. if yes, car turns left
    elif ldr_l > 650 and ldr_r < 650:
        smartcar.Motor_L(0, 200)
        smartcar.Motor_R(1, 200)
    #determine whether ldr_l is less than 650 and ldr_r is greater than 650. if yes, car turns right
    elif ldr_l < 650 and ldr_r > 650:
        smartcar.Motor_L(1, 200)
        smartcar.Motor_R(0, 200)
    #if all above conditions are not satisfied, car stops
    else:
        smartcar.Motor_L(0, 0)
        smartcar.Motor_R(1, 0)
