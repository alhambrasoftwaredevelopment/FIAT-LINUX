'''
Progress - created a swipe left and right system that works - probably can get a vertical version.
create random 2D array width x height
add a move counter
add a "solver that compares with how far you are from solving
make the game have expandable size
corner moves that don't rotate still cost a move point  - izzy


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


def get_high_score():
    high_score_file = open("early archive/high_score.txt", "r")
    bestscore = int(high_score_file.read())
    high_score_file.close()
    print("The high score is", bestscore)
    return bestscore


def save_high_score(bestscore, movecount):
    try:
        if bestscore < movecount:
            # Write the file to disk
            high_score_file = open("early archive/high_score.txt", "w")
            high_score_file.write(str(bestscore))
            high_score_file.close()
        else:
            high_score_file = open("early archive/high_score.txt", "w")
            high_score_file.write(str(movecount))
            high_score_file.close()

    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")


# Get the high score
bestscore = get_high_score()

'''
# Get the score from the current game
current_score = 0
try:
    # Ask the user for his/her score
    current_score = int(input("What is your score? "))
except ValueError:
    # Error, can't turn what they typed into a number
    print("I don't understand what you typed.")

# See if we have a new high score
if current_score > high_score:
    # We do! Save to disk
    print("Yea! New high score!")
    save_high_score(current_score)
else:
    print("Better luck next time.")
