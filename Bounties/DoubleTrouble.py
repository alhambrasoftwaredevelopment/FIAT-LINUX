print("")
print("give me two numbers if they aren't equal to each other I will give you the sum, ")
print("if they're equal i'll give you their product")
print("")

while True:
    num1 = int(input("give me a number: "))
    num2 = int(input("give me another number: "))

    if num1 != num2:
        print(num1 + num2)
    if num1 == num2:
        print(num1 * num2)
    print("")

# Double Trouble
