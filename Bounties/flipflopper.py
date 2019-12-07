'''

 FLIP FLOPPER BOUNTY *woot woot*
                - Ren -
while True:
    kool = input('Give me a word --> ')
    y = kool[-1:] + kool[1:-1] + kool[:1]
    print(y
'''
print("")
word = input("Give me a word")
print("{0}{1}{2}".format(word[-1], word[1:-1], word[0]))

print("")
print("I can put the last letter of any word that you give me into the first letter ")

while True:
    word = input("give me a word: ")
    new = word[1:-1]
    last = word[-1]
    first = word[0]
    print(last + new + first)

# flip flopper
