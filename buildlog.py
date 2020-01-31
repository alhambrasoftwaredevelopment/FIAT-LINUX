'''

BUILD NOTES - TO DO
To completely rebuild.
learn variable naming conventions
make functions as "light" as possible
    break jobs down into specific tasks
    be careful of what gets passed.
    be mindful of what gets returned

------------------------------------------------------------------------------------------------------------------------

Square Evaluator
	Needs to have a fresh Copy of total
	A list to put latest best moves.
	a starting "best delta" that will get beaten by first try
	focus_x taken and focus_y taken for each move.
	First move gets added to the list and then every subsequent better move is added to the list.
	a way to disengage or negate scores
	a way to "put it back after testing"
	diagonal approach 0,0 UDLR
	1 up eval - if delta <= bestdelta - append
	2 down eval
	1 left eval
	2 right eval
	3x3 rotate checker
	1 clock rot - evaluate
	2 counter - evaluate
	a table that can enact best move.
	SET NEW_X to _____
	SET NEW_Y to _____
	if list[2] == 1:
	    pull_down() etc.
	delay
	rerun
	if board gets stuck with a-b pivot repeating trigger counter
	if counter gets higher than 3-
	goto random x-pos between 1-3
	goto random y-pos between 1-3
	roll die:
	    if 0: rot_clock()
	    else:
	        rot_counter()

------------------------------------------------------------------------------------------------------------------------
add a "solver that compares with how far you are from solving
make the game have expandable size
read in high score, name and date
get high score and current score working
get rid of old versions
start numbering settings versions
be more careful when refactoring - do more checking.
make pieces different colors
make a piece a different size.

------------------------------------------------------------------------------------------------------------------------

TileBreaker 2.4 -
fixed part of the high score tracker - it now knows when done and records if a score is better than high score.
completed first phase of distance checker -
The idea is that each piece to be solved will be featured in the center of the board.
I will need to use a copy of the MASTER_ARRAY

------------------------------------------------------------------------------------------------------------------------

TileBreaker 2.3 -
Fixed corner counting issues
fixed pull highlights
fixed rotate highlights
learned to not use pngs made on older versions of photoshop
------------------------------------------------------------------------------------------------------------------------

TIP - 2D ARRAY VERTICAL / HORIZONTAL SWAP
for w in range (5):
    for l in range (5):
        numcheck = MASTERLIST [l][w]
        print (numcheck)

TIP - BUILD PIECES LIKE AN ASSEMBLY LINE WHEN SETTING UP MULTIPLE PARTS -
GETTING ALL OF THE SETUP LISTS OF THIS PROJECT WAS A CHALLENGE.
USING AN 'EMPTY LIST' IN EACH STEP LIKE THE CURRENT STEP ON AN ASSEMBLY LINE REALLY HELPED.

Saving this code in case of problems - this was the original chunk that was informing the health bar length

    DELT_TOT = []
    for l in range(ARRAY_WIDTH):
        for w in range(ARRAY_HEIGHT):
            numcheck = total[w][l]
            nummod = numcheck % 5
            nummod = abs(nummod - l) % 3
            num = nummod
            DELT_TOT.append((num))
    for l in range(ARRAY_WIDTH):
        for w in range(ARRAY_HEIGHT):
            numcheck = total[l][w]
            nummod = numcheck % 5
            nummod = abs(nummod - l) % 3
            num = nummod
            DELT_TOT.append((num))
    health = sum(DELT_TOT)

------------------------------------------------------------------------------------------------------------------------

Saving this code in case I screw up the "press M" button

       elif key_state[pg.K_m or pg.K_M]:
            print (total)
            shortest_delta_so_far = 100
            DELT_TOT = []
            focus_x = 0
            focus_y = 0
            for w in range(5):
                for l in range(5):
                    numcheck = total[w][l]
                    numdif = numcheck % 5
                    numvert = int(abs((numcheck - numdif) / 5 - w))
                    if numvert > 2:
                        numvert = 2
                    if w == 0 and numcheck >= 20:
                        numvert = 1
                    if w == 4 and numcheck <= 4:
                        numvert = 1
                    nummod = numcheck % 5
                    nunummod = abs(nummod - l) % 3
                    DELT_TOT.append(nunummod)
                    DELT_TOT.append(numvert)
                    health = sum(DELT_TOT)
            #         print('distance vert {}'.format(numvert))
            #         print('item in x:{},y:{} = {} {} = hordelt '.format(w, l, numcheck, nunummod))
            #         print('')
            # print(SHUFFLED_ARRAY[0])
            # print(SHUFFLED_ARRAY[1])
            # print(SHUFFLED_ARRAY[2])
            # print(SHUFFLED_ARRAY[3])
            # print(SHUFFLED_ARRAY[4])
            if health < shortest_delta_so_far:
                shortest_delta_so_far = health
                print('new best = {}'.format(health))
            else:
                print(shortest_delta_so_far)
            best_move = []
            for i in range (100):
                total = up(total)
                print(total)

------------------------------------------------------------------------------------------------------------------------
Core developer badass
youtube
https://www.youtube.com/watch?v=OSGv2VnC0go
slides
https://speakerdeck.com/pyconslides/transforming-code-into-beautiful-idiomatic-python-by-raymond-hettinger-1

'''
