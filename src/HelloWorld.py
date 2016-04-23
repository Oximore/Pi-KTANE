# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import time
import Morse
from gpio import *


def morseDisplay(msg):
    for digit in Morse.morse2binary(msg):
        print (LOW if (digit == '0') else HIGH)
        time.sleep(0.3)

def morseBlink(msg):
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(0, OUTPUT) 
    for digit in Morse.morse2binary(msg):
        wiringpi.digitalWrite(0, (LOW if (digit == '0') else HIGH))
        time.sleep(0.3)


if __name__ == "__main__":
    print( morseDisplay("Hello World"))
