
# print board
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
countX = 0  # count win X
countO = 0  # count win O


def printBoard(arr):
    print(arr[0], "|", arr[1], "|", arr[2])
    print(arr[3], "|", arr[4], "|", arr[5])
    print(arr[6], "|", arr[7], "|", arr[8])

# check winning - return true if we have winning


def isWinner(arr, pl):
    # check 0,1,2
    if(arr[0] == arr[1] and arr[0] == arr[2] and arr[0] == pl):
        return True
    # check 3,4,5
    elif (arr[3] == arr[4] and arr[3] == arr[5] and arr[3] == pl):
        return True
    # check 6,7,8
    elif (arr[6] == arr[7] and arr[6] == arr[8] and arr[6] == pl):
        return True
    # check 0,3,6
    elif(arr[0] == arr[3] and arr[0] == arr[6] and arr[0] == pl):
        return True
    # check 0,4,8
    elif(arr[0] == arr[4] and arr[0] == arr[8] and arr[0] == pl):
        return True
    # check 2,5,8
    elif(arr[2] == arr[5] and arr[2] == arr[8] and arr[2] == pl):
        return True
    # check 1,4,7
    elif(arr[1] == arr[4] and arr[1] == arr[7] and arr[1] == pl):
        return True
    # check 2,4,6
    elif(arr[2] == arr[4] and arr[2] == arr[6] and arr[2] == pl):
        return True
    return False


# check if enable to put X or O
def isEnable(arr, index):
    if(arr[index] == 'X' or arr[index] == 'O'):
        return False
    return True


"""
def teko(arr):
    i=0
    sum = 0
    while(i<len(arr)):
        if(arr[i]=='X' or arr[i]=='O'):
            sum=sum+1
    #return true if teko
    return(i==sum)
"""


def checkNumber(num):
    if(num <= 9 and num >= 1):
        return True
    return False
def resetBoard():
    global board
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def game(startGame):
    global countX
    global countO
    resetBoard()
    cntSteps = 0
    isWinnerCheck = False
    while(cntSteps < 9 and isWinnerCheck == False):
        printBoard(board)
        # input X
        if (cntSteps % 2 == 0):
            x = int(input("Enter X"))
            while(checkNumber(x) == False):
                print("Invalid Number, Press Another Number: ")
                x = int(input())
                checkNumber(x)
            #Check Taken Number
            while(isEnable(board, x-1) == False):
                print("Taken Number Press Anoter Number")
                x = int(input())
            board[x-1] = 'X'
            cntSteps = cntSteps+1
            # check win
            if(isWinner(board, 'X')):
                countX = countX+1
                isWinnerCheck = True
                print("X winner")

        else:
            # input O
            o = int(input("Enter O"))
            while(checkNumber(o) == False):
                print("Invalid Number, Press Another Number: ")
                o = int(input())
                checkNumber(o)
            #Check Taken Number
            while(isEnable(board, o-1) == False):
                print("Taken Number Press Anoter Number")
                o = int(input())
            board[o-1] = 'O'
            cntSteps = cntSteps+1
            if(isWinner(board, 'O')):
                countO = countO+1
                isWinnerCheck = True
                print("O Winner")           
        if(cntSteps == 9):
            printBoard(board)
            # check draw
            if(isWinner(board, 'X') == False and isWinner(board, 'O') == False):
                print("Draw")
            # X winning After 9 steps
            elif(isWinner(board, 'X')):
                countX = countX+1
                print("X Winner")
            else:  # O winning After 9 steps
                countO = countO+1
                print("O Winner")
    
    asnwer = input("Play Again? (Y/N)")
    if(asnwer == 'Y' or asnwer == 'y'):
        game(True)
    else:

        print("Result:\nX:",countX ,"\nO:",countO,"\nThanks For Play")


game(True)
