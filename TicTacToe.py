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
    turn = '0'

    for turn in range(10):
        printBoard(theBoard)
        print('It is ' + player + 's turn. What is your move?')
        choice = input()
        theBoard[choice] = player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        turn += turn

print('Welcome to tic tac toe! Do you wish to play as X or O?')
tictactoe()


