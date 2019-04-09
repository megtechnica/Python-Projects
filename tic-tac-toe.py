the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
            'mid-L': ' ', 'mid-M' : ' ', 'mid-R' : ' ',
            'Low-L': ' ', 'Low-M': ' ', 'Low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['Low-L'] + '|' + board['Low-M'] + '|' + board['Low-R'])
    print(printBoard)

turn = "X"

for i in range(9):
    printBoard(the_board)
    print('Turn for ' + turn + '.  Move on which space?')
    move = input()
    the_board[move] = turn
    if turn == "X":
        turn = "O"
    else: 
        turn = "X"

printBoard(the_board)
