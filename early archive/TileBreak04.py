'''
Progress - created a swipe left and right system that works - probably can get a vertical version.
create random 2D array width x height
add a move counter
add a "solver that compares with how far you are from solving
make the game have expandable size


'''

import random

import pygame as pg
from settings import *

pg.init()


def focus(FOCUSX, FOCUSY):
    print_it_up(FOCUSX, FOCUSY)
    return FOCUSX, FOCUSY


def focus_left(FOCUSX, FOCUSY):
    if FOCUSX > 0:
        FOCUSX -= 1
    focus(FOCUSX, FOCUSY)
    pg.time.delay(100)
    return FOCUSX


def focus_right(FOCUSX, FOCUSY):
    if FOCUSX < 4:
        FOCUSX += 1
    focus(FOCUSX, FOCUSY)
    pg.time.delay(100)
    return FOCUSX


def focus_up(FOCUSX, FOCUSY):
    if FOCUSY > 0:
        FOCUSY -= 1
    focus(FOCUSX, FOCUSY)
    pg.time.delay(100)
    return FOCUSY


def focus_down(FOCUSX, FOCUSY):
    if FOCUSY < 4:
        FOCUSY += 1
    focus(FOCUSX, FOCUSY)
    pg.time.delay(100)
    return FOCUSY


