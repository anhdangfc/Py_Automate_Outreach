import time
import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def player_choose_turn():
    print('You wanna play with \'X\' or \'O\'')
    player_turn = input().upper()
    if player_turn not in ['X', 'O']:
        player_turn = 'O'
    print('Your move would be: \'{}\''.format(player_turn))
    return player_turn


def print_board(board):
    print()
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('-+-+-')


def available_action(board):
    possible_action = []
    for i in board.keys():
        if board[i] == ' ':
            possible_action.append(i)
    return possible_action


def anyone_win(board, computer_ch, player_ch):
    # horizon
    scene1 = ((board['top-L'] == board['top-M']) & (board['top-L'] == board['top-R']))
    if scene1:
        if board['top-L'] == computer_ch:
            result = 'Computer wins. Muahahaha'
        elif board['top-L'] == player_ch:
            result = 'Human wins. Congrats|||'
        else:
            result = 0
        return result
    scene2 = ((board['mid-L'] == board['mid-M']) & (board['mid-L'] == board['mid-R']))
    if scene2:
        if board['mid-L'] == computer_ch:
            result = 'Computer wins. Muahahaha'
        elif board['mid-L'] == player_ch:
            result = 'Human wins. Congrats'
        else:
            result = 0
        return result
    scene3 = ((board['low-L'] == board['low-M']) & (board['low-L'] == board['low-R']))
    if scene3:
        if board['low-L'] == computer_ch:
            result = 'Computer wins. Muahahaha'
        elif board['low-L'] == player_ch:
            result = 'Human wins. Congrats'
        else:
            result = 0
        return result
    # vertical
    scene4 = ((board['top-L'] == board['mid-L']) & (board['top-L'] == board['low-L']))
    if scene4:
        if board['top-L'] == computer_ch:
            result = 'Computer wins. Muahahaha'
        elif board['top-L'] == player_ch:
            result = 'Human wins. Congrats'
        else:
            result = 0
        return result
    scene5 = ((board['top-M'] == board['mid-M']) & (board['top-M'] == board['low-M']))
    if scene5:
        if board['top-M'] == computer_ch:
            result = 'Computer wins. Muahahaha'
        elif board['top-M'] == player_ch:
            result = 'Human wins. Congrats'
        else:
            result = 0
        return result
    scene6 = ((board['top-R'] == board['mid-R']) & (board['top-R'] == board['low-R']))
    if scene6:
        if board['top-R'] == computer_ch:
            result = 'Computer wins. Muahahaha'
        elif board['top-R'] == player_ch:
            result = 'Human wins. Congrats'
        else:
            result = 0
        return result
    # diagnol
    scene7 = ((board['top-L'] == board['mid-M']) & (board['top-L'] == board['low-R']))
    if scene7:
        if board['top-L'] == computer_ch:
            result = 'Computer wins. Muahahaha'
        elif board['top-L'] == player_ch:
            result = 'Human wins. Congrats'
        else:
            result = 0
        return result
    scene8 = ((board['top-R'] == board['mid-M']) & (board['top-R'] == board['low-L']))
    if scene8:
        if board['top-R'] == computer_ch:
            result = 'Computer wins. Muahahaha'
        elif board['top-R'] == player_ch:
            result = 'Human wins. Congrats'
        else:
            result = 0
        return result
    return 0


# Assign the move for human and computer
player = player_choose_turn()
if player == 'X':
    computer = 'O'
else:
    computer = 'X'

turn = computer  # computer goes first

# Game sequence start!
print()
print('Game Start!')
move = 0
for i in range(9):
    print_board(theBoard)  # refresh every time moves made
    print()
    possibleMoves = available_action(theBoard)
    result_update = anyone_win(theBoard, computer, player)
    if result_update != 0:
        # print('-------------------')
        # print(result_update)
        # print('-------------------')
        break
    # computer move
    if turn == computer:
        print('---------- Sequence: {} --------------'.format(i))
        print('Turn for Computer. Muahahahaha...')
        computer_move = random.choice(possibleMoves)
        theBoard[computer_move] = computer
        time.sleep(0.7)
        print('Computer plays ' + computer_move)
    else:
        print('---------- Sequence: {} ---------------'.format(i))
        print('Turn for Human. Move to which space?')
        print(possibleMoves)
        while move not in possibleMoves:
            print('Turn for Human. Move to which space?')
            move = input()
        theBoard[move] = player
        print('Human play' + move)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print('---------- Ending ---------------')
print_board(theBoard)
print('-----------------------------')
result_update = anyone_win(theBoard, computer, player)
if result_update == 0:
    print('Finished! Human vs. Computer: Even')
else:
    print(result_update)
    print('Game Finished! Happy? :D')

print('------------------------------')




