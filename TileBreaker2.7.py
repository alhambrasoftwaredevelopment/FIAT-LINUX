import random
import pygame as pg
from settings import *
from os import path

pg.init()
pg.font.init()
title_font = pg.font.SysFont('Tahoma', int(35))
game_font = pg.font.SysFont('Tahoma', int(20))
screen = pg.display.set_mode((WIDTH, HEIGHT))


def get_high_score():
    high_score_file = open("high_score.txt", "r")
    best_score = (high_score_file.read())
    best_score = int(best_score)
    return best_score


def save_high_score(bestscore, movecount):
    try:
        if bestscore < movecount:
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(bestscore))
            high_score_file.close()
        else:
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(movecount))
            high_score_file.close()
    except IOError:
        print("Unable to save the high score.")


def focus(focus_x, focus_y):
    return focus_x, focus_y


def focus_left(focus_x, focus_y):
    if focus_x > 0:
        focus_x -= 1
    focus(focus_x, focus_y)
    pg.time.delay(100)
    return focus_x


def focus_right(focus_x, focus_y):
    if focus_x < ARRAY_WIDTH - 1:
        focus_x += 1
    focus(focus_x, focus_y)
    pg.time.delay(100)
    return focus_x


def focus_up(focus_x, focus_y):
    if focus_y > 0:
        focus_y -= 1
    focus(focus_x, focus_y)
    pg.time.delay(100)
    return focus_y


def focus_down(focus_x, focus_y):
    if focus_y < ARRAY_HEIGHT - 1:
        focus_y += 1
    focus(focus_x, focus_y)
    pg.time.delay(100)
    return focus_y


def rot_clock(total, focus_x, focus_y, move_count):
    start_x = focus_x
    start_y = focus_y

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


