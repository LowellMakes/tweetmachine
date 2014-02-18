#!/usr/bin/python
import os
import sys
from random import randint
import pygame
import subprocess
import time
import pifacedigitalio as piface
from optparse import OptionParser


logo_path = '/home/pi/tweetmachine/'

def displayText(text, size, line, color, clearScreen):
    if clearScreen:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, size)
        text = font.render(text, 0, color)
        textRotated = pygame.transform.rotate(text, 0)
        textpos = textRotated.get_rect()
        textpos.centery = 90
      ##  if line == 1:
        textpos.top = line
        textpos.centerx = 310
        screen.blit(textRotated,textpos)
       ## elif line == 2:
       ##     textpos.centerx = 40
       ##     screen.blit(textRotated,textpos)

def displayLogo():
    g2path = logo_path + "logo.png"
    graph2 = pygame.image.load(g2path)
    graph2 = pygame.transform.scale(graph2,(600,400))
    graph2rect = graph2.get_rect()
    graph2rect.top = 0
    graph2rect.centerx = 310
    screen.blit(graph2,graph2rect)
    pygame.display.flip()

def displayTwitter():
    number = str(randint(1000,9999))
    text = "tweet @Makesbot lowellmakes " + number
    displayText(text, 50, 1, (200,200,1), True )
    gpath = logo_path+"testimg.jpg"
    graph = pygame.image.load(gpath)
    graph = pygame.transform.rotate(graph, 0)
    graphrect = graph.get_rect()
    graphrect.top = 40
    graphrect.centerx = 310
    screen.blit(graph, graphrect)
    pygame.display.flip()
    cmd ="./tweetmachine.sh "+number
    feedmonitor = subprocess.Popen(['su','pi','-c',cmd])
    feedmonitor.wait()
    screen.fill((0,0,0))
    pygame.display.flip()

def main():
    piface.init()
    global screen
    pygame.init()
    if (not os.path.isdir(logo_path)):
        print "ERROR: tweetmachine dir not found in"
        print logo_path
        sys.exit(2)
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(0)

    parser = OptionParser()
    parser.add_option("-t", "--twitter", dest="twitter", action="store_true",\
default=False, help= "start monitoring twitter feed")
    parser.add_option("-l", "--logo", dest="logo", action ="store_true",\
default=False, help= "display LowellMakes Logo")
    parser.add_option("-w", "--write",dest="text", default ='', help = "display\
text on the screen")
    parser.add_option("-a", "--auto", dest="loop", default =False, action ="store_true",\
help = "runs a loop, accepts input from the std_in")
    parser.add_option("-b", "--btn", dest="btn", default =False, action ="store_true", help = "polls the coin return button")
    (options,args)=parser.parse_args()

    if(options.twitter == True):
        displayTwitter()
    elif(options.logo == True):
        displayLogo()
    elif(not(options.text is '')):
        displayText(options.text, 100, 30, (200,200,1), True )
    elif(options.btn == True):
        while(True):
            if piface.digital_read(0):
                displayTwitter()
                displayLogo()
            elif piface.digital_read(2):
                break;
    elif(options.loop == True):
        end = True
        while(end):
            usr_input=raw_input("enter choice l=logo,t=twitter,e=exit\n")
            if usr_input is "t":
                displayTwitter()
            elif usr_input is "l":
                displayLogo()
            elif usr_input is "e":
                break;
            time.sleep(1)
    time.sleep(1)
if __name__ == '__main__':
    main()
