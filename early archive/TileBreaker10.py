'''

add a "solver that compares with how far you are from solving
make the game have expandable size
corner moves that don't rotate still cost a move point  - izzy

'''

import random
import pygame as pg
from settings import *
from os import path

pg.init()
pg.font.init()
title_font = pg.font.SysFont('Tahoma', 40)
game_font = pg.font.SysFont('NewTimesRoman', 25)
screen = pg.display.set_mode((WIDTH, HEIGHT))


def get_high_score():
    high_score_file = open("early archive/high_score.txt", "r")
    best_score = int(high_score_file.read())
    high_score_file.close()
    return best_score


def save_high_score(bestscore, movecount):
    try:
        if bestscore < movecount:
            high_score_file = open("early archive/high_score.txt", "w")
            high_score_file.write(str(bestscore))
            high_score_file.close()
        else:
            high_score_file = open("early archive/high_score.txt", "w")
            high_score_file.write(str(movecount))
            high_score_file.close()
    except IOError:
        print("Unable to save the high score.")


def focus(FOCUS_X, FOCUS_Y):
    return FOCUS_X, FOCUS_Y


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


def print_it_up(FOCUS_X, FOCUSY):
    for i in range(PRINTBUFFER):
        print("")
    print('current focus: x={}, y={}'.format(FOCUS_X, FOCUSY))
    print('move count: {}'.format(movecount))
    if FOCUS_X == 0:
        print("     v")
    elif FOCUS_X == 1:
        print("         v")
    elif FOCUS_X == 2:
        print("              v")
    elif FOCUS_X == 3:
        print("                   v")
    elif FOCUS_X == 4:
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
    if FOCUS_X == 0:
        print("     ^")
    elif FOCUS_X == 1:
        print("         ^")
    elif FOCUS_X == 2:
        print("              ^")
    elif FOCUS_X == 3:
        print("                   ^")
    elif FOCUS_X == 4:
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


def transcribe(vert_list):
    horz_list = []
    horz_row = []
    for x in range(0, 5):
        for y in range(0, 5):
            horz_row.append((vert_list[y][x]))
        horz_list.append(horz_row)
        horz_row = []
    return horz_list


def movecounter(move_count):
    move_count += 1
    return move_count


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
            DELTAS_LIST.append(num)

    print(MASTER_LIST)
    print(total)
    print(DELTAS_LIST)


def health_bar():
    DELTA_SLIST = []
    for x in range(5):
        for y in range(5):
            num = abs(MASTER_LIST[x][y] - total[x][y])
            DELTA_SLIST.append(num)
    health = sum(DELTA_SLIST)

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
    pg.draw.rect(screen, DARK_GREEN, fill_rect)
    pg.draw.rect(screen, GREEN, outline_rect, 2)


def draw_elements():
    pass


background = pg.image.load('circuit.png').convert()
background_rect = background.get_rect()

