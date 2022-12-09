

import time
import curses

framesFiles = open('000frames.txt','r')

frames = framesFiles.read().split(',\n')


def player(window):
    for i in range(len(frames)):

        window.addstr(10, 0, frames[i])
        window.refresh()

        time.sleep((1/36))


curses.wrapper(player)











    



