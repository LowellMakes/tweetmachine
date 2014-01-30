from random import randint
import pygame
import subprocess
import time
def displayText(text, size, line, color, clearScreen):
    if clearScreen:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, size)
        text = font.render(text, 0, color)
        textRotated = pygame.transform.rotate(text, 0)
        textpos = textRotated.get_rect()
        textpos.centery = 90
        if line == 1:
            textpos.top = 0
            textpos.centerx = 310
            screen.blit(textRotated,textpos)
        elif line == 2:
            textpos.centerx = 40
            screen.blit(textRotated,textpos)


def main():
    global screen
    pygame.init()
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(0)
    while(True):
        number = str(randint(1000,9999))
        text = "tweet @Makesbot lowellmakes " + number
        displayText(text, 50, 1, (200,200,1), True )
       ## pygame.display.flip()
       ## time.sleep(1)

        graph = pygame.image.load("testimg.jpg")
        graph = pygame.transform.rotate(graph, 0)
        graphrect = graph.get_rect()
        graphrect.top = 40
        graphrect.centerx = 310
        screen.blit(graph, graphrect)
        pygame.display.flip()

        feedmonitor = subprocess.Popen(['./tweetmachine.sh',number],shell=True)
        time.sleep(30)
        feedmonitor.kill()

if __name__ == '__main__':
    main()
