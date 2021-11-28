# This is Conway's Game of Life.
# The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur: 
#    1.Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#    2. Any live cell with two or three live neighbours lives on to the next generation.
#    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
#    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


"""
Now its time to figure out how on earth I want to implement this.

There are really 2 key steps here. 

1. Initialise all of the cells in the grid, setting them to dead/alive respectively. I have no idea how to do this. 

2. For a cell of co-ordinate (x,y) figure out its status depending on the status of its neighbours. 
"""

