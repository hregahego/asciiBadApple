
import pygame
import time
import curses
pygame.init()

FPS = 32
CLOCK = pygame.time.Clock()

pygame.mixer.music.load('bad_apple.wav')
pygame.mixer.music.play(0)
framesFiles = open('000frames.txt','r')

frames = framesFiles.read().split(',\n')


def player(window):
    for i in range(len(frames)):

        window.addstr(10, 0, frames[i])
        window.refresh()

        time.sleep((1/36))


curses.wrapper(player)











    



