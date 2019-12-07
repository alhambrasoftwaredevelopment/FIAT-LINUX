print("")
print("I can tell you if the sum of two numbers is 10 or if one of the numbers is 10 ")
print("False means that neither the sum nor one of the numbers equals 10 ")
print("True means that either the sum or one of the numbers equals 10 ")
print("")

while True:
    num1 = int(input("give me a number: "))
    num2 = int(input("give me another number: "))
    sum = num1 + num2

    if sum == 10:
        print("True")
        print("")
    elif num1 == 10:
        print("True")
        print("")
    elif num2 == 10:
        print("True")
        print("")
    else:
        print("False")
        print("")

# 10 to Win
# Maria Gamino
