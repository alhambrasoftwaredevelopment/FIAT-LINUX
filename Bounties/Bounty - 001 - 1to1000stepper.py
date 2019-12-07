'''
while True:

    print ("I can count to 1000 by whatever number you like or click x to exit")
    print ("I can count by 3s (3,6,9) or 5s (5,10 15), whatever you like!")
    stepper = input ("give me a number   ")
    if stepper == "x":
        break
    print ("")
    print ("Oh, you chose {0}. I can count using {0} ".format(str(stepper)))
    for i in range (0,1001, int(stepper)):
        print (i)
    print("")




while True:
    alwayspositive = input ("give me anynumber and I can make it positive")
    alwaysposint = int(alwayspositive)
    if (alwaysposint) <=0:
        print(-alwaysposint)
    else:
        print(alwaysposint)


while True:
    for i in range (1,101):
        print (i)
    if i  >= 100:
        i = 1

'''

import random

random_num_of_lives = random.randrange(1, 100)
print("you currently have {} lives left.".format(random_num_of_lives))
while random_num_of_lives != 0:
    didit = input("Move?")
    if didit.lower() == "h":
        random_num_of_lives = random_num_of_lives - 1
        print("you currently have {} lives left.".format(random_num_of_lives))
