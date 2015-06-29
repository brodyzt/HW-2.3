#following function returns a reflected version of the input grid
def reflectedGrid(grid):
    reflected = []
    for x in range(len(grid[0])):
        tempGrid = []
        for y in range(len(grid)):
            tempGrid.append(grid[y][x])
        reflected.append(tempGrid)
    return reflected

#returns a grid without horizontal repeats
def gridWithoutHorizontalRepeats(grid):
    tempGrid = []
    for row in grid:
        tempSubGrid = []
        for item in row:
            if(tempSubGrid.__contains__(item) == False):
                tempSubGrid.append(item)
        tempGrid.append(tempSubGrid)
    return tempGrid

#formats and prints the input grid
def printGrid(grid):
    for row in grid:
        tempStr = '[ '
        for item in row:
            tempStr = tempStr + item + ' '
        tempStr = tempStr + ']'
        print(tempStr)

#creates an empty grid that will be used to store user input
grid = []

#takes 4 lines of user input and splits the lines by ',' to form a grid, lists inside of lists
for _ in range(4):
    grid.append(raw_input().split(','))

#prints (a): the original grid
print('\nThe Following is part (a), the original grid:')
printGrid(grid)

#prints (b): the reflected grid
print('\nThe Following is part (b), the original grid reflected over the diagonal running from top left to bottom right:')
printGrid(reflectedGrid(grid))

#prints (c): Both versions of the grid with horizontal repeats removed
print('\nThe Following is part (c):')

print('The original grid with repeats removed:')
printGrid(gridWithoutHorizontalRepeats(grid))

print('The reflected grid with repeats removed:')
printGrid(gridWithoutHorizontalRepeats(reflectedGrid(grid)))
