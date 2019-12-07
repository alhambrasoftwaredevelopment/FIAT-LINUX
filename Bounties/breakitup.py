while True:
    numberinputstring = input('give a number between 0 and 999:  ')
    numint = int(numberinputstring)
    new = list(numberinputstring)
    if numint <= 0 or len(new) > 3:
        print('thats not a number I can handle')
    elif len(new) == 3:
        print ('{}00+{}0+{}={}'.format(new[-3], new[-2], new[-1], numberinputstring))
    elif len(new) == 2:
        print('{}0+{}={}'.format(new[-2], new[-1], numberinputstring))
    elif len(new) == 1:
        print('{}={}'.format(new[-1], numberinputstring))
    else:
        print ('thats not a number I can handle')
