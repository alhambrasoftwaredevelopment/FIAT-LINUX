import random

florin = "I like ham sandwiches and to go to bed early when I am tired"
lane = florin.split(" ")
for i in range(1, 100):
    listpicker = random.randrange(1, 10)
    print (lane[listpicker])
