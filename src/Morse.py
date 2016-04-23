# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# From http://code.activestate.com/recipes/578407-simple-morse-code-translator-in-python/

import collections

MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
        
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.' 
    }

morse_code = collections.OrderedDict([
    ('A', '.-'),
    ('B', '-...'),
    ('C', '-.-.'),
    ('D', '-..'),
    ('E', '.'),
    ('F', '..-.'),
    ('G', '--.'),
    ('H', '....'),
    ('I', '..'),
    ('J', '.---'),
    ('K', '-.-'),
    ('L', '.-..'),
    ('M', '--'),
    ('N', '-.'),
    ('O', '---'),
    ('P', '.--.'),
    ('Q', '--.-'),
    ('R', '.-.'),
    ('S', '...'),
    ('T', '-'),
    ('U', '..-'),
    ('V', '...-'),
    ('W', '.--'),
    ('X', '-..-'),
    ('Y', '-.--'),
    ('Z', '--..'),
    
    ('0', '-----'),
    ('1', '.----'),
    ('2', '..---'),
    ('3', '...--'),
    ('4', '....-'),
    ('5', '.....'),
    ('6', '-....'),
    ('7', '--...'),
    ('8', '---..'),
    ('9', '----.'),

    (' ', '   ')
])


def morse2literal(msg):
    result = ""
    for char in msg:
        result += morse_code.get(char.upper(), '?')
    return result

def morse2binary(msg):
    result = ""
    for c in msg:
        if (c == ' ') :
            result += "0000"
        else:
            for dot in morse_code.get(c.upper(), '?'):
                result += "1" if (dot == '.') else "111"
                result += "0"
        result += "00"
    return result


def main():
    
    #msg = raw_input('MESSAGE: ')
    msg = "SOS"
    for char in msg:
        #print (MORSE_CODE[char]) 
        print (morse_code.get(char.upper(), '?'))
    
    print (morse2literal("SOS"))
    print (morse2binary("SOS"))

if __name__ == "__main__":
    main()
