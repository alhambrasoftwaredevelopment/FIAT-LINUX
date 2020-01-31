import random
import pygame as pg
from settings import *
from os import path

pg.init()
pg.font.init()

font_name = pg.font.match_font('hack')
title_font = pg.font.SysFont('Tahoma', int(35))
game_font = pg.font.SysFont('Tahoma', int(20))


def draw_text(surf, text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    surf.blit(text_surface, text_rect)


class Scene:
    def __init__(self):
        self.next = self
        self.name = type(self).__name__

    def process_input(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key in scenes[self.name]:
                self.switch_to(scenes[self.name][event.key]())

    def update(self):
        pass

    def draw(self, screen):
        pass

    def switch_to(self, next_scene):
        self.next = next_scene

    def end(self):
        self.next = None


class TitleScreen(Scene):
    def __init__(self):
        Scene.__init__(self)

    def draw(self, screen):
        screen.fill(BGCOLOR)
        draw_text(screen, "TILE BREAKER", 50, WHITE, WIDTH / 2, HEIGHT / 2, align="center")
        draw_text(screen, "press <SPACE BAR> to start", 20, WHITE, WIDTH / 2, HEIGHT * 3 / 4, align="center")
        draw_text(screen, "press <m> for menu", 20, WHITE, WIDTH / 2, HEIGHT * 3 / 4 + 50, align="center")


class GameScreen(Scene):
    def __init__(self):
        Scene.__init__(self)

    def process_input(self, events):
        pass

    def draw(self, screen):
        GRID_LOC_X = FOCUS_X * GRID_SIZE
        GRID_LOC_Y = FOCUS_Y * GRID_SIZE
        NEW_X = GRID_LOC_X
        NEW_Y = GRID_LOC_Y
        screen.fill(BGCOLOR)
        background = pg.image.load('circuit.jpg').convert()
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        draw_text(screen, "YOU'RE PLAYING", 50, WHITE, WIDTH / 2, HEIGHT / 2, align="center")
        draw_text(screen, "press <q> to end", 20, WHITE, WIDTH / 2, HEIGHT * 3 / 4, align="center")
        pg.draw.rect(screen, DARK_GRAY, (OFFSET, OFFSET, GAMEBOARD_WIDTH + OFFSET, HEIGHT - (2 * OFFSET)), 5)
        pg.draw.line(screen, DARK_GREEN, (NEW_X + OFFSET_II, GAMEBOARD_INSET), (NEW_X + OFFSET_II, HEIGHT - 100), 5)
        pg.draw.line(screen, DARK_GREEN, (GAMEBOARD_INSET + 15, NEW_Y + OFFSET_III), (WIDTH - 365, NEW_Y + OFFSET_III),
                     5)

        looper = 0
        for x in range(0, ARRAY_WIDTH):
            for y in range(0, ARRAY_HEIGHT):
                # print("count: {} x: {} y:{}".format(looper, x * GRID_SIZE, y * GRID_SIZE))
                looper = looper + 1
                tile_surface = game_font.render('{:02d}'.format(total[y][x]), False,
                                                (255, 255, 255))
                pg.draw.circle(screen, DARK_GRAY, (x * GRID_SIZE + OFFSET_II, y * GRID_SIZE + OFFSET_III), 24, 1)
                screen.blit(tile_surface, (x * GRID_SIZE + OFFSET_II - 10, y * GRID_SIZE + OFFSET_III - 12))
        pg.draw.circle(screen, DARK_GREEN, (NEW_X + GAMEBOARD_INSET_II, NEW_Y + GAMEBOARD_INSET), 35, 4)
        score_write = game_font.render('MOVE COUNT: {}'.format(move_count), False, (255, 255, 255))
        screen.blit(score_write, (WIDTH - 260, HEIGHT / 4))
        high_score_write = game_font.render('RECORD SCORE: {}'.format(best_score), False, (255, 255, 255))
        screen.blit(high_score_write, (WIDTH - 260, HEIGHT - HEIGHT / 6))
        title = title_font.render('TILE BREAKER', False, (255, 255, 255))
        screen.blit(title, (WIDTH - 260, HEIGHT / 12))
        completion_rate = game_font.render('COMPLETION RATE:', False, (255, 255, 255))
        screen.blit(completion_rate, (WIDTH - 260, HEIGHT / 3))
        time_counter = game_font.render(
            'TIME:{:02d} {:02d} secs'.format(round(counting_minutes), round(counting_seconds)),
            False, (255, 255, 255))
        screen.blit(time_counter, (WIDTH - 260, HEIGHT - HEIGHT / 4))


class MenuScreen(Scene):
    def __init__(self):
        Scene.__init__(self)

    def draw(self, screen):
        screen.fill(BGCOLOR)
        draw_text(screen, "SETTINGS", 50, WHITE, WIDTH / 2, HEIGHT / 2, align="center")
        draw_text(screen, "press <ESC> to return", 20, WHITE, WIDTH / 2, HEIGHT * 3 / 4, align="center")


class EndScreen(Scene):
    def __init__(self):
        Scene.__init__(self)

    def draw(self, screen):
        screen.fill(BGCOLOR)
        draw_text(screen, "GAME OVER", 50, WHITE, WIDTH / 2, HEIGHT / 2, align="center")
        draw_text(screen, "press <r> to restart", 20, WHITE, WIDTH / 2, HEIGHT * 3 / 4, align="center")


scenes = {'TitleScreen': {pg.K_SPACE: GameScreen,
                          pg.K_m: MenuScreen},
          'MenuScreen': {pg.K_ESCAPE: TitleScreen},
          'GameScreen': {pg.K_q: EndScreen},
          'EndScreen': {pg.K_r: TitleScreen}}
start_time = pg.time.get_ticks()
counting_time = pg.time.get_ticks() - start_time
game_time = counting_time / 1000
counting_minutes = game_time / 120
counting_seconds = game_time % 60


def main(start_scene):
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    scene = start_scene

    while scene:
        pg.display.set_caption(scene.name)
        clock.tick(FPS)
        counting_time = pg.time.get_ticks() - start_time
        game_time = counting_time / 1000
        counting_minutes = game_time / 120
        counting_seconds = game_time % 60
        events = []
        for event in pg.event.get():
            if event.type == pg.QUIT:
                scene.end()
            else:
                events.append(event)
                key_state = pg.key.get_pressed()
                print(key_state)

        scene.process_input(events)
        scene.update()
        scene.draw(screen)
        pg.display.flip()

        scene = scene.next


main(TitleScreen())
