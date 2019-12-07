import random

ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
cardlist = []
for suitor in range(0, 4):
    for ranker in range(0, 13):
        newcard = '{} of {}'.format(ranks[ranker], suits[suitor])
        cardlist.append(newcard)
print(cardlist)
for i in range(0, 51):
    shuffle = random.randrange(0, len(cardlist))
    print (cardlist[shuffle])
    cardlist.remove(cardlist[shuffle])