def rot_counterclock(total, focus_x, focus_y, move_count):
    move_count = move_count + 1
    rotate_counter = True
    bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
    total[start_y + 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest
    bitstobeadded = total[start_y - 1].pop(start_x - 1)  # moving a piece from northwest to west
    total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west
    bitstobeadded = total[start_y].pop(start_x + 1)
    total[start_y - 1].insert(start_x + 1, bitstobeadded)
    bitstobeadded = total[start_y + 1].pop(start_x + 2)
    total[start_y].insert(start_x + 1, bitstobeadded)
    movecounter(move_count)
    return total, rotate_counter


def get_vert(focus_x, focus_y):
    vertlist = []
    vertcolumn = []
    for x in range(0, ARRAY_WIDTH):
        for y in range(0, ARRAY_HEIGHT):
            vertcolumn.append(total[y][x])
        vertlist.append(vertcolumn)
        vertcolumn = []
    return vertlist


def transcribe(vert_list):
    horz_list = []
    horz_row = []
    for x in range(0, ARRAY_WIDTH):
        for y in range(0, ARRAY_HEIGHT):
            horz_row.append((vert_list[y][x]))
        horz_list.append(horz_row)
        horz_row = []
    return horz_list


def health_bar(total):
    health = 0
    DELT_TOT = []
    for l in range(ARRAY_WIDTH):
        for w in range(ARRAY_HEIGHT):
            numcheck = total[w][l]
            nummod = numcheck % 5
            nummod = abs(nummod - l) % 3
            num = nummod
            DELT_TOT.append((num))
    for l in range(ARRAY_WIDTH):
        for w in range(ARRAY_HEIGHT):
            numcheck = total[l][w]
            nummod = numcheck % 5
            nummod = abs(nummod - l) % 3
            num = nummod
            DELT_TOT.append((num))
    health = sum(DELT_TOT)

    return health


def draw_health_bar(screen, x, y, health):
    BAR_LENGTH = health * 5
    BAR_HEIGHT = 15
    fill = (health * 5)
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    pg.draw.rect(screen, DARK_GREEN, fill_rect)
    pg.draw.rect(screen, GREEN, outline_rect, 1)


def solve(total):


    shortest_delta_so_far = 100
    best_move = []
    DELTAS_LIST = []
    FOCUS_X = 0
    FOCUS_X = 0


def movecounter(move_count):
    move_count += 1
    return move_count


def draw_elements():
    pg.draw.rect(screen, DARK_GRAY, (OFFSET, OFFSET + 3, GAMEBOARD_WIDTH + OFFSET, HEIGHT - (2 * OFFSET)), 5)
    pg.draw.line(screen, DARK_GREEN, (new_x + OFFSET_II, GAMEBOARD_INSET), (new_x + OFFSET_II, HEIGHT - 100), 5)
    pg.draw.line(screen, DARK_GREEN, (GAMEBOARD_INSET + 15, new_y + OFFSET_III), (WIDTH - 365, new_y + OFFSET_III), 5)

    looper = 0
    for x in range(0, ARRAY_WIDTH):
        for y in range(0, ARRAY_HEIGHT):
            # print("count: {} x: {} y:{}".format(looper, x * GRID_SIZE, y * GRID_SIZE))
            looper = looper + 1
            tile_surface = game_font.render('{:02d}'.format(total[y][x]), False,
                                            (255, 255, 255))
            pg.draw.circle(screen, DARK_GRAY, (x * GRID_SIZE + OFFSET_II, y * GRID_SIZE + OFFSET_III), 24, 1)
            screen.blit(tile_surface, (x * GRID_SIZE + OFFSET_II - 10, y * GRID_SIZE + OFFSET_III - 12))
    pg.draw.circle(screen, DARK_GREEN, (new_x + GAMEBOARD_INSET_II, new_y + GAMEBOARD_INSET), 35, 4)
    for x in range(70, 451, TILESIZE):
        pg.draw.line(screen, DARK_GRAY, (x + 11, 64), (x + 11, HEIGHT - 56))
    for y in range(60, 441, TILESIZE):
        pg.draw.line(screen, DARK_GRAY, (80, y + 3), (WIDTH - 340, y + 3))
    score_write = game_font.render('MOVE COUNT: {}'.format(move_count), False, (255, 255, 255))
    screen.blit(score_write, (WIDTH - 260, HEIGHT / 4))
    high_score_write = game_font.render('RECORD SCORE: {}'.format(best_score), False, (255, 255, 255))
    screen.blit(high_score_write, (WIDTH - 260, HEIGHT - HEIGHT / 6))
    title = title_font.render('TILE BREAKER', False, (255, 255, 255))
    screen.blit(title, (WIDTH - 260, HEIGHT / 12))
    completion_rate = game_font.render('COMPLETION RATE:', False, (255, 255, 255))
    screen.blit(completion_rate, (WIDTH - 260, HEIGHT / 3))
    time_counter = game_font.render('TIME:{:02d} {:02d} secs'.format(round(counting_minutes), round(counting_seconds)),
                                    False, (255, 255, 255))
    screen.blit(time_counter, (WIDTH - 260, HEIGHT - HEIGHT / 4))


background = pg.image.load('circuit.jpg').convert()
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
    health = solve(total)
    clock.tick(FPS)
    counting_time = pg.time.get_ticks() - start_time
    game_time = counting_time / 1000
    counting_minutes = game_time / 120
    counting_seconds = game_time % 60

    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        key_state = pg.key.get_pressed()

        if key_state[pg.K_LEFT]:
            focus_x = focus_left(focus_x, focus_y)

        elif key_state[pg.K_RIGHT]:
            focus_x = focus_right(focus_x, focus_y)

        elif key_state[pg.K_UP]:
            focus_y = focus_up(focus_x, focus_y)

        elif key_state[pg.K_DOWN]:
            focus_y = focus_down(focus_x, focus_y)

        elif key_state[pg.K_a or pg.K_A]:
            def left():
                pull_left = True
                count_it_up = total[focus_y].pop(0)
                total[focus_y].append(count_it_up)


            left()



        elif key_state[pg.K_d or pg.K_D]:
            pull_right = True
            move_count = movecounter(move_count)
            count_it_up = total[focus_y].pop(-1)
            total[focus_y].insert(0, count_it_up)

        elif key_state[pg.K_w or pg.K_W]:
            pull_up = True
            vert_list = get_vert(focus_x, focus_y)
            count_it_up = vert_list[focus_x].pop(0)
            vert_list[focus_x].append(count_it_up)
            horizontal_again = transcribe(vert_list)
            total = horizontal_again

        elif key_state[pg.K_s or pg.K_S]:
            pull_down = True
            move_count = movecounter(move_count)
            vert_list = get_vert(focus_x, focus_y)
            count_it_up = vert_list[focus_x].pop(-1)
            vert_list[focus_x].insert(0, count_it_up)
            horizontal_again = transcribe(vert_list)
            total = horizontal_again


        elif key_state[pg.K_q or pg.K_Q]:
            start_x = focus_x
            start_y = focus_y
            if start_x >= 1 and start_x <= ARRAY_WIDTH - 2 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 2:
                rot_counterclock(total, focus_x, focus_y, move_count)
                move_count = move_count + 1
                rotate_clock = True

        elif key_state[pg.K_e or pg.K_E]:
            start_x = focus_x
            start_y = focus_y
            if start_x >= 1 and start_x <= ARRAY_WIDTH - 2 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 2:
                rot_clock(total, focus_x, focus_y, move_count)
                move_count = move_count + 1
                rotate_clock = True

        elif key_state[pg.K_m or pg.K_M]:
            solve(total)

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    if rotate_clock or rotate_counter == True:
        pg.draw.circle(screen, DARK_GREEN, (new_x + GAMEBOARD_INSET_II, new_y + GAMEBOARD_INSET), 100, 25)
    if pull_left == True:
        pg.draw.line(screen, DARK_GREEN, (50, new_y + GAMEBOARD_INSET),
                     (new_x + GAMEBOARD_INSET_II, new_y + GAMEBOARD_INSET), 25)
    if pull_right == True:
        pg.draw.line(screen, DARK_GREEN, (new_x + GAMEBOARD_INSET + 15, new_y + GAMEBOARD_INSET),
                     (WIDTH - 300, new_y + GAMEBOARD_INSET), 25)
    if pull_up == True:
        pg.draw.line(screen, DARK_GREEN, (new_x + GAMEBOARD_INSET + 20, 50),
                     (new_x + GAMEBOARD_INSET + 20, new_y + GAMEBOARD_INSET), 25)
    if pull_down == True:
        pg.draw.line(screen, DARK_GREEN, (new_x + GAMEBOARD_INSET + 20, new_y + GAMEBOARD_INSET),
                     (new_x + GAMEBOARD_INSET + 20, HEIGHT - 50), 25)

    GRID_LOC_X = focus_x * GRID_SIZE
    GRID_LOC_Y = focus_y * GRID_SIZE
    new_x = GRID_LOC_X
    new_y = GRID_LOC_Y
    health = health_bar(total)
    draw_health_bar(screen, WIDTH - 260, HEIGHT / 2.35, health)

    if MASTER_ARRAY == total:
        if move_count < best_score:
            score_write = game_font.render('You set high score.'
                                           'the old best score was{} '
                                           'and now its {}'.format(best_score, move_count), False, (255, 255, 255))
            screen.blit(score_write, (WIDTH / 2, HEIGHT / 2))

            save_high_score(best_score, move_count)
            break
        else:
            score_write = game_font.render('Good game! {} is a decent score'.format(move_count), False, (255, 255, 255))
            screen.blit(score_write, (WIDTH / 2, HEIGHT / 2))

    draw_elements()

    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
