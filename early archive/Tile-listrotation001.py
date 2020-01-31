'''
Progress - created a swipe left and right system that works - probably can get a vertical version.
create random 2D array width x height


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


def rot_clock():
    pass


def rot_counterclock():
    pass


def print_it_up(FOCUSX, FOCUSY):
    # print('current focus is ' + "x:" + str(focus_x) + " y:" + str(focus_y))
    for i in range(3):
        print("")

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
    for i in range(8):
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

        elif keystate[pg.K_RIGHT]:
            FOCUSX = focus_right(FOCUSX, FOCUSY)

        elif keystate[pg.K_UP]:
            FOCUSY = focus_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_DOWN]:
            FOCUSY = focus_down(FOCUSX, FOCUSY)

        elif keystate[pg.K_a or pg.K_A]:
            countitup = total[FOCUSY].pop(0)
            total[FOCUSY].append(countitup)
            print_it_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_d or pg.K_D]:
            countitup = total[FOCUSY].pop(-1)
            total[FOCUSY].insert(0, countitup)
            print_it_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_w or pg.K_W]:
            vertlist = get_vert(FOCUSX, FOCUSY)
            countitup = vertlist[FOCUSX].pop(0)
            vertlist[FOCUSX].append(countitup)
            horizontal_again = transcribe(vertlist)
            total = horizontal_again
            print_it_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_s or pg.K_S]:
            vertlist = get_vert(FOCUSX, FOCUSY)
            countitup = vertlist[FOCUSX].pop(-1)
            vertlist[FOCUSX].insert(0, countitup)
            horizontal_again = transcribe(vertlist)
            total = horizontal_again
            print_it_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_q or pg.K_Q]:
            pass

        elif keystate[pg.K_e or pg.K_E]:
            pass

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
