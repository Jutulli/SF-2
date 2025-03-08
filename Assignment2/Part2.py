# Code by Édouard Fortin-Lefrançois
# 2435585
import random
import sys

print("Welcome to the epic matrix game !\nYour goal is to shift the empty space on a board (using WASD) so that all the numbered tiles are in order")
dimensions = int(input("How many dimensions do you want the grid to be?"))
#negative values will result in infinite moves.
move_amount = -1
if dimensions == 3: move_amount = 31
elif dimensions == 4: move_amount = 80

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
    top_string = "\t\tW"
    string = "\tA\tS\tD "

    if position[0] <= 0:
        top_string = top_string.replace("W", "()")

    if position[1] <= 0:
        string = string.replace("A", "()")

    if position[0] >= dimensions - 1:
        string = string.replace("S", "()")

    if position[1] >= dimensions - 1:
        string = string.replace("D", "()")

    return [top_string, string]

def isBoardOrdered(board):
    tile_amount = dimensions*dimensions - 1
    last_num = 0
    for collumn in board:
        for number in collumn:
            if last_num < tile_amount and number != last_num + 1: 
                return False
            last_num = number

    return True

def nextMove(board, moves_remaining: int):
    blank_position = findEmptytile(board)

    display_strings = getMovementStringAtPosition(board, blank_position)

    print("MOVES REMAINING: " + str(move_amount))
    print(" " * len(prompt) + display_strings[0])
    print(prompt + display_strings[1])

    playInput = input().upper()
    if playInput == "QUIT": sys.exit()
    elif not playInput in list(movementDirections.keys()): return

    movement = movementDirections.get(playInput)

    x_object_position = blank_position[0] + movement[0]
    y_object_position = blank_position[1] + movement[1]

    #If the inputs go out of bounds, we skip over to the next input
    if x_object_position >= dimensions or y_object_position >= dimensions: return
    if x_object_position < 0 or y_object_position < 0: return

    valueAtPosition = board[x_object_position][y_object_position]
    board[blank_position[0]][blank_position[1]] = valueAtPosition
    board[x_object_position][y_object_position] = '  '

    return True

board = getNewPuzzle(dimensions)

while True:
    displayBoard(board)
    if nextMove(board, move_amount): move_amount -= 1

    if isBoardOrdered(board):
        print("YOU WON, GREAT JOB GOAT !")
        sys.exit()
    elif move_amount == 0:
        print("----------------------------------------")
        print("You lost fella, best of luck next time !")
        sys.exit()
    