def rot_clock(FOCUSX, FOCUSY):
    start_x = FOCUSX
    start_y = FOCUSY
    try:
        if start_x >= 1 and start_x <= ARRAY_WIDTH - 1 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 1:
            bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
            total[start_y - 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest

            bitstobeadded = total[start_y + 1].pop(start_x - 1)  # moving a piece from northwest to west
            total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west

            bitstobeadded = total[start_y].pop(start_x + 1)
            total[start_y + 1].insert(start_x + 1, bitstobeadded)

            bitstobeadded = total[start_y - 1].pop(start_x + 2)
            total[start_y].insert(start_x + 1, bitstobeadded)
            print_it_up(FOCUSX, FOCUSY)
            return total
    except:
        pass


def rot_counterclock(FOCUSX, FOCUSY):
    start_x = FOCUSX
    start_y = FOCUSY
    try:
        if start_x >= 1 and start_x <= ARRAY_WIDTH - 1 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 1:
            bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
            total[start_y + 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest
            bitstobeadded = total[start_y - 1].pop(start_x - 1)  # moving a piece from northwest to west
            total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west
            bitstobeadded = total[start_y].pop(start_x + 1)
            total[start_y - 1].insert(start_x + 1, bitstobeadded)
            bitstobeadded = total[start_y + 1].pop(start_x + 2)
            total[start_y].insert(start_x + 1, bitstobeadded)
            print_it_up(FOCUSX, FOCUSY)
            return total
    except:
        pass


def print_it_up(FOCUSX, FOCUSY):
    for i in range(PRINTBUFFER):
        print("")
    print('current focus: x={}, y={}'.format(FOCUSX, FOCUSY))
    print('move count: {}'.format(movecount))
    if FOCUSX == 0:
        print("     v")
    elif FOCUSX == 1:
        print("         v")
    elif FOCUSX == 2:
        print("              v")
    elif FOCUSX == 3:
        print("                   v")
    elif FOCUSX == 4:
        print("                        v")
    if FOCUSY == 0:
        print(
            ">   {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  <".format(total[0][0], total[0][1], total[0][2],
                                                                       total[0][3],
                                                                       total[0][4]))
    else:
        print(
            "    {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  ".format(total[0][0], total[0][1], total[0][2],
                                                                      total[0][3],
                                                                      total[0][4]))
    if FOCUSY == 1:
        print(
            ">   {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  <".format(total[1][0], total[1][1], total[1][2],
                                                                       total[1][3],
                                                                       total[1][4]))
    else:
        print(
            "    {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  ".format(total[1][0], total[1][1], total[1][2],
                                                                      total[1][3],
                                                                      total[1][4]))
    if FOCUSY == 2:
        print(
            ">   {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  <".format(total[2][0], total[2][1], total[2][2],
                                                                       total[2][3],
                                                                       total[2][4]))
    else:
        print(
            "    {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  ".format(total[2][0], total[2][1], total[2][2],
                                                                      total[2][3],
                                                                      total[2][4]))
    if FOCUSY == 3:
        print(
            ">   {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  <".format(total[3][0], total[3][1], total[3][2],
                                                                       total[3][3],
                                                                       total[3][4]))
    else:
        print(
            "    {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  ".format(total[3][0], total[3][1], total[3][2],
                                                                      total[3][3],
                                                                      total[3][4]))
    if FOCUSY == 4:
        print(
            ">   {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  <".format(total[4][0], total[4][1], total[4][2],
                                                                       total[4][3],
                                                                       total[4][4]))
    else:
        print(
            "    {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  ".format(total[4][0], total[4][1], total[4][2],
                                                                      total[4][3],
                                                                      total[4][4]))
    if FOCUSX == 0:
        print("     ^")
    elif FOCUSX == 1:
        print("         ^")
    elif FOCUSX == 2:
        print("              ^")
    elif FOCUSX == 3:
        print("                   ^")
    elif FOCUSX == 4:
        print("                        ^")
    for i in range(10 - PRINTBUFFER):
        print("")


def get_vert(FOCUSX, FOCUSY):
    print_it_up(FOCUSX, FOCUSY)
    vertlist = []
    vertcolumn = []
    for x in range(0, 5):
        for y in range(0, 5):
            vertcolumn.append(total[y][x])
        vertlist.append(vertcolumn)
        vertcolumn = []
    return vertlist


def transcribe(vertlist):
    horzlist = []
    horzrow = []
    for x in range(0, 5):
        for y in range(0, 5):
            horzrow.append((vertlist[y][x]))
        horzlist.append(horzrow)
        horzrow = []
    return horzlist


def how_to_move_l_and_r(FOCUSX, FOCUSY):
    print_it_up(FOCUSX, FOCUSY)
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


def movecounter(movecount):
    movecount += 1
    return movecount


class Tile(pg.sprite.Sprite):
    def __init__(self, total, FOCUSX, FOCUSY):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.FOCUSX = FOCUSX
        self.FOCUSY = FOCUSY
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.myarray = total

    def update(self):
        self.rect.x = self.rect.x - 32


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
            FOCUSX = focus_left(FOCUSX, FOCUSY)
            tile = Tile(total, FOCUSX, FOCUSY)
            all_sprites.add(tile)

        elif keystate[pg.K_RIGHT]:
            FOCUSX = focus_right(FOCUSX, FOCUSY)

        elif keystate[pg.K_UP]:
            FOCUSY = focus_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_DOWN]:
            FOCUSY = focus_down(FOCUSX, FOCUSY)

        elif keystate[pg.K_a or pg.K_A]:
            movecount = movecounter(movecount)
            countitup = total[FOCUSY].pop(0)
            total[FOCUSY].append(countitup)
            print_it_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_d or pg.K_D]:
            movecount = movecounter(movecount)
            countitup = total[FOCUSY].pop(-1)
            total[FOCUSY].insert(0, countitup)
            print_it_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_w or pg.K_W]:
            movecount = movecounter(movecount)
            vertlist = get_vert(FOCUSX, FOCUSY)
            countitup = vertlist[FOCUSX].pop(0)
            vertlist[FOCUSX].append(countitup)
            horizontal_again = transcribe(vertlist)
            total = horizontal_again
            print_it_up(FOCUSX, FOCUSY)


        elif keystate[pg.K_s or pg.K_S]:
            movecount = movecounter(movecount)
            vertlist = get_vert(FOCUSX, FOCUSY)
            countitup = vertlist[FOCUSX].pop(-1)
            vertlist[FOCUSX].insert(0, countitup)
            horizontal_again = transcribe(vertlist)
            total = horizontal_again
            print_it_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_q or pg.K_Q]:
            movecount = movecounter(movecount)
            rot_counterclock(FOCUSX, FOCUSY)


        elif keystate[pg.K_e or pg.K_E]:
            movecount = movecounter(movecount)
            rot_clock(FOCUSX, FOCUSY)

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
