'''
Function description: car uses ultrasonic sensor to follow object
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *
from smartCar import *

smartcar = smartCar()
distance = 0

while True:
    #read the ultrasonic sensor value
    distance = smartcar.get_distance()
    # determine whether distance is nearer than 6. if yes, car goes back
    if distance < 6:
        smartcar.Motor_L(0, 150)
        smartcar.Motor_R(0, 150)、
    #determine whether distance is within 10 to 30 (can equal to 30). if yes, car goes forward
    elif distance > 10 and distance <= 30:
        smartcar.Motor_L(1, 150)
        smartcar.Motor_R(1, 150)
    #determine whether distance is within 6 to 10 (can equal to 10). if yes, car stops
    elif distance > 6 and distance <= 10:
        smartcar.Motor_L(1, 0)
        smartcar.Motor_R(0, 0)
    #if none of above conditions are satisfied, car stops
    else:
        smartcar.Motor_L(0, 0)
        smartcar.Motor_R(1, 0)
