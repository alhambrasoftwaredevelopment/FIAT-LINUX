primechecker = 0
for counter in range(1, 10):
    for modchecker in range(1, counter):
        if counter % modchecker == 0:
            primechecker = primechecker + 1
        if counter == modchecker:
            print("prime!")
            print(counter)
            primechecker = 0
            if primechecker == 2:
                print (counter, modchecker)
