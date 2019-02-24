# Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. 
# Note that the puzzle represented by grid does not have to be solvable.
# Problem Link: https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn
def sudoku2(grid):
    checkValues = lambda Array: len(Array)==len(set(Array))
    tgrid = [[row[i] for row in grid] for i in range(9)]
    checkRows = any([not(checkValues([grid[i][j] for i in range(9) if grid[i][j]!='.'])) for j in range(9)])
    checkColumns = any([not(checkValues([tgrid[i][j] for i in range(9) if tgrid[i][j]!='.'])) for j in range(9)])
    checkSubgrids = any([not(checkValues([grid[i+3*(k//3)][j+3*(k%3)] for i in range(3) for j in range(3) 
    if grid[i+3*(k//3)][j+3*(k%3)]!='.'])) for k in range(9)])
    return not(checkRows or checkColumns or checkSubgrids)