import random
fullBoard = [['I','I','I'],['I','I','I'],['I','I','I']]
winner = ""

def badPiece(x,y):
    if fullBoard[y-1][x-1] == 'X' or fullBoard[y-1][x-1] == 'O':
        return True
    else:
        return False

def playerMove(x, y):
    if not badPiece(x,y):
        fullBoard[y-1][x-1]="X"
    else:
        raise Exception

def computerMove():
    placement = False
    while(not placement):
        xRand = random.randint(1,3)
        yRand = random.randint(1,3)
        if not badPiece(xRand,yRand):
            fullBoard[xRand-1][yRand-1]="O"
            print(yRand,xRand)
            placement = True
        else:
            placement = False


def displayBoard():
    for element in fullBoard:
        print(element)

#win check be like "I broken"
def checkWin(board):
    for row in range(0,2):
        if board[row][0]==board[row][1]==board[row][2]:
            if board[row][0] == 'X':
                return True
            elif board[row][0] == 'O':
                return True
            else:
                return False
    for col in range(0,2):
        if board[0][col]==board[1][col]==board[2][col]:
            if board[0][col] == 'X':
                return True
            elif board[0][col] == 'O':
                return True
            else:
                return False
    if board[0][0]==board[1][1]==board[2][2]:
        if board[0][0] == 'X':
            return True
        elif board[0][0] == 'O':
            return True
        else:
            return False
    if board[0][2]==board[1][1]==board[2][0]:
        if board[0][0] == 'X':
            winner = "Player"
            return True
        elif board[0][0] == 'O':
            winner = "Computer"
            return True
        else:
            return False

winner = False
while(winner==False):
    try:
        playerMove(int(input("Enter X axis: ")), int(input("Enter y axis: ")))
    except:
        print("bad move, please try again")
        continue
    computerMove()
    displayBoard()
    winner = checkWin(fullBoard)
print("Winner decided")