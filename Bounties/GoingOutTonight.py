print("What are you doing tonight")
print("")
age = int(input("How old are you? "))

if age <= 17:
    print("Not admitted without a parent ")
elif 21 >= age >= 17:
    print("You can watch an R Rated movie ")
elif 39 >= age >= 21:
    print("You can go to a club, no problem ")
else:
    print("Night in with your cat? ")

    # Maria Gamino
