'''
Progress - created a swipe left and right system that works - probably can get a vertical version.
create random 2D array WIDTH x HEIGHT
add a move counter
add a "solver that compares with how far you are from solving
make the game have expandable size


'''
print("welcome to the Tile game")
print("arrow keys change focus")
print("WADS keys move rows and columns")
print("Q and E rotate around focus")
import random

import pygame as pg
from settings import *
from os import path
img_dir = path.join(path.dirname(__file__), 'img')

pg.init()
pg.font.init()
game_font = pg.font.SysFont('Tahoma', 30)

screen = pg.display.set_mode((WIDTH, HEIGHT))
'''#tile_list = ['1.png','2.png','3.png', '4.png', '5.png',
            '6.png', '7.png', '8.png', '9.png', '10.png',
            '11.png', '12.png', '13.png', '14.png', '15.png',
            '16.png', '17.png', '18.png', '19.png', '20.png',
             '21.png','22.png','23.png', '24.png', '25.png']


#player_img = pg.image.load(path.join("0.png")).convert()
print(player_img)
player_mini_img = pg.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
'''
def focus(FOCUSX, FOCUSY):
    print_it_up(FOCUSX, FOCUSY)
    return FOCUSX, FOCUSY
def focus_left(FOCUSX, FOCUSY):
    if FOCUSX > 0:
        FOCUSX -= 1
    focus(FOCUSX, FOCUSY)
    pg.time.delay(100)
    return FOCUSX
def focus_right(FOCUSX, FOCUSY):
    if FOCUSX < 4:
        FOCUSX += 1
    focus(FOCUSX, FOCUSY)
    pg.time.delay(100)
    return FOCUSX
def focus_up(FOCUSX, FOCUSY):
    if FOCUSY > 0:
        FOCUSY -= 1
    focus(FOCUSX, FOCUSY)
    pg.time.delay(100)
    return FOCUSY
def focus_down(FOCUSX, FOCUSY):
    if FOCUSY < 4:
        FOCUSY += 1
    focus(FOCUSX, FOCUSY)
    pg.time.delay(100)
    return FOCUSY
def rot_clock(total, FOCUSX, FOCUSY):
    start_x = FOCUSX
    start_y = FOCUSY
    try:
        if start_x >= 1 and start_x <= ARRAY_WIDTH - 1 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 1:
            bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
            total[start_y - 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest

            bitstobeadded = total[start_y + 1].pop(start_x - 1)  # moving a piece from northwest to west
            total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west

            bitstobeadded = total[start_y].pop(start_x + 1)
            total[start_y + 1].insert(start_x + 1, bitstobeadded)

            bitstobeadded = total[start_y - 1].pop(start_x + 2)
            total[start_y].insert(start_x + 1, bitstobeadded)
            print_it_up(FOCUSX, FOCUSY)
            return total
    except:
        return total
def rot_counterclock(total, FOCUSX,FOCUSY):
    start_x = FOCUSX
    start_y = FOCUSY
    try:
        if start_x >= 1 and start_x <= ARRAY_WIDTH - 1 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 1:
            bitstobeadded = total[start_y].pop(start_x - 1) # moving a piece from west to southwest
            total[start_y + 1].insert(start_x-1, bitstobeadded)# moving a piece from west to southwest
            bitstobeadded = total[start_y - 1].pop(start_x - 1)# moving a piece from northwest to west
            total[start_y].insert(start_x-1, bitstobeadded)# moving a piece from northwest to west
            bitstobeadded = total[start_y].pop(start_x + 1)
            total[start_y - 1].insert(start_x + 1, bitstobeadded)
            bitstobeadded = total[start_y + 1].pop(start_x + 2)
            total[start_y].insert(start_x + 1, bitstobeadded)
            print_it_up(FOCUSX, FOCUSY)
            return total
    except:
        return total
def print_it_up(FOCUSX, FOCUSY):

    for i in range (PRINTBUFFER):
        print("")
    print('current focus: x={}, y={}'.format(FOCUSX, FOCUSY))
    print ('move count: {}'.format(movecount))
    if FOCUSX == 0:
        print("     v")
    elif FOCUSX == 1:
        print("         v")
    elif FOCUSX == 2:
        print("              v")
    elif FOCUSX == 3:
        print("                   v")
    elif FOCUSX == 4:
        print("                        v")
    if FOCUSY == 0:
        print(
            ">   {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  <".format(total[0][0], total[0][1], total[0][2], total[0][3],
                                                                    total[0][4]))
    else:
        print(
            "    {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  ".format(total[0][0], total[0][1], total[0][2], total[0][3],
                                                                    total[0][4]))
    if FOCUSY == 1:
        print(
            ">   {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  <".format(total[1][0], total[1][1], total[1][2], total[1][3],
                                                                    total[1][4]))
    else:
        print(
            "    {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  ".format(total[1][0], total[1][1], total[1][2], total[1][3],
                                                                    total[1][4]))
    if FOCUSY == 2:
        print(
            ">   {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  <".format(total[2][0], total[2][1], total[2][2], total[2][3],
                                                                    total[2][4]))
    else:
        print(
            "    {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  ".format(total[2][0], total[2][1], total[2][2], total[2][3],
                                                                    total[2][4]))
    if FOCUSY == 3:
        print(
            ">   {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  <".format(total[3][0], total[3][1], total[3][2], total[3][3],
                                                                    total[3][4]))
    else:
        print(
            "    {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  ".format(total[3][0], total[3][1], total[3][2], total[3][3],
                                                                    total[3][4]))
    if FOCUSY == 4:
        print(
            ">   {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  <".format(total[4][0], total[4][1], total[4][2], total[4][3],
                                                                    total[4][4]))
    else:
        print(
            "    {:02d}   {:02d}   {:02d}   {:02d}   {:02d}  ".format(total[4][0], total[4][1], total[4][2], total[4][3],
                                                                    total[4][4]))
    if FOCUSX == 0:
        print("     ^")
    elif FOCUSX == 1:
        print("         ^")
    elif FOCUSX == 2:
        print("              ^")
    elif FOCUSX == 3:
        print("                   ^")
    elif FOCUSX == 4:
        print("                        ^")
    for i in range(10-PRINTBUFFER):
        print("")


def get_vert(FOCUSX, FOCUSY):
    print_it_up(FOCUSX, FOCUSY)
    vertlist = []
    vertcolumn = []
    for x in range(0, 5):
        for y in range(0, 5):
            vertcolumn.append(total[y][x])
        vertlist.append(vertcolumn)
        vertcolumn = []
    return vertlist
def transcribe(vertlist):
    horzlist = []
    horzrow = []
    for x in range(0, 5):
        for y in range(0, 5):
            horzrow.append((vertlist[y][x]))
        horzlist.append(horzrow)
        horzrow = []
    return horzlist
def how_to_move_l_and_r(FOCUSX, FOCUSY):
    print_it_up(FOCUSX, FOCUSY)
    vertlist = []
    for y in range(0, 5):
        vertlist.append(total[y][FOCUSY])
    print(vertlist)
    vertlist.append(vertlist[0])
    vertlist.remove(vertlist[0])
    print(vertlist)
    goback = vertlist.pop(-1)
    vertlist.insert(0, goback)
    print(vertlist)
def movecounter(movecount):
    movecount += 1
    return movecount
def class_grid(total, WIDTH, HEIGHT, GRIDSIZE):
    anum = 1
    for xloc in range(0, WIDTH, GRIDSIZE):
        for yloc in range(0, HEIGHT, GRIDSIZE):

            tile = Tile(anum,total,xloc,yloc)
            anum = anum+1
            all_sprites.add(tile)
class Tile(pg.sprite.Sprite):
    def __init__(self, anum, totalnum, xloc, yloc):
        pg.sprite.Sprite.__init__(self)
        self.num = anum
        self.size = random.randrange(2,5)
        self.image = pg.Surface((self.size, self.size))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,WIDTH)
        self.rect.y = yloc
        self.fallspeed = random.randrange(1,10)

        self.myarray_rowone = total[0]
        self.myarray_rowtwo = total[1]

    def update(self):
        self.rect.y= self.rect.y + self.fallspeed
        if self.rect.y >= HEIGHT/2:
            self.kill()

