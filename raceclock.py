#!/usr/bin/python
import RPi.GPIO as GPIO  # Raspberry Pi control module
import time

# Mapping of GPIO Controller pins to Serial Registers
SDI = 11  # Serial data in
RCLK = 12  # Register clock
SRCLK = 13  # Serial shift clock
BUTTON = 15  # Start button
RED = 16  # Red LED control
YELLOW = 18  # Yellow LED control
GREEN = 22  # Green LED control

# LED segment map to display digits 0 - 9
digits = {
    0: '00111111',
    1: '00000110',
    2: '01011011',
    3: '01001111',
    4: '01100110',
    5: '01101101',
    6: '01111101',
    7: '00000111',
    8: '01111111',
    9: '01101111',
    'off': '00000000'
}


def boardInit():  # force the inital state of the board
    GPIO.setwarnings(False)  # don't want warnings from hardware
    GPIO.setmode(GPIO.BOARD)  # want to use controller pin numbering instead of the connector

    GPIO.setup(SDI, GPIO.OUT, initial=0)  # set pin 0 as the output and send 0 (0V)
    GPIO.setup(RCLK, GPIO.OUT, initial=0)  # set pin 1 as the output and send 0 (0V)
    GPIO.setup(SRCLK, GPIO.OUT, initial=0)  # set pin 2 as the output and send 0 (0V)
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set the button input to 1 (5V)

    GPIO.setup(RED, GPIO.OUT, initial=0)  # turn on the red LED 
    GPIO.setup(YELLOW, GPIO.OUT, initial=1)  # turn off the yellow LED 
    GPIO.setup(GREEN, GPIO.OUT, initial=1)  # turn off the green LED 


def hc595Output(digits):
    # load the 8-bit pattern to the display the digit with the 595 chip 
    for i in range(8):
        segment = int(digits[i])
        GPIO.output(SDI, int(digits[i]))  # load data
        
        # generate a clock signal for 1 ms (0 -> 1 -> 0)
        GPIO.output(SRCLK, 1)
        time.sleep(0.001)
        GPIO.output(SRCLK, 0)
        
        # generate the RCLK signal to make the loaded 8-bit pattern avaulable on the 595's parallel outputs 
        GPIO.output(RCLK, 1)
        time.sleep(0.001)
        GPIO.output(RCLK, 0)


if __name__ == "__main__":      # main section 
    boardInit()                     # initalize the board
    hc595Output(digits['off'])      # turn the display off 
    
    print("Press button to start")
        
    while GPIO.input(BUTTON) == 1:  # Wait for the button to be pressed, read 0 
        time.sleep(0.1)
    
    for i in range(9, 0, -1):   # generate and display digits 9 -> 0 
        hc595Output(digits[i])  # call the display function with the corresponding bit patten 
        
        if i == 3:              # when there are 3 seconds left, turn on the yellow LED and turn off the red one 
            GPIO.output(RED, 1)
            GPIO.output(YELLOW, 0)
        
        time.sleep(1)   

        GPIO.output(YELLOW, 1)      # Turn off the yellow LED 
        hc595Output([digits[0]])    # Display 0 
        GPIO.output(GREEN, 0)       # Turn on the green LED 
        
        print("Press button to exit program")

        while GPIO.input(BUTTON) == 1:  # Wait for the button to be pressed, read 0 
            time.sleep(0.1)

        hc595Output(digits['off'])      # Turn the display off 
        GPIO.cleanup()
