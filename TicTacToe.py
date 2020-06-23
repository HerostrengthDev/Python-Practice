#! python3

import pprint

theBoard = {'TL': ' ', 'TM': ' ', 'TR': ' ','L': ' ', 'M': ' ', 'R': ' ','BL': ' ', 'BM': ' ', 'BR': ' '}
def printBoard(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('------')
    print(board['L'] + '|' + board['M'] + '|' + board['R'])
    print('------')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def tictactoe():

    player =  input()

    for turn in range(10):
        printBoard(theBoard)
        print(f"Turn {turn + 1}. \nIt's {player}'s turn")
        choice = input()
        theBoard[choice] = player
        if turn > 5:
            if theBoard['TR'] == theBoard['TM'] == theBoard['TL'] or \
                theBoard['R'] == theBoard['M'] == theBoard['L'] or\
                theBoard['BR'] == theBoard['BM'] == theBoard['BL'] or\
                theBoard['BR'] == theBoard['R'] == theBoard['TR'] or \
                theBoard['BM'] == theBoard['M'] == theBoard['TM'] or\
                theBoard['BL'] == theBoard['L'] == theBoard['TL'] or\
                theBoard['TR'] == theBoard['M'] == theBoard['BL'] or \
                theBoard['TL'] == theBoard['M'] == theBoard['BR']:
                printBoard(theBoard)
                print(player + ' wins!')
                break
        if turn == 8:
            print("It's a tie!")
            break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        turn += turn

print('Welcome to tic tac toe!\nDo you wish to play as X or O?')

tictactoe()

