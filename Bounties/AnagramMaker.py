import random

ListLength = 1
newlist = []
WordToBeScrambled = ''
WordToBeScrambled = input('what word would you like to scramble?: ')
ListOfStrings = list(WordToBeScrambled)
print (ListOfStrings)

while WordToBeScrambled != "Exit":
    for i in range(0, len(WordToBeScrambled)):
        pick = random.randrange(0, len(ListOfStrings))
        ListOfStrings.remove(ListOfStrings[pick])
        newlist.append(ListOfStrings[pick])

    print(newlist)
