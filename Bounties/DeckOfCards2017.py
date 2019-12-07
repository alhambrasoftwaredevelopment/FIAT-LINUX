import random

deck = []
p1 = []
p2 = []
p3 = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]  # list of suits
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King"]  # list of ranks

for s in range(0, 4):
    newsuit = suits[s]
    for r in range(0, 13):
        newrank = ranks[r]
        newcard = 'the {} of {}'.format(newrank, newsuit)
        deck.append(newcard)
print (deck)
random.shuffle(deck)
print(deck)

for jhon in range(0, 5):
    playercount = 1
    for i in range(0, 3):
        playercard = deck[-1]
        deck.remove(playercard)
        if playercount == 1:
            p1.append(playercard)
        elif playercount == 2:
            p2.append(playercard)
        elif playercount == 3:
            p3.append(playercard)
        else:
            print ('yadadadadada')
        playercount = playercount + 1
print (playercount)
print (p1)
print (p2)
print (p3)
