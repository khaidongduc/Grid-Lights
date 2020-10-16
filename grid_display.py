## A helper function that displays a grid of differently colored
## cell. The grid should be represented as a list of lists. The
## elements of the inner lists (i.e., the cells) are represented as
## numbers between 0 and 10. Each number gets mapped to a specific
## color.
##
## The number to color mapping is as follows:
##  0 -> white
##  1 -> gold 
##  2 -> orange
##  3 -> red
##  4 -> dark red
##  5 -> medium violet red
##  6 -> midnight blue
##  7 -> sea green
##  8 -> dark green
##  9 -> black
##

import pygame


def run_display(grid, cell_size, on_click):
    """
    This function takes a grid (represented as a list of lists) where
    each cell holds a number between 0 and 9 and the desired cell_size
    in pixels and displays this grid on the screen graphically. Each
    cell number gets translated into a color.

    The third parameter is the name of a function that specifies what
    should be done when there is a mouse click somewhere in the
    grid. The function on_click should take three parameters, the grid
    and two numbers identifying the clicked cell by its row and column
    value and it should return a (potentially updated) copy of the
    grid.
    """
    pygame.init()
    margin = 2
    width = 200
    height = 200

    if len(grid) > 0:
        height = len(grid) * (cell_size + margin) + margin
        if len(grid[0]) > 0:
            width = len(grid[0]) * (cell_size + margin) + margin

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    keepGoing = True
    while (keepGoing):

        dt = clock.tick()

        # go through all events that happened and check ...
        for event in pygame.event.get():
            # ... whether the event was a quit event
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                col = int((mousex - margin) / (cell_size + margin))
                row = int((mousey - margin) / (cell_size + margin))
                # on mouse click call event handler function on_click
                grid = on_click(grid, row, col)

        # draw everything
        screen.fill(pygame.color.Color("plum"))

        x = margin
        y = margin
        for row in grid:
            for cell in row:
                pygame.draw.rect(screen, decode_color(cell), (x, y, cell_size, cell_size))
                x += cell_size + margin
            y += cell_size + margin
            x = margin

        pygame.display.update()

    pygame.quit()


def decode_color(number):
    if number == 0:
        return pygame.color.Color("white")
    elif number == 1:
        return pygame.color.Color("gold")
    elif number == 2:
        return pygame.color.Color("orange")
    elif number == 3:
        return pygame.color.Color("red")
    elif number == 4:
        return pygame.color.Color("darkred")
    elif number == 5:
        return pygame.color.Color("mediumvioletred")
    elif number == 6:
        return pygame.color.Color("midnightblue")
    elif number == 7:
        return pygame.color.Color("seagreen")
    elif number == 8:
        return pygame.color.Color("darkgreen")
    elif number == 9:
        return pygame.color.Color("black")
