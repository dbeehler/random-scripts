import random
fullBoard = [['I','I','I'],['I','I','I'],['I','I','I']]

#TO DO
#Probably fix win checker more
#add something to see if all pieces are filled with no winner
#Random start (Comp can start (50/50 chance))


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
            fullBoard[yRand-1][xRand-1]="O"
            print(xRand-1,yRand-1)
            placement = True
        else:
            placement = False


def displayBoard():
    for element in fullBoard:
        print(element)

#win check be like "I broken"
def checkWin(board):
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2]:
            if board[row][0]=='X' and board[row][1]=='X' and board[row][2]=='X':
                print("winner by row player")
                return True
            elif board[row][0]=='O' and board[row][1]=='O' and board[row][2]=='O':
                print("winner by row comp")
                return True
            else:
                return False

    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]:
            if board[0][col]== 'X' and board[1][col]=='X' and board[2][col]=='X':
                print("Winner by col player")
                return True
            elif board[0][col]== 'O' and board[1][col]=='O' and board[2][col]=='O':
                print("Winner by col comp")
                return True
            else:
                return False

    if board[0][0]==board[1][1]==board[2][2]:
        if board[0][0] == 'X':
            print("Winner by diag1 player")
            return True
        elif board[0][0] == 'O':
            print("Winner by diag1 comp")
            return True
        else:
            return False

    if board[0][2]==board[1][1]==board[2][0]:
        if board[0][2] == 'X':
            print("Winner by diag2 player")
            winner = "Player"
            return True
        elif board[0][2] == 'O':
            print("Winner by diag2 comp")
            winner = "Computer"
            return True
        else:
            return False
    return False

winner = False
while(winner==False):
    try:
        playerMove(int(input("Enter X axis: ")), int(input("Enter y axis: ")))
    except Exception as e:
        print(e)
        print("bad move, please try again")
        continue
    computerMove()
    displayBoard()
    winner=checkWin(fullBoard)