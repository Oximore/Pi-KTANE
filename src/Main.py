#!/usr/bin/env python3
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import Morse
import HelloWorld

if __name__ == "__main__":
    msg = "Hello World"
    print(msg)
    print(Morse.morse2literal(msg))
    print(Morse.morse2binary(msg))
    HelloWorld.morseDisplay(msg)