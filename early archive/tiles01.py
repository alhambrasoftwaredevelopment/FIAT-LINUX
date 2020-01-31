# Tiles - created by Clay Jones 2019

import pygame as pg
import random
from tilesettings import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

pg.init()
pg.font.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tiles")
title_font = pg.font.SysFont('Tahoma', int(40))
game_font = pg.font.SysFont('Tahoma', int(20))
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()


def import_history():
    """imports game data to update high score"""
    pass


def save_game_data():
    """saves and records game info for future plays"""
    pass


'''------------------------------------------------------------------------------------------------------------------'''


def init_game_array_and_list():
    """initializes data that will drive game"""
    pass


'''------------------------------------------------------------------------------------------------------------------'''


def get_current_focus():
    """may be a really important piece for establishing current focus that runs throughout game loop"""
    pass


def get_current_array():
    """very important function that will run automatically throughout game loop"""
    pass


'''------------------------------------------------------------------------------------------------------------------'''


def focus_left():
    """focus circle left and wraps"""
    pass


def focus_right():
    """focus circle left and wraps"""
    pass


def focus_up():
    """focus circle left and wraps"""
    pass


def focus_down():
    """focus circle left and wraps"""
    pass


'''------------------------------------------------------------------------------------------------------------------'''


def pull_left():
    """pulls current row one left"""
    pass


def pull_right():
    """pulls current row one right"""
    pass


def pull_up():
    """pulls current row one up"""
    pass


def pull_down():
    """pulls current row one down"""
    pass


def pull_clock():
    """rotates the eight pieces clockwise around the focus - doesn't work on the edges"""
    pass


def pull_counterclock():
    """rotates the eight pieces counter clockwise around the focus - doesn't work on the edges"""
    pass


'''------------------------------------------------------------------------------------------------------------------'''


def solver_setup():
    """establishes current state to prepare for solving"""
    pass


def solver_vert_and_horz():
    """calculates best vertical and horizontal moves """
    pass


def solver_clock_and_counter():
    pass


def solver_master():
    solver_setup()
    solver_vert_and_horz()
    solver_clock_and_counter()


'''------------------------------------------------------------------------------------------------------------------'''


def welcome_menu():
    """outside the while loop - press any key to begin. music catalog"""
    pass


def pause_menu():
    """stop clock, overlay, current stats"""
    pass


def instructions_menu():
    """pause game, overlay jpg of moves. game resumes upon release"""
    pass


def game_over_screen():
    """current stats, play again or exit"""
    pass


'''------------------------------------------------------------------------------------------------------------------'''
welcome = pg.image.load(path.join(img_dir, 'welcome.jpg')).convert()
welcome_rect = welcome.get_rect()
background = pg.image.load(path.join(img_dir, 'circuitbox.jpg')).convert()
background_rect = background.get_rect()
paused = pg.image.load(path.join(img_dir, 'paused.jpg')).convert()
paused_rect = paused.get_rect()
info = pg.image.load(path.join(img_dir, 'info.jpg')).convert()
info_rect = info.get_rect()

game_img = welcome
game_rect = welcome_rect

running = True
current_game_state = 0

'''------------------------------------------------------------------------------------------------------------------'''
# game_states: welcoming=1, playing = 2, teaching = 3, pausing = 4, solving = 5, exiting = -1
'''------------------------------------------------------------------------------------------------------------------'''
while running:
    clock.tick(FPS)
    # events()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running == False
    key_state = pg.key.get_pressed()

    if key_state[pg.K_i or pg.K_I]:
        """information screen"""
        current_game_state = 3

    if key_state[pg.K_ESCAPE]:
        """get completely out of the game"""
        running == False
        break

    if key_state[pg.K_SPACE]:
        game_state_before_pause = current_game_state

        if current_game_state != 4:
            current_game_state = 4
        else:
            current_game_state = 1

    if key_state[pg.K_LEFT]:
        focus_x = focus_left(focus_x, focus_y)

    elif key_state[pg.K_RIGHT]:
        focus_x = focus_right(focus_x, focus_y)

    elif key_state[pg.K_UP]:
        focus_y = focus_up(focus_x, focus_y)

    elif key_state[pg.K_DOWN]:
        focus_y = focus_down(focus_x, focus_y)

    elif key_state[pg.K_a or pg.K_A]:
        pull_left = True
        move_count = movecounter(move_count)
        total = left(total)


    elif key_state[pg.K_d or pg.K_D]:
        pull_right = True
        move_count = movecounter(move_count)
        total = right(total)


    elif key_state[pg.K_w or pg.K_W]:
        pull_up = True
        move_count = movecounter(move_count)
        total = up(total)


    elif key_state[pg.K_s or pg.K_S]:
        pull_down = True
        move_count = movecounter(move_count)
        total = down(total)



    elif key_state[pg.K_q or pg.K_Q]:
        start_x = focus_x
        start_y = focus_y
        if start_x >= 1 and start_x <= ARRAY_WIDTH - 2 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 2:
            rot_counterclock(total, focus_x, focus_y)
            move_count = move_count + 1
            rotate_clock = True

    elif key_state[pg.K_e or pg.K_E]:
        start_x = focus_x
        start_y = focus_y
        move_count = move_count + 1
        if start_x >= 1 and start_x <= ARRAY_WIDTH - 2 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 2:
            rot_clock(total, focus_x, focus_y)
            rotate_clock = True
    # update()
    all_sprites.update()
    if current_game_state == 0:  # states: welcoming = 1, playing = 2, teaching = 3, pausing = 4, solving = 5, exiting = -1
        game_img = welcome
        game_rect = welcome_rect
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
        game_img = welcome
        game_rect = welcome_rect
    print(current_game_state)

    # draw()
    screen.fill(BLACK)
    # game_img = game_state(current_game_state)
    screen.blit(game_img, game_rect)
    all_sprites.draw(screen)

    pg.display.flip()

pg.quit()
