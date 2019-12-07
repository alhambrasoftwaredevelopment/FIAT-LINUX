''' PLURAL AND SINGLE BOUNTY *woot woot*
                    - Ren -             '''
while True:
    x = input('Give me a noun -->')
    y = list(x)
    if 's' in y:
        z = x.replace("s", " ")
        print(z)
    elif 's' not in y:
        y.append('s')
        w = ''.join(y)
        print(w)

_________________________________________
# Plural And Single
# Works But not as well...Cactus = Cactuses instead of Cacti
# By Efrain
import inflect

p = inflect.engine()
while True:
    plu = input("Enter A Plural Or Singular Word: ")
    print("The Plural/Singular Of ", plu, " Is ", p.plural(plu))

print("")
word = input("Give me a word")
if word[-1] == "s":
    print(word[:-1])
if word[-1] != "s":
    print("{0}s".format(word))

print("")
print("If you give me a word that is plural i'll make it singular. ")
print("If you give me a word that is singular i'll make it plural. ")
print("")

while True:
    word = input("give me a word: ")
    if word[-1] is not "s":
        print(word + "s")
        print("")
    else:
        print(word[:-1])
        print("")

# plural and single
