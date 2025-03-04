import random
import sys

dimensions = int(input("How many dimensions slime?"))

movementDirections = {
    "W": (-1,0),
    "S": (1,0),
    "A": (0, -1),
    "D": (0,1)}


prompt = "Enter WASD (or QUIT): "

def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

def tileLabels(n: int):
    lst = [x for x in range(1, n**2)]
    lst.append('  ')
    return lst

def getNewPuzzle(n: int):
    labels = tileLabels(n)
    random.shuffle(labels)
    return [labels[n*i:n*(i+1)] for i in range(0,n)]

def findEmptytile(board):
    for row in board:
        if '  ' in row:
            return (board.index(row), row.index('  '))
        
def getMovementStringAtPosition(board, position):
    topString = "\t\tW"
    string = "\tA\tS\tD "

    if position[0] <= 0:
        topString = topString.replace("W", "()")

    if position[1] <= 0:
        string = string.replace("A", "()")

    if position[0] >= dimensions - 1:
        string = string.replace("S", "()")

    if position[1] >= dimensions - 1:
        string = string.replace("D", "()")

    return [topString, string]

def nextMove(board):
    blankPosition = findEmptytile(board)

    displayStrings = getMovementStringAtPosition(board, blankPosition)

    print(" " * len(prompt) + displayStrings[0])
    print(prompt + displayStrings[1])

    playInput = input().upper()
    if playInput == "QUIT": sys.exit()
    #EVERYTHING BELOW HERE IS TECHNICALLY FOR PART 2 BUT IT'S NICE FOR TESTING
    movement = movementDirections.get(playInput)

    xObjectPosition = blankPosition[0] + movement[0]
    yObjectPosition = blankPosition[1] + movement[1]

    #If the inputs go out of bounds, we skip over to the next input
    if xObjectPosition >= dimensions or yObjectPosition >= dimensions: return
    if xObjectPosition < 0 or yObjectPosition < 0: return

    valueAtPosition = board[xObjectPosition][yObjectPosition]
    board[blankPosition[0]][blankPosition[1]] = valueAtPosition
    board[xObjectPosition][yObjectPosition] = '  '

board = getNewPuzzle(dimensions)

while True:
    displayBoard(board)
    nextMove(board)

    
