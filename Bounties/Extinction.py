''' EXTINCTION BOUNTY *woot woot*
            - Ren -             '''
x = 'dinosaur'
z = list(x)
while True:
    asteroid = int(input('Give me a number from 0 to 7 >'))
    del z[asteroid]
    y = ''.join(z)
    print(y)
    if len(z) == 0:
        print("RIP Dino, you will be missed :'( ")
        break
