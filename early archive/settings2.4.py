import random

WIDTH, HEIGHT = 800, 500
OFFSET, OFFSET_II, OFFSET_III = 50, 120, 100
TITLE = "Tile Breaker 2020"
GAMEBOARD_WIDTH, GAMEBOARD_HEIGHT, GAMEBOARD_INSET, GAMEBOARD_INSET_II = 400, 400, 100, 120
ARRAY_WIDTH, ARRAY_HEIGHT = 5, 5
ARRAY_LENGTH = ARRAY_WIDTH * ARRAY_HEIGHT
GRID_SIZE = int((HEIGHT - (OFFSET_II)) / ARRAY_WIDTH)
FOCUS_X, FOCUS_Y = 0, 0
FPS = 60
BUTTON_SIZE = 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 122)
DARK_GRAY = (50, 50, 50)
DARK_GREEN = (0, 50, 0)

EMPTY_LIST_I = []
EMPTY_LIST_II = []
MASTER_LIST = []
MASTER_ARRAY = []
SHUFFLED_LIST = []
SHUFFLED_ARRAY = []
NEG_DELTA = []

DELTAS_LIST = []
HORIZONTAL_LIST = []
total = []

move_count = 0
best_score = 0
best_time = 0
game_loop = False

# LISTS SETUP:
# STEP ONE:
# creates SHUFFLE LIST and shuffles it.
# since 'pop' is used; list gets copied into EMPTY LIST to preserve data
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
# STEP THREE: sets up Delta between master list index and shuffle list index
for x in range(ARRAY_LENGTH):
    nums = abs(
        x - SHUFFLED_LIST[x])
    DELTAS_LIST.append(nums)
total = SHUFFLED_ARRAY.copy()
for x in range(ARRAY_LENGTH - 1, 0, -1):
    nums = abs(
        x - SHUFFLED_LIST[x])
    NEG_DELTA.append(nums)

# print(MASTER_LIST)
# print(SHUFFLED_LIST)

# print('')
# print (DELTAS_LIST)
# print('')#
print(SHUFFLED_ARRAY[0])
print(SHUFFLED_ARRAY[1])
print(SHUFFLED_ARRAY[2])
print(SHUFFLED_ARRAY[3])
print(SHUFFLED_ARRAY[4])
print('')
thing = MASTER_ARRAY[0][0]
START_X = 2
START_Y = 2
VERT_DISPLACE = 0
HORZ_DISPLACE = 0
if MASTER_ARRAY[0][0] in SHUFFLED_ARRAY[START_Y]:  # Its in the starting middle row
    if SHUFFLED_ARRAY[START_Y][START_X + HORZ_DISPLACE] == MASTER_ARRAY[0][
        0]:  # check to see if it is in the middle middle
        print("problem 00")
    else:
        HORZ_DISPLACE = HORZ_DISPLACE + 1  # move to middle row 2 indexes 1 and 3
        if SHUFFLED_ARRAY[START_Y][START_X + HORZ_DISPLACE] == MASTER_ARRAY[0][0] or \
                SHUFFLED_ARRAY[START_Y][START_X - HORZ_DISPLACE] == MASTER_ARRAY[0][0]:
            print("problem 01")
        else:
            HORZ_DISPLACE = HORZ_DISPLACE + 1
            print('YEPP it')

elif MASTER_ARRAY[0][0] in SHUFFLED_ARRAY[START_Y + 1] or MASTER_ARRAY[0][0] in SHUFFLED_ARRAY[
    START_Y - 1]:
    VERT_DISPLACE = VERT_DISPLACE + 1
    if SHUFFLED_ARRAY[START_Y + 1][START_X] == MASTER_ARRAY[0][0] or SHUFFLED_ARRAY[START_Y - 1][START_X] == \
            MASTER_ARRAY[0][0]:
        print("problem 02")
    elif SHUFFLED_ARRAY[START_Y + 1][START_X + 1] == MASTER_ARRAY[0][0] or \
            SHUFFLED_ARRAY[START_Y + 1][START_X - 1] == MASTER_ARRAY[0][0] or \
            SHUFFLED_ARRAY[START_Y - 1][START_X + 1] == MASTER_ARRAY[0][0] or \
            SHUFFLED_ARRAY[START_Y - 1][START_X - 1] == MASTER_ARRAY[0][0]:
        HORZ_DISPLACE = HORZ_DISPLACE + 1
        print('too old 4ts')

    else:
        HORZ_DISPLACE = HORZ_DISPLACE + 2
        print("problem 04")



