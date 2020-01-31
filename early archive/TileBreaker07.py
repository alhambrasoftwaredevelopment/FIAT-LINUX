'''
Progress - created a swipe left and right system that works - probably can get a vertical version.
create random 2D array width x height
add a move counter
add a "solver that compares with how far you are from solving
make the game have expandable size


'''
print("welcome to the Tile game")
print("arrow keys change focus")
print("WADS keys move rows and columns")
print("Q and E rotate around focus")
import random

import pygame as pg
from settings import *
from os import path

pg.init()
pg.font.init()
game_font = pg.font.SysFont('Tahoma', 25)
screen = pg.display.set_mode((WIDTH, HEIGHT))


def focus(FOCUSX, FOCUSY):
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


def rot_clock(total, FOCUSX, FOCUSY):
    start_x = FOCUSX
    start_y = FOCUSY

    try:
        if start_x >= 1 and start_x <= ARRAY_WIDTH - 1 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 1:
            rotate_counter = True
            bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
            total[start_y - 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest

            bitstobeadded = total[start_y + 1].pop(start_x - 1)  # moving a piece from northwest to west
            total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west

            bitstobeadded = total[start_y].pop(start_x + 1)
            total[start_y + 1].insert(start_x + 1, bitstobeadded)

            bitstobeadded = total[start_y - 1].pop(start_x + 2)
            total[start_y].insert(start_x + 1, bitstobeadded)
            return total, rotate_counter
    except:
        return total


def rot_counterclock(total, FOCUSX, FOCUSY):
    start_x = FOCUSX
    start_y = FOCUSY

    try:
        if start_x >= 1 and start_x <= ARRAY_WIDTH - 1 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 1:
            rotate_counter = True
            bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
            total[start_y + 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest
            bitstobeadded = total[start_y - 1].pop(start_x - 1)  # moving a piece from northwest to west
            total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west
            bitstobeadded = total[start_y].pop(start_x + 1)
            total[start_y - 1].insert(start_x + 1, bitstobeadded)
            bitstobeadded = total[start_y + 1].pop(start_x + 2)
            total[start_y].insert(start_x + 1, bitstobeadded)
            return total, rotate_counter
    except:
        return total


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


def movecounter(movecount):
    movecount += 1
    return movecount


def class_grid(total, WIDTH, HEIGHT, GRIDSIZE):
    anum = 1
    for xloc in range(0, WIDTH, GRIDSIZE):
        for yloc in range(0, HEIGHT, GRIDSIZE):
            tile = Tile(anum, total, xloc, yloc)
            anum = anum + 1
            all_sprites.add(tile)


def solve(total):
    DELTASLIST = []
    for x in range(5):
        for y in range(5):
            num = abs(MASTERLIST[x][y] - total[x][y])
            DELTASLIST.append(num)

    print(MASTERLIST)
    print(total)
    print(DELTASLIST)


def health_bar():
    DELTASLIST = []
    for x in range(5):
        for y in range(5):
            num = abs(MASTERLIST[x][y] - total[x][y])
            DELTASLIST.append(num)
    health = sum(DELTASLIST)

    return health


def draw_health_bar(screen, x, y, health):
    if health < 0:
        health = 0
    BAR_LENGTH = health
    BAR_HEIGHT = 15
    fill = (health)
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if BAR_LENGTH > 120:
        fill = 120
    pg.draw.rect(screen, GREEN, fill_rect)
    pg.draw.rect(screen, WHITE, outline_rect, 2)


all_sprites = pg.sprite.Group()
pg.display.set_caption("Tile Break 2020")
clock = pg.time.Clock()

running = True
while running:
    rotate_counter = False
    rotate_clock = False
    pull_down = False
    pull_up = False
    pull_left = False
    pull_right = False

    clock.tick(FPS)
    # class_grid(total, width,height,GRIDSIZE)
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
            pull_left = True
            movecount = movecounter(movecount)
            countitup = total[FOCUSY].pop(0)
            total[FOCUSY].append(countitup)


        elif keystate[pg.K_d or pg.K_D]:
            pull_right = True
            movecount = movecounter(movecount)
            countitup = total[FOCUSY].pop(-1)
            total[FOCUSY].insert(0, countitup)


        elif keystate[pg.K_w or pg.K_W]:
            pull_up = True
            movecount = movecounter(movecount)
            vertlist = get_vert(FOCUSX, FOCUSY)
            countitup = vertlist[FOCUSX].pop(0)
            vertlist[FOCUSX].append(countitup)
            horizontal_again = transcribe(vertlist)
            total = horizontal_again



        elif keystate[pg.K_s or pg.K_S]:
            pull_down = True
            movecount = movecounter(movecount)
            vertlist = get_vert(FOCUSX, FOCUSY)
            countitup = vertlist[FOCUSX].pop(-1)
            vertlist[FOCUSX].insert(0, countitup)
            horizontal_again = transcribe(vertlist)
            total = horizontal_again


        elif keystate[pg.K_q or pg.K_Q]:
            movecount = movecounter(movecount)
            rot_counterclock(total, FOCUSX, FOCUSY)
            rotate_clock = True



        elif keystate[pg.K_e or pg.K_E]:
            movecount = movecounter(movecount)
            rot_clock(total, FOCUSX, FOCUSY)
            rotate_clock = True

        elif keystate[pg.K_m or pg.K_M]:
            solve(total)

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    for x in range(0, 5):
        for y in range(0, 5):
            tile_surface = game_font.render('{:02d}'.format(total[y][x]), False,
                                            (255, 255, 255))
            screen.blit(tile_surface, (x * GRIDSIZE + 25, y * GRIDSIZE + 20))

    GRIDLOCX = FOCUSX * GRIDSIZE
    GRIDLOCY = FOCUSY * GRIDSIZE
    NEWX = GRIDLOCX
    NEWY = GRIDLOCY

    pg.draw.circle(screen, GREEN, (NEWX + 37, NEWY + 37), 25, 2)
    if rotate_clock or rotate_counter == True:
        pg.draw.circle(screen, GREEN, (NEWX + 37, NEWY + 37), 150, 2)
    if pull_left == True:
        pg.draw.line(screen, GREEN, (0, NEWY + OFFSET), (NEWX + OFFSET, NEWY + OFFSET), 2)
        pg.draw.line(screen, GREEN, (0, NEWY + OFFSETII), (NEWX + OFFSET, NEWY + OFFSETII), 2)
    if pull_right == True:
        pg.draw.line(screen, GREEN, (NEWX + OFFSET, NEWY + OFFSET), (WIDTH, NEWY + OFFSET), 2)
        pg.draw.line(screen, GREEN, (NEWX + OFFSET, NEWY + OFFSETII), (WIDTH, NEWY + OFFSETII), 2)
    if pull_up == True:
        pg.draw.line(screen, GREEN, (NEWX + OFFSET, 0), (NEWX + OFFSET, NEWY + OFFSET), 2)
        pg.draw.line(screen, GREEN, (NEWX + OFFSETII, 0), (NEWX + OFFSETII, NEWY + OFFSET), 2)

    if pull_down == True:
        pg.draw.line(screen, GREEN, (NEWX + OFFSET, NEWY + OFFSET), (NEWX + OFFSET, HEIGHT), 2)
        pg.draw.line(screen, GREEN, (NEWX + OFFSETII, NEWY + OFFSET), (NEWX + OFFSETII, HEIGHT), 2)
    health = health_bar()
    draw_health_bar(screen, WIDTH - 250, HEIGHT - 30, health)

    pg.draw.line(screen, DARK_GRAY, (NEWX + OFFSET, 0), (NEWX + OFFSET, HEIGHT), 1)
    pg.draw.line(screen, DARK_GRAY, (NEWX + OFFSETII, 0), (NEWX + OFFSETII, HEIGHT), 1)
    pg.draw.line(screen, DARK_GRAY, (0, NEWY + OFFSET), (WIDTH, NEWY + OFFSET), 1)
    pg.draw.line(screen, DARK_GRAY, (0, NEWY + OFFSETII), (WIDTH, NEWY + OFFSETII), 1)
    score_write = game_font.render('Move count: {}'.format(movecount), False, (255, 255, 255))
    screen.blit(score_write, (20, HEIGHT - 40))
    # *after* drawing everything, flip the display
    pg.display.flip()
pg.quit()
