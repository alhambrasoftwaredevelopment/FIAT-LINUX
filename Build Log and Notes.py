'''
BUILD NOTES - TO DO
To completely rebuild.
learn variable naming conventions
make functions as "light" as possible
    break jobs down into specific tasks
    be careful of what gets passed.
    be mindful of what gets returned




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


add a "solver that compares with how far you are from solving
make the game have expandable size
read in high score, name and date
get high score and current score working
get rid of old versions
start numbering settings versions
be more careful when refactoring - do more checking.
make pieces different colors
make a piece a different size.
____________________________________________________________________
TileBreaker 2.4 -
fixed part of the high score tracker - it now knows when done and records if a score is better than high score.
completed first phase of distance checker -
The idea is that each piece to be solved will be featured in the center of the board.
I will need to use a copy of the MASTER_ARRAY

____________________________________________________________________
TileBreaker 2.3 -
Fixed corner counting issues
fixed pull highlights
fixed rotate highlights
learned to not use pngs made on older versions of photoshop
____________________________________________________________________


TIP - 2D ARRAY VERTICAL / HORIZONTAL SWAP
for w in range (5):
    for l in range (5):
        numcheck = MASTERLIST [l][w]
        print (numcheck)

TIP - BUILD PIECES LIKE AN ASSEMBLY LINE WHEN SETTING UP MULTIPLE PARTS -
GETTING ALL OF THE SETUP LISTS OF THIS PROJECT WAS A CHALLENGE.
USING AN 'EMPTY LIST' IN EACH STEP LIKE THE CURRENT STEP ON AN ASSEMBLY LINE REALLY HELPED.
'''
