import pygame as pg
import random
from tilesettings import *
from os import path

pg.init()
pg.font.init()
pg.mixer.init()
clock = pg.time.Clock()
title_font = pg.font.SysFont('Tahoma', int(40))
game_font = pg.font.SysFont('Tahoma', int(20))
screen = pg.display.set_mode((WIDTH, HEIGHT))


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
running = True
welcoming = True
playing = False
solving = False
teaching = False
pausing = False
'''------------------------------------------------------------------------------------------------------------------'''
while running:
    clock.tick(FPS)
    # events()
    # update()
    # draw()

pg.quit()
