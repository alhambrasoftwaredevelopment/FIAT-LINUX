import random
import pygame as pg
from settings import *
from os import path
import cx_Freeze

pg.init()
pg.font.init()
title_font = pg.font.SysFont('Tahoma', int(35))
game_font = pg.font.SysFont('Tahoma', int(20))
screen = pg.display.set_mode((width, height))
shortest_delta_so_far = 100

img_dir = path.join(path.dirname(__file__), 'img')

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


def rot_clock(total, focus_x, focus_y):
    print (total)
    start_x = focus_x
    start_y = focus_y

    rotate_counter = True
    bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
    print(bitstobeadded)
    total[start_y - 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest
    bitstobeadded = total[start_y + 1].pop(start_x - 1)  # moving a piece from northwest to west
    print(bitstobeadded)
    total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west
    bitstobeadded = total[start_y].pop(start_x + 1)
    total[start_y + 1].insert(start_x + 1, bitstobeadded)
    print(bitstobeadded)
    bitstobeadded = total[start_y - 1].pop(start_x + 2)
    total[start_y].insert(start_x + 1, bitstobeadded)
    return total, rotate_counter


def rot_counterclock(total, focus_x, focus_y):
    print(total)
    start_x = focus_x
    start_y = focus_y

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
    DELT_TOT = []
    for w in range(5):
        for l in range(5):
            numcheck = total[w][l]
            numdif = numcheck % 5
            numvert = int(abs((numcheck - numdif) / 5 - w))
            if numvert > 2:
                numvert = 2
            if w == 0 and numcheck >= 20:
                numvert = 1
            if w == 4 and numcheck <= 4:
                numvert = 1
            nummod = numcheck % 5
            nunummod = abs(nummod - l) % 3
            DELT_TOT.append(nunummod)
            DELT_TOT.append(numvert)
    health = sum(DELT_TOT)
    return health



def draw_health_bar(screen, x, y, health):
    BAR_LENGTH = health *7
    BAR_HEIGHT = 25
    fill = (health * 7)
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if health > 30:
        pg.draw.rect(screen, RED, fill_rect)
        pg.draw.rect(screen, GREEN, outline_rect, 1)

    elif health > 10:
        pg.draw.rect(screen, YELLOW, fill_rect)
        pg.draw.rect(screen, GREEN, outline_rect, 1)

    else:
        pg.draw.rect(screen, GREEN, fill_rect)
        pg.draw.rect(screen, GREEN, outline_rect, 1)




def movecounter(move_count):
    move_count += 1
    return move_count


def draw_elements(GAMEBOARD_INSET_II):
    pg.draw.rect(screen, DARK_GRAY, (OFFSET, OFFSET + 3, GAMEBOARD_WIDTH + OFFSET, height - (2 * OFFSET)), 5)
    pg.draw.line(screen, DARK_GREEN, (new_x + OFFSET_II, GAMEBOARD_INSET), (new_x + OFFSET_II, height - 100), 5)
    pg.draw.line(screen, DARK_GREEN, (GAMEBOARD_INSET + 15, new_y + OFFSET_III), (width - 365, new_y + OFFSET_III), 5)

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
        pg.draw.line(screen, DARK_GRAY, (x + 11, 64), (x + 11, height - 56))
    for y in range(60, 441, TILESIZE):
        pg.draw.line(screen, DARK_GRAY, (80, y + 3), (width - 340, y + 3))
    score_write = game_font.render('MOVE COUNT: {}'.format(move_count), False, (255, 255, 255))
    screen.blit(score_write, (width - 260, height / 4))
    high_score_write = game_font.render('RECORD SCORE: {}'.format(best_score), False, (255, 255, 255))
    screen.blit(high_score_write, (width - 260, height - height / 6))
    title = title_font.render('TILE BREAKER', False, (255, 255, 255))
    screen.blit(title, (width - 260, height / 12))
    completion_rate = game_font.render('COMPLETION RATE:', False, (255, 255, 255))
    screen.blit(completion_rate, (width - 260, height / 3))



def up(total):
    vert_list = get_vert(focus_x, focus_y)
    count_it_up = vert_list[focus_x].pop(0)
    vert_list[focus_x].append(count_it_up)
    horizontal_again = transcribe(vert_list)
    total = horizontal_again
    return total


def down(total):
    vert_list = get_vert(focus_x, focus_y)
    count_it_up = vert_list[focus_x].pop(-1)
    vert_list[focus_x].insert(0, count_it_up)
    horizontal_again = transcribe(vert_list)
    total = horizontal_again
    return total

def left(total):
    count_it_up = total[focus_y].pop(0)
    total[focus_y].append(count_it_up)
    return total

def right(total):
    count_it_up = total[focus_y].pop(-1)
    total[focus_y].insert(0, count_it_up)
    return total



best_score = get_high_score()
all_sprites = pg.sprite.Group()
pg.display.set_caption("Tile Break 2020")
clock = pg.time.Clock()
start_time = pg.time.get_ticks()

welcome = pg.image.load(path.join(img_dir, 'welcome.jpg')).convert()
welcome_rect = welcome.get_rect()
background = pg.image.load(path.join(img_dir, 'circuit.jpg')).convert()
background_rect = background.get_rect()
paused = pg.image.load(path.join(img_dir, 'paused.jpg')).convert()
paused_rect = paused.get_rect()
info = pg.image.load(path.join(img_dir, 'info.jpg')).convert()
info_rect = info.get_rect()

game_img = welcome
game_rect = welcome_rect

running = True
current_game_state = 0
game_time = 0
pause_time = 0
running = True
while running:
    rotate_counter = False
    rotate_clock = False
    pull_down = False
    pull_up = False
    pull_left = False
    pull_right = False
    # health = solve(total)
    clock.tick(FPS)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        key_state = pg.key.get_pressed()
        if key_state[pg.K_n or pg.K_N]:
            """information screen"""
            current_game_state = 1

        if key_state[pg.K_i or pg.K_I]:
            """information screen"""
            where_you_come_from = current_game_state
            if current_game_state == 1 or current_game_state == 0:
                current_game_state = 3
                pause_time = game_time
            elif current_game_state == 3:
                current_game_state = 0

        if key_state[pg.K_ESCAPE]:
            """get completely out of the game"""
            pg.QUIT
            running == False
            current_game_state = 5

        if key_state[pg.K_SPACE]:
            """pause and unpause"""
            game_state_before_pause = current_game_state
            pg.time.delay(100)
            if current_game_state == 1:
                current_game_state = 4
                pause_time = game_time
            elif current_game_state == 4:
                current_game_state = 1

        if key_state[pg.K_LEFT]:
            focus_x = focus_left(focus_x, focus_y)

        if key_state[pg.K_RIGHT]:
            focus_x = focus_right(focus_x, focus_y)

        if key_state[pg.K_UP]:
            focus_y = focus_up(focus_x, focus_y)

        if key_state[pg.K_DOWN]:
            focus_y = focus_down(focus_x, focus_y)

        if key_state[pg.K_a or pg.K_A]:
            pull_left = True
            move_count = movecounter(move_count)
            total = left(total)


        if key_state[pg.K_d or pg.K_D]:
            pull_right = True
            move_count = movecounter(move_count)
            total = right(total)


        if key_state[pg.K_w or pg.K_W]:
            pull_up = True
            move_count = movecounter(move_count)
            total = up(total)


        if key_state[pg.K_s or pg.K_S]:
            pull_down = True
            move_count = movecounter(move_count)
            total = down(total)

        if key_state[pg.K_q or pg.K_Q]:
            start_x = focus_x
            start_y = focus_y
            if start_x >= 1 and start_x <= ARRAY_WIDTH - 2 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 2:
                rot_counterclock(total, focus_x, focus_y)
                move_count = move_count + 1
                rotate_clock = True

        if key_state[pg.K_e or pg.K_E]:
            start_x = focus_x
            start_y = focus_y
            move_count = move_count +1
            if start_x >= 1 and start_x <= ARRAY_WIDTH - 2 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 2:
                rot_clock(total, focus_x, focus_y)
                rotate_clock = True

        if key_state[pg.K_ESCAPE]:
            """get completely out of the game"""
            running == False
            break

        if key_state[pg.K_m or pg.K_M]:
            count_delts = 0
            best_delt = 0
            shortest_delta_so_far = 0
            DELT_TOT = []
            countdif = 0
            for w in range(5):
                for l in range(5):
                    numcheck = total[w][l]
                    numdif = numcheck % 5
                    numvert = int(abs((numcheck - numdif) / 5 - w))
                    if countdif == numcheck:
                        DELT_TOT.append(5)
                        print ('{} home'.format(total[w][l]))
                    countdif = countdif +1
                    if numvert > 2:
                        numvert = 2
                    if w == 0 and numcheck >= 20:
                        numvert = 1
                    if w == 4 and numcheck <= 4:
                        numvert = 1
                    nummod = numcheck % 5
                    nunummod = abs(nummod - l) % 3
                    DELT_TOT.append(nunummod)
                    DELT_TOT.append(numvert)
                    current_health = sum(DELT_TOT)
            focus_x = 0
            focus_y = 0
            pg.time.wait(100)
            for diagonal in range (5):
                for i in range (4):
                    DELT_TOT = []
                    if i == 0:
                        total = up(total)

                    if i == 1:
                        total = down(total)

                    if i == 2:
                        total = left(total)

                    if i == 3:
                        total = right(total)

                    for w in range(5):
                        for l in range(5):
                            numcheck = total[w][l]
                            numdif = numcheck % 5
                            numvert = int(abs((numcheck - numdif) / 5 - w))
                            if numvert > 2:
                                numvert = 2
                            if w == 0 and numcheck >= 20:
                                numvert = 1
                            if w == 4 and numcheck <= 4:
                                numvert = 1
                            nummod = numcheck % 5
                            nunummod = abs(nummod - l) % 3
                            DELT_TOT.append(nunummod)
                            DELT_TOT.append(numvert)
                            health = sum(DELT_TOT)
                    if i == 0:
                        down(total)
                    if i == 1:
                        up(total)
                    if i == 2:
                        right(total)
                    if i == 3:
                        left(total)
                    #         print('distance vert {}'.format(numvert))
                    #         print('item in x:{},y:{} = {} {} = hordelt '.format(w, l, numcheck, nunummod))
                    #         print('')
                    best_delt = abs(current_health - health)

                    if best_delt > shortest_delta_so_far:
                        best_list = []
                        best_list.append(best_delt)
                        best_list.append(focus_x)
                        best_list.append(focus_y)
                        best_list.append(i)
                        shortest_delta_so_far = best_delt
                        print(best_list)
                        DELT_TOT = []
                focus_x = focus_x +1
                focus_y = focus_y +1
            pg.time.wait(200)
            focus_y = 1

            for l in range (3):
                focus_x = 1
                for w in range (3):
                    DELT_TOT = []
                    start_x = focus_x
                    start_y = focus_y
                    rotate_counter = True
                    bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
                    total[start_y + 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest
                    bitstobeadded = total[start_y - 1].pop(start_x - 1)  # moving a piece from northwest to west
                    total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west
                    bitstobeadded = total[start_y].pop(start_x + 1)
                    total[start_y - 1].insert(start_x + 1, bitstobeadded)
                    bitstobeadded = total[start_y + 1].pop(start_x + 2)
                    total[start_y].insert(start_x + 1, bitstobeadded)
                    numcheck = total[w][l]
                    numdif = numcheck % 5
                    numvert = int(abs((numcheck - numdif) / 5 - w))
                    if numvert > 2:
                        numvert = 2
                    if w == 0 and numcheck >= 20:
                        numvert = 1
                    if w == 4 and numcheck <= 4:
                        numvert = 1
                    nummod = numcheck % 5
                    nunummod = abs(nummod - l) % 3
                    DELT_TOT.append(nunummod)
                    DELT_TOT.append(numvert)
                    health = sum(DELT_TOT)
                    best_delt = abs(current_health - health)
                    if best_delt > shortest_delta_so_far:
                        new_best_delt = []
                        new_best_delt.append(best_list[0])
                        best_list = []
                        best_list.append(best_delt)
                        best_list.append(focus_x)
                        best_list.append(focus_y)
                        best_list.insert(3,5)
                        print ('Bl1{}nbd{}'.format(best_delt, new_best_delt))
                        shortest_delta_so_far = best_delt
                        DELT_TOT = []
                    print(best_list)
                    focus_x = focus_x+1
                    bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
                    total[start_y - 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest
                    bitstobeadded = total[start_y + 1].pop(start_x - 1)  # moving a piece from northwest to west
                    total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west
                    bitstobeadded = total[start_y].pop(start_x + 1)
                    total[start_y + 1].insert(start_x + 1, bitstobeadded)

                    bitstobeadded = total[start_y - 1].pop(start_x + 2)
                    total[start_y].insert(start_x + 1, bitstobeadded)
                    total = total
                focus_y = focus_y +1

            if best_list[3] == 0:
                focus_x = best_list[1]
                focus_y = best_list[2]
                total = down(total)

            elif best_list[3] == 1:
                focus_x = best_list[1]
                focus_y = best_list[2]
                total = up(total)
            elif best_list[3] == 2:
                focus_x = best_list[1]
                focus_y = best_list[2]
                total = right(total)
            elif best_list[3] == 3:
                focus_x = best_list[1]
                focus_y = best_list[2]
                total = left(total)
            elif best_list[3] == 4:
                print ('___________________________________________________________________________________________')
                focus_x = best_list[1]
                focus_y = best_list[2]
                total = left(total)
            elif best_list[3] == 5:
                print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                focus_x = best_list[1]
                focus_y = best_list[2]
                bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
                total[start_y - 1].insert(start_x - 1,
                                          bitstobeadded)  # moving a piece from west to southwest
                bitstobeadded = total[start_y + 1].pop(start_x - 1)  # moving a piece from northwest to west
                total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west
                bitstobeadded = total[start_y].pop(start_x + 1)
                total[start_y + 1].insert(start_x + 1, bitstobeadded)

                bitstobeadded = total[start_y - 1].pop(start_x + 2)
                total[start_y].insert(start_x + 1, bitstobeadded)
                total = total
            focus(focus_x,focus_y)








    # Update
    all_sprites.update()
    if current_game_state == 0:  # states: welcoming = 1, playing = 2, teaching = 3, pausing = 4, solving = 5, exiting = -1
        game_img = welcome
        game_rect = welcome_rect
        score_write = game_font.render('best score {}'.format(move_count), False, (255, 255, 255))
        screen.blit(score_write, (width/2 - 100, height -100))
    elif current_game_state == 1:
        game_img = background
        game_rect = background_rect
    elif current_game_state == 3:
        game_img = info
        game_rect = info_rect
    elif current_game_state == 4:
        game_img = paused
        game_rect = paused_rect
    else:
        if event.type == pg.QUIT:
            running = False

    # Draw / render
    screen.fill(BLACK)
    screen.blit(game_img, game_rect)
    all_sprites.draw(screen)
    if rotate_clock or rotate_counter == True:
        pg.draw.circle(screen, DARK_GREEN, (new_x + GAMEBOARD_INSET_II, new_y + GAMEBOARD_INSET), 100, 25)
    if pull_left == True:
        pg.draw.line(screen, DARK_GREEN, (50, new_y + GAMEBOARD_INSET),
                     (new_x + GAMEBOARD_INSET_II, new_y + GAMEBOARD_INSET), 25)
    if pull_right == True:
        pg.draw.line(screen, DARK_GREEN, (new_x + GAMEBOARD_INSET + 15, new_y + GAMEBOARD_INSET),
                     (width - 300, new_y + GAMEBOARD_INSET), 25)
    if pull_up == True:
        pg.draw.line(screen, DARK_GREEN, (new_x + GAMEBOARD_INSET + 20, 50),
                     (new_x + GAMEBOARD_INSET + 20, new_y + GAMEBOARD_INSET), 25)
    if pull_down == True:
        pg.draw.line(screen, DARK_GREEN, (new_x + GAMEBOARD_INSET + 20, new_y + GAMEBOARD_INSET),
                     (new_x + GAMEBOARD_INSET + 20, height - 50), 25)

    GRID_LOC_X = focus_x * GRID_SIZE
    GRID_LOC_Y = focus_y * GRID_SIZE
    new_x = GRID_LOC_X
    new_y = GRID_LOC_Y
    if current_game_state == 1:
        health = health_bar(total)
        draw_health_bar(screen, 80, height -40, health)
        draw_elements(GAMEBOARD_INSET_II)
        counting_time = pg.time.get_ticks() - start_time
        game_time = counting_time / 1000 - pause_time
        counting_minutes = game_time / 120
        counting_seconds = game_time % 60
        time_counter = game_font.render(
            'TIME: {:02d}:{:02d} secs'.format(round(counting_minutes), round(counting_seconds)),
            False, (255, 255, 255))
        screen.blit(time_counter, (width - 260, height - height / 4))
    if current_game_state == 0:  # states: welcoming = 1, playing = 2, teaching = 3, pausing = 4, solving = 5, exiting = -1
        score_write = title_font.render('BEST SCORE: {}'.format(best_score), False, (0, 255, 0))
        screen.blit(score_write, (15, height -50))


    if MASTER_ARRAY == total:
        current_game_state = 0
        if move_count < best_score:
            score_write = title_font.render('You set high score.'
                                           'the old best score was{} '
                                           'and now its {}'.format(best_score, move_count), False, (255, 255, 255))
            screen.blit(score_write, (15, height -50))
            pg.time.delay(2000)
            save_high_score(best_score, move_count)
            total.append(1)
            best_score = move_count

        else:
            score_write = game_font.render('Good game! {} is a decent score'.format(move_count), False, (255, 255, 255))
            screen.blit(score_write, (15, height -50))
            pg.time.delay(2000)
        for array_length in range(ARRAY_LENGTH):
            MASTER_LIST.append(array_length)
            SHUFFLED_LIST.append(array_length)
        random.shuffle(SHUFFLED_LIST)
        EMPTY_LIST_I = SHUFFLED_LIST.copy()
        EMPTY_LIST_II = MASTER_LIST.copy()
        # STEP TWO - Copies SHUFFLE LIST into SHUFFLE ARRAY
        for array_width in range(ARRAY_WIDTH):
            SHUFFLED_ARRAY.append([])
            MASTER_ARRAY.append([])
            for array_height in range(ARRAY_HEIGHT):
                pop_array = SHUFFLED_LIST.pop(0)
                pop_array2 = MASTER_LIST.pop(0)
                SHUFFLED_ARRAY[array_width].append(pop_array)
                MASTER_ARRAY[array_width].append(pop_array2)
        SHUFFLED_LIST = EMPTY_LIST_I.copy()
        MASTER_LIST = EMPTY_LIST_II.copy()
        total = SHUFFLED_ARRAY.copy()



    # *after* drawing everything, flip the display
    pg.display.flip()


pg.quit()
