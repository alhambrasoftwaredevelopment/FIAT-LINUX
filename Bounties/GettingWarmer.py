print("")
print("true means that your guess is 10 or closer to my number ")
print("false means that your guess is 10 more from my number ")
print("")

while True:
    guess = int(input("what is your guess: "))
    if 40 <= guess <= 60:
        print("True")
    else:
        print("False")

# getting warmer
