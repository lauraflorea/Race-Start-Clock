# Race-Start-Clock

## Notable Components
  * Raspberry PI
  * 78HC595 (8 bit shift register)
  * hexadecimal LED  
  * 3 LEDS: 1 red, 1 yellow, 1 green
  

## What does it do? 
Below is an explanation of what occurs when the program is run: 
1. When the program starts, the initial state is that the red LED is on and the hexadecimal display segments are all off.

2. The user is prompted to press the button.

3. Once they press the button, the hexadecimal display turns on and depicts a 9.

4. The display next counts down from 9 to 0 every second. 

5. When the hexadecimal LED displays 3, the red LED turns off and the yellow LED turns on. 

6. When the hexadecimal LED displays 0, the yellow LED turns off and the green LED turns on.

7. The user is prompted to press the button again to exit the program.

8. Once they press the button, the green LED and the hexadecimal display turn off.

## Further Explanation 

The circuit has 11 LEDs: a hexadecimal LED which consists of 8 LED segments, and 3 regular LEDs of different colours. 

In order to control each LED, 11 outputs would be required to control each individual LED. 

However, the Raspberry Pi only has 8 possible outputs, so a serial to parallel shift register IC (integrated circuit) is needed to control this circuit.

The 74HC595 is used in this project as the IC, and has 3 input pins:
1. DS, which is where the 8-bit binary code is used to control the LED segments.
2. Serial Clock, which loads the data bit by bit. 
3. R Clock, which controls the output of the internal buffer to the 8 output pins that are linked to the hexadecimal LED (i.e. it shows the data to the output).

The order and sequence of the values displayed on the hexadecimal LED are controlled by the 74HC595. 

The status of the 8 LED segments are uploaded in a serial way, and with another command this data is available to the 8 output pins of the IC. 
