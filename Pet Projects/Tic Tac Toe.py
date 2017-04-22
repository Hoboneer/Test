# Tic Tac Toe
import time
grid = ["_" for cells in range(9)]

knots_game = True
player1_turn = True
player2_turn = False
available_cells = 9

GRID_MARKERS = """
[7][8][9]
[4][5][6]
[1][2][3]
"""
"""
For reference; this is what it's like in the code if it was visualised.
Players see the grid differently

[0][1][2]
[3][4][5]
[6][7][8]
"""

WINNING_GRIDS = [
[0, 1, 2],
[3, 4, 5],
[6, 7, 8],
[0, 3, 6],
[1, 4, 7],
[2, 5, 8],
[0, 4, 8],
[2, 4, 6]
]

def display_grid(grid, GRID_MARKERS):
    """
    Assigns what the cells are in the visual and prints them in a 3x3 with the numbered grid afterward as reference for the next cell assignment
    """
    grid_visual = []
    for moves in grid:
        cell = str("[" + moves + "]")
        grid_visual.append(cell)
    print ("This is what the grid looks like:")
    time.sleep(1)
    print (grid_visual[6] + grid_visual[7] + grid_visual[8])
    print (grid_visual[3] + grid_visual[4] + grid_visual[5])
    print (grid_visual[0] + grid_visual[1] + grid_visual[2])
    time.sleep(1)
    print (GRID_MARKERS)

def validate_grid_choice(move, grid, player1_turn, player2_turn, available_cells):
    """
    Checks if the move is valid. If valid, it assigns 'X' or 'O' to the cell they chose depending on which player placed it. If not, it does nothing and tells them to do it again because the opponent's turn isn't set to 'True'
    """
    if grid[move] == "_":
        if player1_turn:
            grid[move] = "X"
            player1_turn = False
            player2_turn = True
        elif player2_turn:
            grid[move] = "O"
            player1_turn = True
            player2_turn = False
        available_cells -= 1
        return grid[move], player1_turn, player2_turn, available_cells
    elif grid[move] != "_":
        if player1_turn:
            player1_turn = True
        elif player2_turn:
            player2_turn = True
        print ("\nInvalid Input")
        return grid[move], player1_turn, player2_turn, available_cells

def check_victory(grid, WINNING_GRIDS, available_cells, player1_turn, player2_turn):
    """
    Called at the start of the game loop (so called once every loop). Checks if a person has 3 in a row or the whole grid is filled (really just the available number of cells [which is 9] is now 0. Then if game should end, it assigns the relevant variables to 'False'
    """
    for cells in WINNING_GRIDS:
        if all(grid[cell] == "X" for cell in cells):
            print ("\n=== Player 1 wins! ===")
            knots_game = False
            player1_turn = False
            player2_turn = False
            break
        elif all(grid[cell] == "O" for cell in cells):
            print ("\n=== Player 2 wins! ===")
            knots_game = False
            player1_turn = False
            player2_turn = False
            break
        else:
            knots_game = True
    if available_cells == 0 and knots_game == True:
        knots_game = False
        player1_turn = False
        player2_turn = False
        print ("\n=== No one won! ===")
    else:
        pass
    return knots_game, player1_turn, player2_turn

print ("The numbers on the grid corresponds to the number that you type to place a marker there")
time.sleep(1)

while knots_game:
    knots_game, player1_turn, player2_turn = check_victory(grid, WINNING_GRIDS, available_cells, player1_turn, player2_turn)
    if player1_turn:
        if available_cells > 0:
            print ("\nPlayer 1 Turn")
            display_grid(grid, GRID_MARKERS)
            move = str(input("Where do you place a mark? "))
            if move.isdigit():
                move = int(move) - 1
                grid[move], player1_turn, player2_turn, available_cells = validate_grid_choice(move, grid, player1_turn, player2_turn, available_cells)
            else:
                print ("\nInvalid Input")
                time.sleep(1)
        else:
            break
    elif player2_turn:
        if available_cells > 0:
            print ("\nPlayer 2 Turn")
            display_grid(grid, GRID_MARKERS)
            move = str(input("Where do you place a mark? "))
            if move.isdigit():
                move = int(move) - 1
                grid[move], player1_turn, player2_turn, available_cells = validate_grid_choice(move, grid, player1_turn, player2_turn, available_cells)
            else:
                print ("\nInvalid Input")
                time.sleep(1)
        else:
            break