'''


def focus(FOCUSX, FOCUS_Y):
    return FOCUSX, FOCUS_Y


def focus_left(FOCUS_X, FOCUS_Y):
    if FOCUS_X > 0:
        FOCUS_X -= 1
    focus(FOCUS_X, FOCUS_Y)
    pg.time.delay(100)
    return FOCUS_X


def focus_right(FOCUS_X, FOCUS_Y):
    if FOCUS_X < 4:
        FOCUS_X += 1
    focus(FOCUS_X, FOCUS_Y)
    pg.time.delay(100)
    return FOCUS_X


def focus_up(FOCUS_X, FOCUS_Y):
    if FOCUS_Y > 0:
        FOCUS_Y -= 1
    focus(FOCUS_X, FOCUS_Y)
    pg.time.delay(100)
    return FOCUS_Y


def focus_down(FOCUS_X, FOCUS_Y):
    if FOCUS_Y < 4:
        FOCUS_Y += 1
    focus(FOCUS_X, FOCUS_Y)
    pg.time.delay(100)
    return FOCUS_Y


def rot_clock(total, FOCUS_X, FOCUS_Y):
    start_x = FOCUS_X
    start_y = FOCUS_Y

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


def rot_counterclock(total, FOCUS_X, FOCUS_Y):
    start_x = FOCUS_X
    start_y = FOCUS_Y

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


def print_it_up(FOCUS_X, FOCUS_Y):
    for i in range(PRINTBUFFER):
        print("")
    print('current focus: x={}, y={}'.format(FOCUS_X, FOCUS_Y))
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


def get_vert(FOCUS_X, FOCUS_Y):
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


def class_grid(total, WIDTH, HEIGHT, GRID_SIZE):
    anum = 1
    for xloc in range(0, WIDTH, GRID_SIZE):
        for yloc in range(0, HEIGHT, GRID_SIZE):
            tile = Tile(anum, total, xloc, yloc)
            anum = anum + 1
            all_sprites.add(tile)


def solve(total):
    DELTAS_LIST = []
    for x in range(5):
        for y in range(5):
            num = abs(MASTER_LIST[x][y] - total[x][y])
            DELTASLIST.append(num)

    print(MASTER_LIST)
    print(total)
    print(DELTASLIST)


'''
def health_bar():
    DELTASLIST = []
    for x in range(5):
        for y in range(5):
            num = abs(MASTER_LIST[x][y] - total[x][y])
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
'''

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

            FOCUS_X = focus_left(FOCUS_X, FOCUS_Y)


        elif keystate[pg.K_RIGHT]:
            FOCUS_X = focus_right(FOCUS_X, FOCUS_Y)

        elif keystate[pg.K_UP]:
            FOCUS_Y = focus_up(FOCUS_X, FOCUS_Y)

        elif keystate[pg.K_DOWN]:
            FOCUS_Y = focus_down(FOCUS_X, FOCUS_Y)

        elif keystate[pg.K_a or pg.K_A]:
            pull_left = True
            movecount = movecounter(move_count)
            countitup = total[FOCUS_Y].pop(0)
            total[FOCUS_Y].append(countitup)


        elif keystate[pg.K_d or pg.K_D]:
            pull_right = True
            movecount = movecounter(move_count)
            countitup = total[FOCUS_Y].pop(-1)
            total[FOCUS_Y].insert(0, countitup)


        elif keystate[pg.K_w or pg.K_W]:
            pull_up = True
            movecount = movecounter(move_count)
            vertlist = get_vert(FOCUS_X, FOCUS_Y)
            countitup = vertlist[FOCUS_X].pop(0)
            vertlist[FOCUS_X].append(countitup)
            horizontal_again = transcribe(vertlist)
            total = horizontal_again



        elif keystate[pg.K_s or pg.K_S]:
            pull_down = True
            movecount = movecounter(move_count)
            vertlist = get_vert(FOCUS_X, FOCUS_Y)
            countitup = vertlist[FOCUS_X].pop(-1)
            vertlist[FOCUS_X].insert(0, countitup)
            horizontal_again = transcribe(vertlist)
            total = horizontal_again


        elif keystate[pg.K_q or pg.K_Q]:
            movecount = movecounter(move_count)
            rot_counterclock(total, FOCUS_X, FOCUS_Y)
            rotate_clock = True



        elif keystate[pg.K_e or pg.K_E]:
            movecount = movecounter(move_count)
            rot_clock(total, FOCUS_X, FOCUS_Y)
            rotate_clock = True

        elif keystate[pg.K_m or pg.K_M]:
            solve(total)

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    GRIDLOCX = FOCUS_X * GRID_SIZE
    GRIDLOCY = FOCUS_Y * GRID_SIZE
    NEWX = GRIDLOCX
    NEWY = GRIDLOCY
    if MASTER_LIST == total:
        save_high_score(bestscore, move_count)
        break

    if rotate_clock or rotate_counter == True:
        pg.draw.circle(screen, GREEN, (NEWX + 37, NEWY + 37), 120, 5)
    if pull_left == True:
        pg.draw.line(screen, GREEN, (0, NEWY + OFFSET), (NEWX + OFFSET, NEWY + OFFSET), 5)
        pg.draw.line(screen, GREEN, (0, NEWY + OFFSET_II), (NEWX + OFFSET, NEWY + OFFSET_II), 5)
    if pull_right == True:
        pg.draw.line(screen, GREEN, (NEWX + OFFSET, NEWY + OFFSET), (WIDTH, NEWY + OFFSET), 5)
        pg.draw.line(screen, GREEN, (NEWX + OFFSET, NEWY + OFFSET_II), (WIDTH, NEWY + OFFSET_II), 5)
    if pull_up == True:
        pg.draw.line(screen, GREEN, (NEWX + OFFSET, 0), (NEWX + OFFSET, NEWY + OFFSET), 5)
        pg.draw.line(screen, GREEN, (NEWX + OFFSET_II, 0), (NEWX + OFFSET_II, NEWY + OFFSET), 5)

    if pull_down == True:
        pg.draw.line(screen, GREEN, (NEWX + OFFSET, NEWY + OFFSET), (NEWX + OFFSET, HEIGHT), 5)
        pg.draw.line(screen, GREEN, (NEWX + OFFSET_II, NEWY + OFFSET), (NEWX + OFFSET_II, HEIGHT), 5)
    # health = health_bar()
    # draw_health_bar(screen, width - 250, height - 30, health)

    pg.draw.line(screen, DARK_GRAY, (NEWX + OFFSET, 0), (NEWX + OFFSET, HEIGHT), 1)
    pg.draw.line(screen, DARK_GRAY, (NEWX + OFFSET_II, 0), (NEWX + OFFSET_II, HEIGHT), 1)
    pg.draw.line(screen, DARK_GRAY, (0, NEWY + OFFSET), (WIDTH, NEWY + OFFSET), 1)
    pg.draw.line(screen, DARK_GRAY, (0, NEWY + OFFSET_II), (WIDTH, NEWY + OFFSET_II), 1)
    for x in range(0, 5):
        for y in range(0, 5):
            tile_surface = game_font.render('{:02d}'.format(total[y][x]), False,
                                            (255, 255, 255))
            pg.draw.circle(screen, DARK_GRAY, (x * GRID_SIZE + 38, y * GRID_SIZE + 37), 30, 5)
            screen.blit(tile_surface, (x * GRID_SIZE + 25, y * GRID_SIZE + 20))
    pg.draw.circle(screen, GREEN, (NEWX + 37, NEWY + 37), 25, 4)
    score_write = game_font.render('Move count: {}'.format(move_count), False, (255, 255, 255))
    screen.blit(score_write, (20, HEIGHT - 40))
    high_score_write = game_font.render('highscore: {}'.format(bestscore), False, (255, 255, 255))
    screen.blit(high_score_write, (120, HEIGHT - 120))
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
