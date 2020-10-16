
# A version of "Lights Out" - http://en.wikipedia.org/wiki/Lights_Out_%28game%29

import random
from grid_display import run_display

# Use colors 2 and 4 for the on and off states.
ON = 2
OFF = 4
# The grid should be 5 columns by 5 rows.
SIZE = 5
# The difference between the chosen block and neighbour block

def run_lights():
    """
    Create the initial representation of the grid and start the
    display.
    """
    grid = [[random.choice([ON, OFF]) for j in range(SIZE)] for i in range(SIZE)]
    print(grid)
    # start display
    cell_size = 40
    run_display(grid, cell_size, on_click)


def toggle(grid, row, col):
    if ((0 <= row < SIZE) and (0 <= col < SIZE)):
        grid[row][col] = (ON + OFF) - grid[row][col]

def on_click(grid, row, col):
    """
    This function gets called when there was a mouse click somewhere
    in the grid. The parameters give you the grid and the row and
    column the click was in. (Row and column identify one cell in the
    grid.)

    This function toggles the status of the clicked cell as well as
    its four neighboring cells.
    """
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    print(row, col)
    toggle(grid, row, col)
    for i in range(4):
        toggle(grid, row + dx[i], col + dy[i])
    return grid


run_lights()
