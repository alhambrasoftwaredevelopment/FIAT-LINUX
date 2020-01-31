import random

'''
create random 2D array width x height


'''

import pygame as pg
from settings import *

pg.init()

row01 = [6, 8, 9, 10, 18]
row02 = [16, 1, 5, 22, 3]
row03 = [2, 13, 11, 14, 19]
row04 = [12, 20, 15, 7, 4]
row05 = [17, 0, 24, 21, 23]
total = [row01, row02, row03, row04, row05]
print(total)
vertlist = []
for y in range(0, 5):
    vertlist.append(total[y][FOCUSY])
print(vertlist)
vertlist.append(vertlist[0])
vertlist.remove(vertlist[0])
print(vertlist)
goback = vertlist.pop(-1)
vertlist.insert(0, goback)
print(vertlist)
all_sprites = pg.sprite.Group()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Sprite Example")
clock = pg.time.Clock()
running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            if FOCUSX <= 1:
                FOCUSX = 1
            else:
                FOCUSX = FOCUSX - 1
            print('(x:' + str(FOCUSX) + ', y:' + str(FOCUSY) + ')')
            print(ARRAY[FOCUSY][FOCUSX])
        if keystate[pg.K_RIGHT]:
            try:
                FOCUSX += 1
                if FOCUSX >= SQUARESIZE - 1:
                    FOCUSX = SQUARESIZE - 1
            except:
                FOCUSX += 1
            print('(x:' + str(FOCUSX) + ', y:' + str(FOCUSY) + ')')
            print(ARRAY[FOCUSY][FOCUSX])
        if keystate[pg.K_UP]:
            if FOCUSY >= SQUARESIZE:
                FOCUSY = SQUARESIZE
            else:
                FOCUSY = FOCUSY - 1
                if FOCUSY <= 0:
                    FOCUSY = 0
            print('(x:' + str(FOCUSX) + ', y:' + str(FOCUSY) + ')')
            print(ARRAY[FOCUSY][FOCUSX])
        if keystate[pg.K_DOWN]:
            if FOCUSY >= SQUARESIZE:
                FOCUSY = SQUARESIZE
            else:
                FOCUSY = FOCUSY + 1
                if FOCUSY >= SQUARESIZE:
                    FOCUSY = SQUARESIZE
            print('(x:' + str(FOCUSX) + ', y:' + str(FOCUSY) + ')')
            print(ARRAY[FOCUSY][FOCUSX])

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
