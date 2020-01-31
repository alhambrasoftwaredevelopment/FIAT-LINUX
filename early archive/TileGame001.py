'''
adding focus

'''
import pygame
import random
from settings import *


def draw_grid():
    for x in range(0, WIDTH, GRIDSIZE):
        pygame.draw.line(screen, GREEN, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRIDSIZE):
        pygame.draw.line(screen, GREEN, (0, y), (WIDTH, y))


class Tile(pygame.sprite.Sprite):
    # sprite for the Tiles
    def __init__(self, xloc, yloc):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.size = 118
        self.offset = 5
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(DARK_BLUE)
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # center the sprite on the screen
        self.rect.center = (xloc + self.size / 2 + self.offset, yloc + self.size / 2 + self.offset)

    def update(self):
        # any code here will happen every time the game loop updates
        pass


class Focus(pygame.sprite.Sprite):
    # sprite for the Tiles
    def __init__(self, focxloc, focyloc):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.size = 118
        self.offset = 5
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(GREEN)
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        self.focxloc = focxloc
        self.focyloc = focyloc
        # center the sprite on the screen
        self.rect.center = (self.focxloc + self.size / 2 + self.offset, self.focyloc + self.size / 2 + self.offset)

    def update(self):
        pygame.draw.rect(screen, RED, (self.focxloc, self.focxloc + 118, self.focyloc, self.focyloc + 118), 4)


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Tile Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
for xloc in range(0, WIDTH, GRIDSIZE):
    for yloc in range(0, HEIGHT, GRIDSIZE):
        tile = Tile(xloc, yloc)
        all_sprites.add(tile)
focus = Focus(160, 128)
all_sprites.add(focus)
# Game loop
x = 0
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    draw_grid()
    focus.update()

    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
