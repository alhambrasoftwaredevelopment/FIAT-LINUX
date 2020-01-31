import random
ARRAY_WIDTH, ARRAY_HEIGHT = 5, 5
ARRAY_LENGTH = ARRAY_WIDTH * ARRAY_HEIGHT
MASTER_LIST = []
MASTER_ARRAY = []
SHUFFLED_LIST = []
SHUFFLED_ARRAY = []
DELT_TOT = []




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
SHUFFLED_ARRAY = [[9, 3, 0, 8, 23],
[15, 12, 1, 16, 22],
[6, 5, 21, 4, 7],
[24, 18, 10, 14, 17],
[13, 19, 2, 20, 11]]

SHUFFLED_LIST = [9, 3, 0, 8, 23, 15, 12, 1, 16, 22, 6, 5, 21, 4, 7, 24, 18, 10, 14, 17, 13, 19, 2, 20, 11]
print('')
print(SHUFFLED_ARRAY[0])
print(SHUFFLED_ARRAY[1])
print(SHUFFLED_ARRAY[2])
print(SHUFFLED_ARRAY[3])
print(SHUFFLED_ARRAY[4])
print('')
print (SHUFFLED_LIST)

for w in range (5):
    for l in range (5):
        numcheck = SHUFFLED_ARRAY [w][l]
        nummod = numcheck%5
        nummod = abs(nummod - l)%3
        DELT_TOT.append((nummod))
        health = sum(DELT_TOT)


        print ('item in x:{},y:{} = {} {} = hordelt '.format (w,l, numcheck,nummod))
        print('')
        print(SHUFFLED_ARRAY[0])
        print(SHUFFLED_ARRAY[1])
        print(SHUFFLED_ARRAY[2])
        print(SHUFFLED_ARRAY[3])
        print(SHUFFLED_ARRAY[4])
        print('')
