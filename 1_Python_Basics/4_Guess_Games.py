import random
import sys


def compare_message(guess, result):  # write the function for repeated tasks
    if guess > result:
        if result > 10:
            bot_line = result - random.randint(1, 10)  # add a bottom line to make the game easier
        else:
            bot_line = 0
        print('Guess some smaller number than your previous try, but larger than {0}.'.format(bot_line))
    elif guess < result:
        if result < 90:
            top_line = result + random.randint(1, 10)  # add a bottom line to make the game easier
        else:
            top_line = 100
        print('Guess some bigger number than your previous guess. But, smaller than {0}.'.format(top_line))


# START the program
while True:
    option1 = 'Type [1] to play the BLIND GUESS game.'
    option2 = 'Type [2] to play the SMART GUESS game.'
    option3 = 'Type [3] to play Rock-Paper-Scissors game.'
    option4 = 'Type [\'EXIT\'] to exit the game.'
    print('{0} \n {1} \n {2} \n {3}'.format(option1, option2, option3, option4))
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

    elif response == '2':
        print('---- SMART GUESS GAME ----')
        print('The game will draw a random number from 1 to 100 \n You will have 3 guesses.')
        print('After each guess, you will have the hint to make a better guess next time')
        print()
        result = random.randint(1, 100)

        print('First guess, choose between 0 and 100:')  # Guess 1
        guess_1 = int(input())
        if guess_1 == result:  # Guess 1 right
            print('Bingo! You\'re right! Random num is: ' + str(result))
        else:  # Guess 1 wrong
            compare_message(guess_1, result)  # Hint
            print('Second guess, choose between 0 and 100:')  # Guess 2
            guess_2 = int(input())
            if guess_2 == result:  # Guess 2 right
                print('BINGO! You\'re right! Random num is: ' + str(result))
            else:
                compare_message(guess_2, result)  # Guess 2 wrong
                print('Third guess, choose between 0 and 100:')
                guess_3 = int(input())  # Guess 3
                if guess_3 == result:
                    print('BINGO! You\'re right! Random num is: ' + str(result))  # Guess 3 right
                else:
                    print('WRONG! Random num is: ' + str(result))  # Guess 3 wrong
    elif response == '3':
        print('---- ROCK, PAPER, SCISSOR ----')
        print('Input your option with one of Rock - Paper - Scissors')
        print('\'r\' for Rock \n \'p\' for Paper \n \'s\' for Scissors')
        choice = input()
        result = random.choice(['r', 'p', 's'])  # rock, paper, scissor
        map_dict = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

        if choice == result:
            print('EVEN. Your choice: {0}. Computer\'s choice: {1}'.format(choice, result))
        # win cases
        elif (choice == 'r' and result == 's') or (choice == 'p' and result == 'r') or (choice == 's' and result == 'p'):
            print('WIN! Your choice: {0}. Computer\'s choice: {1}'.format(map_dict[choice], map_dict[result]))
        # lose case
        else:
            print('LOSE! Your choice: {0}. Computer\'s choice: {1}'.format(map_dict[choice], map_dict[result]))
        print()
    else:
        print('Your response: ' + response + '. Do not know how to react')
