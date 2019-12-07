"""
 Bounces a rectangle around the screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/-GmKoaX2iMs
"""

import random

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Rectangle")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50
rect2_x = 100
rect2_y = 100
rect3_x = 100
rect3_y = 100
randx = random.randrange(-3, 3)
randy = random.randrange(-3, 3)
randx2 = random.randrange(-3, 3)
randy2 = random.randrange(-3, 3)
# Speed and direction of rectangle
rect_change_x = 2
rect_change_y = 2
rect2_change_x = randx
rect2_change_y = randy
rect3_change_x = randx2
rect3_change_y = randy2

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Logic
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y
    rect2_x += rect2_change_x
    rect2_y += rect2_change_y
    rect3_x += rect2_change_x
    rect3_y += rect2_change_y

    # Bounce the ball if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    if rect2_y > 450:
        rect2_y = 0
    if rect2_y < 0:
        rect2_y = 450
    if rect2_x > 650:
        rect2_x = 0
    if rect2_x < 0:
        rect2_x = 650
    if rect3_y > 450:
        rect3_y = 0
    if rect3_y < 0:
        rect3_y = 450
    if rect3_x > 650:
        rect3_x = 0
    if rect3_x < 0:
        rect3_x = 650

    # --- Drawing
    # Set the screen background
    screen.fill(BLACK)

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])
    pygame.draw.rect(screen, WHITE, [rect2_x, rect2_y, 50, 50])
    pygame.draw.rect(screen, BLACK, [rect2_x + 10, rect2_y + 10, 30, 30])
    pygame.draw.rect(screen, WHITE, [rect3_x, rect3_y, 110, 50])
    pygame.draw.rect(screen, GREEN, [rect3_x + 10, rect3_y + 110, 30, 30])

    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close everything down
pygame.quit()
