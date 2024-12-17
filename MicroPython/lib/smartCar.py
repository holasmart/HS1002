# from microbit import pin1, pin2, sleep, i2c
from microbit import *
import ustruct
import machine
import utime  # import utime module for time related operations
from time import sleep_us, ticks_us
distance = 0

class smartCar(object):
    def __init__(self):
        self.pin = pin16  # pin of ir receiver
        self.pin.set_pull(self.pin.NO_PULL)  # set pin to non-pull-up mode to ensure that there is no voltage when the pin is suspended
        self.gired_data = [0, 0, 0, 0]  # initialize a list of length 4 for storing the received 4 bytes of data
        self.add = 0x30
        self.set_all_pwm(0)
        self.led_off()

    def set_pwm(self, channel, value):
        i2c.write(self.add, bytearray([channel, value & 0xFF]), repeat=False)

    def set_all_pwm(self, value):
        i2c.write(self.add, bytearray([0x01, value & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0x02, value & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0x03, value & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0x04, value & 0xFF]), repeat=False)

    def Motor_L(self, stateR, right1):
        if (stateR == 0):
            self.set_pwm(1, right1)
            self.set_pwm(2, 0)
        elif (stateR == 1):
            self.set_pwm(1, right1)
            self.set_pwm(2, 255)

    def Motor_R(self, stateL, left1):
        if (stateL == 0):
            self.set_pwm(3, 255)
            self.set_pwm(4, left1)
        elif (stateL == 1):
            self.set_pwm(3, 0)
            self.set_pwm(4, left1)

    def Motor_stop(self):
        self.Motor_L(1 , 0)
        self.Motor_R(1 , 0)
    #control the left RGB led
    def right_red(self , red):
        self.set_pwm(8 , red)

    def right_green(self ,  green):
        self.set_pwm(7 , green)

    def right_blue(self ,  blue):
        self.set_pwm(6 , blue)
    #control the right RGB led
    def left_red(self , red):
        self.set_pwm(9 , red)

    def left_green(self , green):
        self.set_pwm(10 , green)

    def left_blue(self , blue):
        self.set_pwm(5 , blue)

    def led_off(self):
        self.left_red(255)
        self.left_green(255)
        self.left_blue(255)
        self.right_red(255)
        self.right_green(255)
        self.right_blue(255)

    def get_distance(self):
        pin14.write_digital(0)
        sleep_us(2)
        pin14.write_digital(1)
        sleep_us(10)
        pin14.write_digital(0)

        t = machine.time_pulse_us(pin15 , 1 , 35000)
        if (t <= 0 and self.lastEchoDuration >= 0) :
            t = self.lastEchoDuration

        self.lastEchoDuration = t
        return round(t * 0.013)

    #ir receiver
    def wait_for_signal(self, level, timeout_us):
        """Wait for the specified level duration and return False if it times out"""
        start_time = utime.ticks_us()  # Record the current microsecond time
        while utime.ticks_diff(utime.ticks_us(), start_time) < timeout_us:  # Loop before timeout
            if self.pin.read_digital() == level:  # If a specified level is detected
                return True  # return True: signals match
        return False  # If it times out, return False: no signal was detected

    def read_bit(self):
        """Read one bit of data"""
        high_time = 0  # Used to record the duration of the high level
        # Wait for the low part to end, usually the leading 0.56ms part of the data
        if not self.wait_for_signal(1, 600):  # Wait high level with a timeout of 600 microseconds
            return -1  # If the wait times out, return -1: the read failed
        # calculate the high level duration to determine whether the data bit is 0 or 1
        start_time = utime.ticks_us()  # Record the time when the high level starts
        if not self.wait_for_signal(0, 2000):  # Wait for the high level to end with a timeout of 2ms
            return -1  # If the wait times out, return -1: the read failed
        high_time = utime.ticks_diff(utime.ticks_us(), start_time)  # Calculate the high level duration
        return 1 if high_time > 800 else 0  # If the high level time is greater than 800 microseconds, it is 1, otherwise it is 0

    def read_byte(self):
        """Read one bit of data (8 bits)"""
        byte = 0  # Initialize byte data to 0
        for j in range(8):  # Loop 8 times to read 8 bits of data
            bit = self.read_bit()  # Call read_bit to read a bit of data
            if bit == -1:  # If read fails
                return -1  # If -1 is returned, the byte failed to be read
            byte >>= 1  # Move byte right to make room for the next bit of data
            if bit == 1:  # If the read bit is 1
                byte |= 0x80  # Place 1 in the highest bit of byte
        return byte  # Return the complete byte data

    def read_data(self):
        """Read 4 bytes of data and verify"""
        # Wait for a low level of 9ms, usually indicate the guiding part of the infrared signal
        if not self.wait_for_signal(0, 10000):  # Set timeout to 10ms
            return -1  # If times out, return -1: the read failed
        # Wait for 4.5ms high level, part of the guide signal
        if not self.wait_for_signal(1, 5000):  # Set timeout to 5ms
            return -1  # If times out, return -1: the read failed

        for i in range(4):  # Loop 4 times to read 4 bytes of data
            byte = self.read_byte()  # Read a byte
            if byte == -1:  # If read fails
                return -1  # return -1
            self.gired_data[i] = byte  # Save the read bytes to the gired_data list

        # Verify received data: the third byte of data should be the inverse of the fourth byte
        if self.gired_data[2] != ~self.gired_data[3] & 0xff:  # verify through inverse
            return -1  # If the check fails, -1 is returned

        return self.gired_data  # If the check passes, return the complete received data

    def ir_data(self):
        data = self.read_data()  # call read_data to read the ir receiver data
        if data != -1:  # If the data is successfully read
            #print("Received IR data:", data[2])  # Print the received data
            return data[2]


