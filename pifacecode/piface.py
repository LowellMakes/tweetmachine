import os
import sys
import pifacedigitalio as piface
from optparse import OptionParser
import time

valid_selections=["b3","b5","d3","d5","c3","c5"]

def idle_state():
    piface.digital_write(0, 0)
    piface.digital_write(1, 0)
    piface.digital_write(2, 0)
    piface.digital_write(3, 0)
    piface.digital_write(4, 0)
    piface.digital_write(5, 0)
    piface.digital_write(6, 0)
    piface.digital_write(7, 0)
    time.sleep(.2)


def snd_b():
    piface.digital_write(0, 1)
    piface.digital_write(3, 1)
    piface.digital_write(6, 1)
    piface.digital_write(7, 1)
    time.sleep(.2)

def snd_d():
    piface.digital_write(1,1)
    piface.digital_write(5,1)
    time.sleep(.2)

def snd_c():
    piface.digital_write(1,1)
    piface.digital_write(3,1)
    piface.digital_write(7,1)
    time.sleep(.2)

def snd_three():
    piface.digital_write(0, 1)
    piface.digital_write(5, 1)
    piface.digital_write(6, 1)
    time.sleep(.2)

def snd_five():
    piface.digital_write(3, 1)
    piface.digital_write(5, 1)
    piface.digital_write(7, 1)
    time.sleep(.2)

def test():
    for i in range(0,8):
        piface.digital_write(i,0)
        time.sleep(.2)
        piface.digital_write(i,1)
        time.sleep(.2)

def main():
    piface.init()
    parser = OptionParser()

    usage = "cmd -s <a1>"

    parser.add_option("-s", "--selection", type ="string", help="-s <b3,b5,d3,d5,c3,c5", dest ="selection")

    options,arguments = parser.parse_args()

    if(options.selection not in valid_selections):
        print "Invalid Selection"
    else:
        idle_state();
        if options.selection == "b3":
            snd_b();
            idle_state();
            snd_three();
        elif options.selection == "b5":
            snd_b();
            idle_state();
            snd_five();
        elif options.selection == "d3":
            snd_d();
            idle_state();
            snd_three();
        elif options.selection == "d5":
            snd_d();
            idle_state();
            snd_five();
        elif options.selection == "c3":
            snd_c();
            idle_state();
            snd_three();
        elif options.selection == "c5":
            snd_c();
            idle_state();
            snd_five();
        idle_state();



## TODO: add the user input stuff here



if __name__ == "__main__":
        main()