tile_surface = game_font.render(str(total[random.randrange(0,4)][random.randrange(0,4)]), False, (255, 255, 255))

all_sprites = pg.sprite.Group()


pg.display.set_caption("Tile Break 2020")
clock = pg.time.Clock()

running = True
while running:
    clock.tick(FPS)
    #class_grid(total, WIDTH,HEIGHT,GRIDSIZE)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        keystate = pg.key.get_pressed()

        if keystate[pg.K_LEFT]:
            FOCUSX = focus_left(FOCUSX, FOCUSY)


        elif keystate[pg.K_RIGHT]:
            FOCUSX = focus_right(FOCUSX, FOCUSY)

        elif keystate[pg.K_UP]:
            FOCUSY = focus_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_DOWN]:
            FOCUSY = focus_down(FOCUSX, FOCUSY)

        elif keystate[pg.K_a or pg.K_A]:
            movecount = movecounter(movecount)
            countitup = total[FOCUSY].pop(0)
            total[FOCUSY].append(countitup)
            print_it_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_d or pg.K_D]:
            movecount = movecounter(movecount)
            countitup = total[FOCUSY].pop(-1)
            total[FOCUSY].insert(0, countitup)
            print_it_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_w or pg.K_W]:
            movecount = movecounter(movecount)
            vertlist = get_vert(FOCUSX, FOCUSY)
            countitup = vertlist[FOCUSX].pop(0)
            vertlist[FOCUSX].append(countitup)
            horizontal_again = transcribe(vertlist)
            total = horizontal_again
            print_it_up(FOCUSX, FOCUSY)


        elif keystate[pg.K_s or pg.K_S]:
            movecount = movecounter(movecount)
            vertlist = get_vert(FOCUSX, FOCUSY)
            countitup = vertlist[FOCUSX].pop(-1)
            vertlist[FOCUSX].insert(0, countitup)
            horizontal_again = transcribe(vertlist)
            total = horizontal_again
            print_it_up(FOCUSX, FOCUSY)

        elif keystate[pg.K_q or pg.K_Q]:
            movecount = movecounter(movecount)
            rot_counterclock(total, FOCUSX,FOCUSY)


        elif keystate[pg.K_e or pg.K_E]:
            movecount = movecounter(movecount)
            rot_clock(total, FOCUSX,FOCUSY)

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    for x in range (0,5):
        for y in range (0,5):
            tile_surface = game_font.render('{:02d}'.format(total[y][x]), False,
                                            (255, 255, 255))
            screen.blit(tile_surface, (x*GRIDSIZE+25, y*GRIDSIZE+20))
    GRIDLOCX = FOCUSX*GRIDSIZE
    GRIDLOCY = FOCUSY*GRIDSIZE
    NEWX = GRIDLOCX
    NEWY = GRIDLOCY


    pg.draw.circle(screen,GREEN,(NEWX+40,NEWY+40),25, 2)
    score_write = game_font.render(str(movecount), False,(255, 255, 255))
    screen.blit(score_write, (WIDTH/2, HEIGHT-40))
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
