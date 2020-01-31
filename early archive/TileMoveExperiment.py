# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# Player sprite and movement
import pygame
import random
from settings import *

TILESIZE = 100
WIDTH = 600
HEIGHT = 600
FPS = 120

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, COLOR):
        pygame.sprite.Sprite.__init__(self)
        self.size = 95
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        self.speedx = 0

        self.x = x
        self.y = y

        self.rect.x = x - self.size
        self.rect.y = y - self.size

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH


all_sprites = pygame.sprite.Group()
counter = 0
for x in range(100, 600, 120):
    for y in range(150, 650, 100):
        COLOR = (255 - counter, 0, counter)
        player = Player(x, y, COLOR)
        all_sprites.add(player)

        counter = counter + 10

# Game loop
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
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
