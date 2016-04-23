import getopt
import sys
import time
import wiringpi
from gpio import *



def blink():
    # For sequential pin numbering, one of these MUST be called before using IO functions
    wiringpi.wiringPiSetup()
    # Set pin 6 to 1 ( OUTPUT )
    wiringpi.pinMode(0, OUTPUT) 
    while True:
        # Write 1 ( HIGH ) to pin 6
        wiringpi.digitalWrite(0, HIGH)
        time.sleep(0.5)
        # Write 0 ( LOW ) to pin 6
        wiringpi.digitalWrite(0, LOW)
        time.sleep(0.5)


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
        
        blink()
        
    except Usage, err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())