elif MASTER_ARRAY[0][0] in SHUFFLED_ARRAY[START_Y + 2] or MASTER_ARRAY[0][0] in SHUFFLED_ARRAY[
    START_Y - 2]:
    VERT_DISPLACE = VERT_DISPLACE + 2

    if SHUFFLED_ARRAY[START_Y + 2][START_X] == MASTER_ARRAY[0][
        0] or SHUFFLED_ARRAY[START_Y - 2][START_X] == MASTER_ARRAY[0][
        0]:
        print('gotteeee')

    elif SHUFFLED_ARRAY[START_Y + 2][START_X + 1] == MASTER_ARRAY[0][0] or \
            SHUFFLED_ARRAY[START_Y + 2][START_X - 1] == MASTER_ARRAY[0][0] or \
            SHUFFLED_ARRAY[START_Y - 2][START_X + 1] == MASTER_ARRAY[0][0] or \
            SHUFFLED_ARRAY[START_Y - 2][START_X - 1] == MASTER_ARRAY[0][0]:
        print("mgr")

        HORZ_DISPLACE = HORZ_DISPLACE + 1
    else:
        print("problem duda")
        HORZ_DISPLACE = HORZ_DISPLACE + 2

print('vert: {}'.format(VERT_DISPLACE))
print('horz: {}'.format(HORZ_DISPLACE))

'''

count = 0
POSSIBLE_MOVES_LIST = []
for x in range(ARRAY_LENGTH):
    posdelt = abs(SHUFFLED_LIST[x] - x)
    countbackwards = (ARRAY_LENGTH - 1) - x
    negdelt = abs(countbackwards - SHUFFLED_LIST[x])
    num_I = posdelt
    print('posdelt ={} negdelt = {}'.format(posdelt, negdelt))
    if num_I >= 20 and num_I < 25:
        num_I = 4 + num_I % 5
    elif num_I >= 15 and num_I < 20:
        num_I = 3 + num_I % 5
    elif num_I >= 10 and num_I < 15:
        num_I = 2 + num_I % 5
    elif num_I >= 5 and num_I < 10:
        num_I = 1 + num_I % 5
    else:
        num_I = num_I % 5
    num_II = negdelt
    if num_II >= 20 and num_II < 25:
        num_II = 4 + num_II % 5
    elif num_II >= 15 and num_II < 20:
        num_II = 3 + num_II % 5
    elif num_II >= 10 and num_II <15:
        num_II = 2 + num_II % 5
    elif num_II >= 5 and num_II < 10:
        num_II = 1 + num_II % 5
    else:
        num_II = num_II % 5
    # print (SHUFFLED_LIST[x],posdelt, countbackwards - SHUFFLED_LIST[x])
    print('{} {} {}'.format(x, posdelt, negdelt))
    if num_I >= num_II:
        POSSIBLE_MOVES_LIST.append(num_II)
    else:
        POSSIBLE_MOVES_LIST.append(num_I)
    print('num_I ={} num_II = {}'.format(num_I, num_II))
print(POSSIBLE_MOVES_LIST)

print(SHUFFLED_ARRAY[0])
print(SHUFFLED_ARRAY[1])
print(SHUFFLED_ARRAY[2])
print(SHUFFLED_ARRAY[3])
print(SHUFFLED_ARRAY[4])
print('')

'''
