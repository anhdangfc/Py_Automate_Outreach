import random, sys

while True:
    print("Type [1] to play the BLIND GUESS game. \n Type ['EXIT'] to exit the game.")
    response = input()

    if response == 'EXIT':
        sys.exit()
    elif response == '1':
        print('---- BLIND GUESS GAME ----')
        print('The game will draw a random number from 1 to 100 \n You will have 3 guesses.')
        print()
        print('First guess, choose between 0 and 100:')
        guess_1 = input()
        print('Second guess, choose between 0 and 100:')
        guess_2 = input()
        print('Third guess, choose between 0 and 100:')
        guess_3 = input()
        print()

        # group all 3 guesses
        guess_nums = [guess_1, guess_2, guess_3]
        for ix in range(len(guess_nums)):
            print('Your guess no.{0} is: {1}'.format(ix + 1, guess_nums[ix]))
        print()

        # draw the random number
        result = random.randint(1, 100)
        if result in guess_nums:
            print('Bingo! You\'re right! Random num is: ' + str(result))
        else:
            print('WRONG! Random num is: ' + str(result))
    else:
        print('Your response: ' + response + '. Do not know how to react')