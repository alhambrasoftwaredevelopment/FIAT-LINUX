import random

print ("-------------------------------------")
print ("        Guess the number game")
print ("-------------------------------------")
print ("")
guess = -1
name = input('Player, what is your name?  :')
print("hello " + name + ", Let's play a game")

the_number = random.randint(0, 100)

while guess != the_number:
    guess_text = input('guess a number between 0 and 100')
    guess = int(guess_text)
    if guess < the_number:
        print("too low")
    elif guess > the_number:
        print ("too high")
    else:
        print("you got it!")
