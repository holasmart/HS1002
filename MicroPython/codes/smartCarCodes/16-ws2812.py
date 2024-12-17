'''
Function description: ws2812 shows: red, green, blue, cyan, pink, yellow and off
Compiling IDE: MU 1.2.0
Program name: HolaSmart
'''
from microbit import *  # import microbit module to access hardware
import neopixel  # import neopixel library to control WS2812 LED

# the number of NeoPixel pixels connected to pin P8
NUM_PIXELS = 2
# create NeoPixel object, connect to pin P8
np = neopixel.NeoPixel(pin8 , NUM_PIXELS)

while True:
    #show red
    for num in range(0, 2) :    # traverse all connected LED
        np[num] = (255, 0, 0)   # Set the current LED to red
        np.show()   # Update the display status of the LED
    sleep(1000) # delay 1s
    #Show green
    for num in range(0, 2) :    # traverse all connected LED
        np[num] = (0, 255, 0)  # Set the current LED to green
        np.show()  # Update the display status of the LED
    sleep(1000)  # delay 1s
    # Similarly, set blue, cyan, pink, yellow, and off
    #show blue
    for num in range(0, 2) :
        np[num] = (0, 0, 255)
        np.show()
    sleep(1000)
    #show cyan
    for num in range(0, 2) :
        np[num] = (0, 255, 255)
        np.show()
    sleep(1000)
    #show pink
    for num in range(0, 2) :
        np[num] = (255, 0, 255)
        np.show()
    sleep(1000)
    #show yellow
    for num in range(0, 2) :
        np[num] = (255, 255, 0)
        np.show()
    sleep(1000)
    #turn off
    for num in range(0, 2) :
        np[num] = (0, 0, 0)
        np.show()
    sleep(1000)
