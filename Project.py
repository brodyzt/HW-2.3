#following function returns a reflected version of the input grid
def reflectedGrid(grid):
    reflected = []
    for x in range(len(grid[0])):
        tempGrid = []
        for y in range(len(grid)):
            tempGrid.append(grid[y][x])
        reflected.append(tempGrid)
    return reflected

def gridWithoutHorizontalRepeats(grid):
    tempGrid = []
    for row in grid:
        tempSubGrid = []
        for item in row:
            if(tempSubGrid.__contains__(item) == False):
                tempSubGrid.append(item)
        tempGrid.append(tempSubGrid)
    return tempGrid

def printGrid(grid):
    for row in grid:
        tempStr = '[ '
        for item in row:
            tempStr = tempStr + item + ' '
        tempStr = tempStr + ']'
        print(tempStr)

grid = []

for _ in range(4):
    grid.append(raw_input().split(','))

#prints (a): the original grid
'''print('\nThe Following is part (a), the original grid:')
for row in grid:
    print('[ {0} {1} {2} {3} {4} ]'.format(row[0],row[1],row[2],row[3],row[4]))'''
printGrid(grid)
'''
#prints (b): the reflected grid
print('\nThe Following is part (b), the original grid reflected over the diagonal running from top left to bottom right:')
for row in reflectedGrid(grid):
    print('[ {0} {1} {2} {3} ]'.format(row[0],row[1],row[2],row[3]))

#prints (c): Both versions of the grid with horizontal repeats removed
print('\nThe Following is part (c):\n')

print('The original grid with repeats removed:')
for row in gridWithoutHorizontalRepeats(grid):
    tempStr = '[ '
    for item in row:
        tempStr = tempStr + item + ' '
    tempStr = tempStr + ']'
    print(tempStr)

print('The reflected grid with repeats removed:')
for row in gridWithoutHorizontalRepeats(reflectedGrid(grid)):
    print('[ {0} {1} {2} {3} ]'.format(row[0],row[1],row[2],row[3]))
'''