'''
Function description: read the IR receiver signals
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''

from microbit import *
from smartCar import *

smartcar = smartCar()

# initialize a variable ir to store the data read by the IR receiver on the car
ir = 0

# loop. Keep reading and processing IR receiver data
while True:
    # call smartcar example ir_data(): it returns the current data read by the IR receiver
    # assign the returned value to variable ir
    ir = smartcar.ir_data()

    # Check if the variable ir is not a None. This may be to ensure that valid data is read, because in some cases the sensor may be not able to read a single value. 
    if ir != None:
        #  If a valid infrared data is read, print it  
        print("ir data:" , ir)

