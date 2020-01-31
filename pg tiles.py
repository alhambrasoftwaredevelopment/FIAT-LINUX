import pygame as pg
from os import path
import sys
from oopsettings import *
from sprites import *


class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.img_dir = path.join(path.dirname(__file__), 'img')
        self.welcome = pg.image.load(path.join(self.img_dir, 'welcome.jpg')).convert()
        self.welcome_rect = self.welcome.get_rect()
        self.background = pg.image.load(path.join(self.img_dir, 'circuit.jpg')).convert()
        self.background_rect = self.background.get_rect()
        self.paused = pg.image.load(path.join(self.img_dir, 'paused.jpg')).convert()
        self.paused_rect = self.paused.get_rect()
        self.info = pg.image.load(path.join(self.img_dir, 'info.jpg')).convert()
        self.info_rect = self.info.get_rect()

        self.game_img = self.welcome
        self.game_rect = self.welcome_rect
    def load_data(self):
        self.high_score_file = open("high_score.txt", "r")
        self.best_score = int(self.high_score_file.read())
        print(self.best_score)
        return self.best_score

    def save_data(self):
        try:
            self.high_score_file = open("high_score.txt", "w")
            if bestscore < movecount:
                self.high_score_file.write(str(self.best_score))
                self.high_score_file.close()
            else:
                self.high_score_file.write(str(self.move_count))
                self.high_score_file.close()
        except IOError:
            print("Unable to save the high score.")





    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 2, 2)
        self.clock = pg.time.Clock()
        self.current_game_state = 0
        self.move_count = 0
        self.start_time = pg.time.get_ticks()
        for x in range(10, 20):
            Wall(self, x, 5)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()


    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        #print(self.current_game_state)
        if self.current_game_state == 0:
            self.game_img = self.welcome
            self.game_rect = self.welcome_rect

        if self.current_game_state == 1:
            self.game_img = self.background
            self.game_rect = self.background_rect

        if self.current_game_state == 3:
            self.game_img = self.info
            self.game_rect = self.info_rect

        if self.current_game_state == 4:
            self.game_img = self.paused
            self.game_rect = self.paused_rect


    def draw_grid(self):
        for x in range(76, 457, TILESIZE):
            pg.draw.line(self.screen, LIGHT_GRAY, (x, 76), (x, HEIGHT-45))
        for y in range(76, 457, TILESIZE):
            pg.draw.line(self.screen, LIGHT_GRAY, (76, y), (WIDTH-345, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.screen.blit(self.game_img, self.game_rect)
        if self.current_game_state == 1:
            self.draw_grid()
            self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            key_state = pg.key.get_pressed()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE and self.current_game_state == 0:
                    pg.time.delay(200)
                    self.quit()
                if event.key == pg.K_ESCAPE and self.current_game_state == 1:
                    pg.time.delay(200)
                    self.current_game_state = 0
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)
                if key_state[pg.K_n or pg.K_N]:
                    self.current_game_state = 1
                if key_state[pg.K_i or pg.K_I]:
                    if self.current_game_state != 3:
                        self.current_game_state = 3
                    elif self.current_game_state == 3:
                        self.current_game_state = 1
                if key_state[pg.K_SPACE]:
                    pg.time.delay(100)
                    if self.current_game_state == 1:
                        self.current_game_state = 4
                    elif self.current_game_state == 4:
                        self.current_game_state = 1



    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