best_score = get_high_score()
all_sprites = pg.sprite.Group()
pg.display.set_caption("Tile Break 2020")
clock = pg.time.Clock()
start_time = pg.time.get_ticks()
running = True
while running:
    rotate_counter = False
    rotate_clock = False
    pull_down = False
    pull_up = False
    pull_left = False
    pull_right = False

    clock.tick(FPS)
    counting_time = pg.time.get_ticks() - start_time
    game_time = counting_time / 1000
    counting_minutes = game_time / 120
    counting_seconds = game_time % 60

    # class_grid(total, width,height,GRIDSIZE)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        key_state = pg.key.get_pressed()

        if key_state[pg.K_LEFT]:
            FOCUS_X = focus_left(FOCUS_X, FOCUS_Y)

        elif key_state[pg.K_RIGHT]:
            FOCUS_X = focus_right(FOCUS_X, FOCUS_Y)

        elif key_state[pg.K_UP]:
            FOCUS_Y = focus_up(FOCUS_X, FOCUS_Y)

        elif key_state[pg.K_DOWN]:
            FOCUS_Y = focus_down(FOCUS_X, FOCUS_Y)

        elif key_state[pg.K_a or pg.K_A]:
            pull_left = True
            move_count = movecounter(move_count)
            count_it_up = total[FOCUS_Y].pop(0)
            total[FOCUS_Y].append(count_it_up)

        elif key_state[pg.K_d or pg.K_D]:
            pull_right = True
            move_count = movecounter(move_count)
            count_it_up = total[FOCUS_Y].pop(-1)
            total[FOCUS_Y].insert(0, count_it_up)

        elif key_state[pg.K_w or pg.K_W]:
            pull_up = True
            move_count = movecounter(move_count)
            vert_list = get_vert(FOCUS_X, FOCUS_Y)
            count_it_up = vert_list[FOCUS_X].pop(0)
            vert_list[FOCUS_X].append(count_it_up)
            horizontal_again = transcribe(vert_list)
            total = horizontal_again

        elif key_state[pg.K_s or pg.K_S]:
            pull_down = True
            move_count = movecounter(move_count)
            vert_list = get_vert(FOCUS_X, FOCUS_Y)
            count_it_up = vert_list[FOCUS_X].pop(-1)
            vert_list[FOCUS_X].insert(0, count_it_up)
            horizontal_again = transcribe(vert_list)
            total = horizontal_again

        elif key_state[pg.K_q or pg.K_Q]:
            move_count = movecounter(move_count)
            rot_counterclock(total, FOCUS_X, FOCUS_Y)
            rotate_clock = True

        elif key_state[pg.K_e or pg.K_E] and FOCUS_X > 1 and FOCUS_X < 5 and FOCUS_Y > 1 and FOCUS_Y < 5:
            move_count = movecounter(move_count)
            rot_clock(total, FOCUS_X, FOCUS_Y)
            rotate_clock = True

        elif key_state[pg.K_m or pg.K_M]:
            solve(total)

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    GRID_LOC_X = FOCUS_X * GRID_SIZE
    GRID_LOC_Y = FOCUS_Y * GRID_SIZE
    NEW_X = GRID_LOC_X
    NEW_Y = GRID_LOC_Y
    if MASTER_LIST == total:
        game_loop = False
        if move_count < best_score:
            score_write = game_font.render('You set high score.'
                                           'the old best score was{} '
                                           'and now its {}'.format(best_score, move_count), False, (255, 255, 255))
            screen.blit(score_write, (WIDTH / 2, HEIGHT / 2))

            save_high_score(best_score, move_count)
            break

    if rotate_clock or rotate_counter == True:
        pg.draw.circle(screen, GREEN, (NEW_X + 37, NEW_Y + 37), 150, 2)
    if pull_left == True:
        pg.draw.line(screen, GREEN, (0, NEW_Y + OFFSET), (NEW_X + OFFSET, NEW_Y + OFFSET), 5)
        pg.draw.line(screen, GREEN, (0, NEW_Y + OFFSET_II), (NEW_X + OFFSET, NEW_Y + OFFSET_II), 5)
    if pull_right == True:
        pg.draw.line(screen, GREEN, (NEW_X + OFFSET + 30, NEW_Y + OFFSET), (WIDTH, NEW_Y + OFFSET), 5)
        pg.draw.line(screen, GREEN, (NEW_X + OFFSET + 30, NEW_Y + OFFSET_II), (WIDTH, NEW_Y + OFFSET_II), 5)
    if pull_up == True:
        pg.draw.line(screen, GREEN, (NEW_X + OFFSET, 0), (NEW_X + OFFSET, NEW_Y + OFFSET), 5)
        pg.draw.line(screen, GREEN, (NEW_X + OFFSET_II, 0), (NEW_X + OFFSET_II, NEW_Y + OFFSET), 5)
    if pull_down == True:
        pg.draw.line(screen, GREEN, (NEW_X + OFFSET, NEW_Y + OFFSET + 30), (NEW_X + OFFSET, HEIGHT), 5)
        pg.draw.line(screen, GREEN, (NEW_X + OFFSET_II, NEW_Y + OFFSET + 30), (NEW_X + OFFSET_II, HEIGHT), 5)
    # health = health_bar()eee
    # draw_health_bar(screen, width - 300, height / 2.35, health)

    pg.draw.line(screen, DARK_GREEN, (NEW_X + OFFSET, 15), (NEW_X + OFFSET, HEIGHT - 40), 1)
    pg.draw.line(screen, DARK_GREEN, (NEW_X + OFFSET_II, 15), (NEW_X + OFFSET_II, HEIGHT - 40), 1)
    pg.draw.line(screen, DARK_GREEN, (25, NEW_Y + OFFSET), (WIDTH - 340, NEW_Y + OFFSET), 1)
    pg.draw.line(screen, DARK_GREEN, (25, NEW_Y + OFFSET_II), (WIDTH - 340, NEW_Y + OFFSET_II), 1)
    looper = 0
    for x in range(0, 5):

        for y in range(0, 5):
            print("count: {} x: {} y:{}".format(looper, x * GRID_SIZE + 38, y * GRID_SIZE + 38))
            looper = looper + 1
            tile_surface = game_font.render('{:02d}'.format(total[y][x]), False,
                                            (255, 255, 255))
            pg.draw.circle(screen, DARK_GRAY, (x * GRID_SIZE + 38, y * GRID_SIZE + 37), 30, 2)
            screen.blit(tile_surface, (x * GRID_SIZE + 25, y * GRID_SIZE + 20))
    pg.draw.circle(screen, GREEN, (NEW_X + 38, NEW_Y + 37), 35, 1)
    score_write = game_font.render('MOVE COUNT: {}'.format(move_count), False, (255, 255, 255))
    screen.blit(score_write, (WIDTH - 300, HEIGHT / 4))
    high_score_write = game_font.render('RECORD SCORE: {}'.format(best_score), False, (255, 255, 255))
    screen.blit(high_score_write, (WIDTH - 300, HEIGHT - HEIGHT / 6))
    title = title_font.render('TILE BREAKER', False, (255, 255, 255))
    screen.blit(title, (WIDTH - 300, HEIGHT / 30))
    completion_rate = game_font.render('COMPLETION RATE:', False, (255, 255, 255))
    screen.blit(completion_rate, (WIDTH - 300, HEIGHT / 3))
    time_counter = game_font.render('TIME:{:02d} {:02d} secs'.format(round(counting_minutes), round(counting_seconds)),
                                    False, (255, 255, 255))
    screen.blit(time_counter, (WIDTH - 300, HEIGHT - 150))

    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
