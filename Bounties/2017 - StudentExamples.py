# 10/30/17
# Number Cycler 1-100
'''
x = 1
while True:
    for counter in range(1, 101):
        print(counter)
        x += 1

# By Efrain Telles

# 10/30/17
# count to 1,000 by any multiple
print('')
print('_____________________________________________')
print('Enter A Number For Their Multiples Up To 1000')
print('_____________________________________________')
print('')
while True:
    print("")
    num = int(input('Enter A Number: '))
    for i in range(0, 1001, num):
        print(i)


# By Efrain Telles

# 10/30/17
# count to 1,000 by any multiple
print('')
print('_____________________________________________')
print('Enter A Number For Their Multiples Up To 1000')
print('_____________________________________________')
print('')
while True:
    print("")
    num = int(input('Enter A Number: '))
    for i in range(0, 1001, num):
        print(i)


# By Efrain Telles
'''
print('*********************************************************')
print('  I can make any number positive, do you want to try?')
print('*********************************************************')

number = input("Input a number -->")
intnumber = int(number)
print(abs(intnumber))
