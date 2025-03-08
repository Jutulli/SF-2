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

#Coordinate Info
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

def isBoardOrdered(board):
    tile_amount = dimensions*dimensions - 1
    last_num = 0
    for collumn in board:
        for number in collumn:
            if last_num < tile_amount and number != last_num + 1: 
                return False
            last_num = number

    return True
        
def getAvailableMovesAtPosition(board, position):
    available_moves = []
    for key in movementDirections.keys():
        direction = movementDirections[key]
        if 0 <= position[0] + direction[0] < (dimensions) and 0 <= position[1] + direction[1] < (dimensions):
            available_moves.append(key)
    return available_moves

def getMovementString(available_moves):
    middle_string = "Enter WASD (or QUIT):"
    top_string = (" " * len(middle_string)) + "\t\tW\n"
    bottom_string = "\tA\tS\tD "

    for key in movementDirections.keys():
        if not key in available_moves:
            top_string = top_string.replace(key, "()")
            bottom_string = bottom_string.replace(key, "()")

    return top_string + middle_string + bottom_string

def nextMove(board, moves_remaining: int):
    blank_position = findEmptytile(board)
    available_moves = getAvailableMovesAtPosition(board, blank_position)

    print("MOVES REMAINING: " + str(move_amount))
    print(getMovementString(available_moves))

    playInput = input().upper()
    if playInput == "QUIT": sys.exit()
    elif not playInput in available_moves: return

    #Code for switching positions
    movement = movementDirections.get(playInput)

    x_object_position = blank_position[0] + movement[0]
    y_object_position = blank_position[1] + movement[1]

    valueAtPosition = board[x_object_position][y_object_position]
    board[blank_position[0]][blank_position[1]] = valueAtPosition
    board[x_object_position][y_object_position] = '  '

    return True

board = getNewPuzzle(dimensions)

while True:
    displayBoard(board)

    if nextMove(board, move_amount): 
        move_amount -= 1

    if isBoardOrdered(board):
        print("----------------------------------------")
        print("YOU WON, GREAT JOB GOAT !")
        sys.exit()
    elif move_amount == 0:
        print("----------------------------------------")
        print("You lost fella, best of luck next time !")
        sys.exit()
    
