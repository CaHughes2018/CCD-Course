# Carol's Tic Tac Toe Game - CA in Python - https://gitpod.io/#snapshot/71c8b505-e500-465b-8bd8-2b7247433f4a


board = [' ' for x in range(10)]


def insertBoard(letter, pos):
    global board
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def isWinner(bo, le):
    # This function returns True for whichever player has won.
    # Shorthand for board and letter keeps the code shorter bo,le
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # middle row across
    (bo[1] == le and bo[2] == le and bo[3] == le) or # bottom row across
    (bo[7] == le and bo[4] == le and bo[1] == le) or # left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the centre
    (bo[9] == le and bo[6] == le and bo[3] == le) or # right
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move  = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard('X', move)
                else:
                    print('This postion is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
        

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
    

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    #This is my algorithm, board is cloned so that the original doesn't change used [:]
    #Look for winning move or block opponent
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move


    #Aiming for the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    #Aiming for the centre
    if 5 in possibleMoves:
        move = 5
        return move

    #Try the edges
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def printBoard():
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def main():
    #Main game loop
    print('Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical). The board has positions 1-9 starting at the top left.')
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print('O\'s win this time...')
            break

        
        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Game over and it is a tie!')
            else:
                insertBoard('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard()
        else:
            print('X\'s win, Tidy!')
            break
#Tidy is a comment from Wales, it means great or well done :)

    if isBoardFull(board):
        print('Game over and it is a tie!')

main()

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break