import numpy as np


def start_new_game():
    done = False
    # print("press Enter\n\n")
    print("\nNew game")
    while not done:

        penalty = 0
        listhm = []  # Create a list for the correct guesses

        check = 0
        gmandict = ['hangman', 'mississippi', 'miscellaneous', 'santabarbara', 'alhambrahigh']
        r = np.random.randint(1, len(gmandict))
        word = gmandict[r]  # the word chosen from  the dictionary
        for i in range(len(word)):  # Populate list of word to be guessed with "*" for each letter
            listhm.insert(i, "_")

        print(' '.join(listhm))
        while penalty < 7:

            k = 0
            # input your guess letter guess_letter

            guess_letter = input("Input a letter\n")

            # verify whether the new string has more than one character.
            if len(guess_letter) == 1:

                # verify whether the new letter was used earlier.

                for i in range(len(word)):
                    if guess_letter == listhm[i]:  # You have used this letter already

                        k = 1
                if k > 0:
                    penalty = penalty + 1
                    print("You have used already this letter. Your penalty =", penalty)
                    penaltyDraw(penalty)
                    k = 0
                else:
                    k = 0

                for i in range(len(word)):

                    if guess_letter == word[
                        i]:  # if guess_letter is in the word, then replace the "*" with the correct guess
                        temp = word[i]
                        listhm[i] = temp
                        check = check + 1  # Variable counting how many correct guesses are
                        k = 1
                if k > 0:
                    k = 0
                else:
                    penalty = penalty + 1
                    print("Wrong letter, your penalty is =", penalty)
                    penaltyDraw(penalty)
            elif guess_letter == word:
                print(word, 'is correct!')
                print("You guessed the word with a loooong shot! Your penalty is ", penalty)
                # print(guess_letter,"\n\n", word,"\n\n" ,listhm)
                # print("Press Enter to play a new game")
                start_new_game()

            else:
                penalty = penalty + 1
                print("You have a very looong letter! Penalty =", penalty)
                penaltyDraw(penalty)

            print(' '.join(listhm))  # Display the new list with the letters you correctly guessed
            if len(word) == check:  # If all letters were correctly guessed, end the game
                print(word)
                print("You guessed the word! Your penalty is ", penalty)

                input("\n\nPress Enter to start a new  game\n\n Here")

                start_new_game()

        if penalty == 7:
            print("Game Over - you  lost the game for having 7 penalties ")
            print(word)
            input("\n\nPress Enter to start a new  game\n\n Here")
            start_new_game()

    return


def penaltyDraw(penalty):
    penaltyTotal = 7
    if penalty == 1:
        # draw gallows
        print('you have ', penaltyTotal - penalty, 'guesses left\n')
        print('  ===========    ')
        print('  ||/       |    ')
        print('  ||             ')
        print('  ||             ')
        print('  ||             ')
        print('  ||             ')
        print('  ||             ')
        print(',,||,,,,,,,,,,,,,')
        print('\n')
    elif penalty == 2:
        # draw head
        print('you have ', penaltyTotal - penalty, 'guesses left\n')
        print('  ===========    ')
        print('  ||/       |    ')
        print('  ||       ()    ')
        print('  ||             ')
        print('  ||             ')
        print('  ||             ')
        print('  ||             ')
        print(',,||,,,,,,,,,,,,,')
        print('\n')
    elif penalty == 3:
        # draw body
        print('you have ', penaltyTotal - penalty, 'guesses left\n')
        print('  ===========    ')
        print('  ||/       |    ')
        print('  ||       ()    ')
        print('  ||        |    ')
        print('  ||        |    ')
        print('  ||             ')
        print('  ||             ')
        print(',,||,,,,,,,,,,,,,')
        print('\n')
    elif penalty == 4:
        # draw left arm
        print('you have ', penaltyTotal - penalty, 'guesses left\n')
        print('  ===========    ')
        print('  ||/       |    ')
        print('  ||       ()    ')
        print('  ||       \|    ')
        print('  ||        |    ')
        print('  ||             ')
        print('  ||             ')
        print(',,||,,,,,,,,,,,,,')
        print('\n')
    elif penalty == 5:
        # draw right arm
        print('you have ', penaltyTotal - penalty, 'guesses left\n')
        print('  ===========    ')
        print('  ||/       |    ')
        print('  ||       ()    ')
        print('  ||       \|/   ')
        print('  ||        |    ')
        print('  ||             ')
        print('  ||             ')
        print(',,||,,,,,,,,,,,,,')
        print('\n')
    elif penalty == 6:
        # draw left leg
        print('you have ', penaltyTotal - penalty, 'guesses left\n')
        print('  ===========    ')
        print('  ||/       |    ')
        print('  ||       ()    ')
        print('  ||       \|/   ')
        print('  ||        |    ')

        print('  ||      ,/     ')
        print('  ||             ')
        print(',,||,,,,,,,,,,,,,')
        print('\n')
    elif penalty == 7:
        # draw right leg
        print('you have ', penaltyTotal - penalty, 'guesses left\n')
        print('  ===========    ')
        print('  ||/       |    ')
        print('  ||       ()    ')
        print('  ||       \|/   ')
        print('  ||        |    ')
        print('  ||      ,/ \,  ')
        print('  ||             ')
        print(',,||,,,,,,,,,,,,,')
        print('\n')
    return


input("\n\nPress Enter to start a new  game\n\n Here")
start_new_game()
