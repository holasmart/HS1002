'''
Function description: serial monitor prints ultrasonic sensor values
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *  # import microbit module to control micro:bit development board  
from smartCar import *  # import smartCar module. This module may be customized to control the smart car  

smartcar = smartCar()  # create a smartCar object to operate the smart car 

distance = 0 # initialize the variable distance value detected by the ultrasonic sensor

while True:
    distance = smartcar.get_distance()  #assign smartcar.get_distance() to distance
    print("distance:", distance ,"CM")   	#print the distance value
    sleep(1000)
