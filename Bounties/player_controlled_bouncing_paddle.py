import random

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
vec = pygame.math.Vector2
size = [SCREEN_WIDTH, SCREEN_HEIGHT]


# img_dir = path.join(path.dirname(__file__), 'Imagesp1')


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((10, 60))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.pos = vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -.15
        elif keys[pygame.K_RIGHT]:
            self.acc.x = .15
        elif keys[pygame.K_UP]:
            self.acc.y = -.15
        elif keys[pygame.K_DOWN]:
            self.acc.y = .15
        else:
            self.acc.x = 0
            self.acc.y = 0
            if self.vel.x >= 0:
                self.vel.x = self.vel.x - .04
            if self.vel.x <= 0:
                self.vel.x = self.vel.x + .04
            if self.vel.y >= 0:
                self.vel.y = self.vel.y - .04
            if self.vel.y <= 0:
                self.vel.y = self.vel.y + .04

        if self.pos.x <= 15:
            self.vel.x = self.vel.x * -1  # -vec(0, 0)
            self.acc = vec(0, 0)
            # self.pos.x = 16

        if self.pos.x >= SCREEN_WIDTH - 15:
            self.vel.x = self.vel.x * -1  # vec(0, 0)
            self.acc = vec(0, 0)
            # self.pos.x = SCREEN_WIDTH - 16

        if self.pos.y <= 20:
            self.vel.y = self.vel.y * -1  # vec(0, 0)
            self.acc = vec(0, 0)
            # self.pos.y = 40

        if self.pos.y >= SCREEN_HEIGHT - 20:
            self.vel.y = self.vel.y * -1  # vec(0, 0)
            self.acc = vec(0, 0)
            # self.pos.y = SCREEN_HEIGHT - 40
        self.vel += self.acc
        self.pos += self.vel + .5 * self.acc
        self.rect.center = self.pos


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.change_x = random.randrange(-5, 5)
        self.change_y = random.randrange(-5, 5)
        # self.vel = vec(self.change_x, self.change_y)
        self.BALL_SIZE = random.randrange(10, 40)
        self.x = random.randrange(self.BALL_SIZE, SCREEN_WIDTH - self.BALL_SIZE)
        self.y = random.randrange(self.BALL_SIZE, SCREEN_HEIGHT - self.BALL_SIZE)
        self.randred = random.randrange(0, 255)
        self.randgrn = random.randrange(0, 255)
        self.randblu = random.randrange(0, 255)
        self.color = (self.randred, self.randgrn, self.randblu)
        ball_img = pygame.image.load("C:\\Users\\clay\\PycharmProjects\\Experiments\\ball_image1.png").convert()
        self.image_orig = pygame.transform.scale(ball_img, (self.BALL_SIZE, self.BALL_SIZE))
        # self.image_orig.fill(self.color)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.rot = 0
        self.rot_speed = random.randrange(-10, 10)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        # Move the ball's center
        # self.vel = vec(self.change_x, self.change_y)
        self.x += self.change_x
        self.y += self.change_y
        # Bounce the ball if needed
        if self.y > SCREEN_HEIGHT - self.BALL_SIZE or self.y < self.BALL_SIZE:
            self.change_y *= -1
        if self.x > SCREEN_WIDTH - self.BALL_SIZE or self.x < self.BALL_SIZE:
            self.change_x *= -1
        self.rect.center = (self.x, self.y)


def main():
    pygame.init()

    # Set the height and width of the screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Bouncing Balls")
    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    allsprites = pygame.sprite.Group()
    ballgroup = pygame.sprite.Group()
    Player.groups = allsprites
    player = Player()
    allsprites.add(player)
    Ball.groups = ballgroup, allsprites
    ball_list = []
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = Ball()
                    ballgroup.add(ball)
                    allsprites.add(ball)
                    ball_list.append(ball)
        for ball in ball_list:
            if ball == pygame.sprite.spritecollideany(player, ball_list, collided=None):
                ball.change_y *= -1
                ball.change_x *= -1
            if len(ball_list) >= 2:
                big_ball = ball
                ball_list.remove(ball)
                for another in ball_list:
                    if another == pygame.sprite.spritecollideany(big_ball, ball_list, collided=None):
                        big_ball.change_y *= -1
                        big_ball.change_x *= -1
                        another.change_y *= -1
                        another.change_x *= -1
                ball_list.append(big_ball)
        allsprites.update()
        screen.fill(BLACK)
        clock.tick(60)
        # Go ahead and update the screen with what we've drawn.
        allsprites.draw(screen)
        pygame.display.flip()
    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
