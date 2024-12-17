'''
Function description: the car uses ultrasonic sensor to avoid obstacles
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *
from smartCar import *

smartcar = smartCar()
distance = 0

while True:
    ##read the ultrasonic sensor value
    distance = smartcar.get_distance()
    #determine whether distance is farther than 10. if yes, car goes forward
    if distance > 10:
        smartcar.Motor_L(1, 150)
        smartcar.Motor_R(1, 150)
    #if the above condition is not satisfied, car turns left for 500ms
    else:
        smartcar.Motor_L(0, 150)
        smartcar.Motor_R(1, 150)
        sleep(500)
