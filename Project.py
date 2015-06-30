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
        tempStr = '['
        for item in row:
            tempStr = tempStr + str(item) + (',','')[row.index(item) == len(row) - 1]
        tempStr = tempStr + ']'
        print(tempStr)

def matrix_multiply(matrix_a, matrix_b):
    temp_matrix = []
    for m_1_y in range(len(matrix_a)):
        temp_row = []
        for m_2_x in range(len(matrix_a)):
            dot_product = 0
            for m_1_x in range(len(matrix_a[m_1_y])):
                dot_product += int(matrix_a[m_1_y][m_1_x]) * int(matrix_b[m_1_x][m_2_x])
            temp_row.append(dot_product)
        temp_matrix.append(temp_row)
    return temp_matrix

#prompts user for grid specifications
row = int(input('How many rows would you like the grid to have: '))
print('Please enter the contents of each row with each item separated by a ","')

#creates an empty grid that will be used to store user input
grid = []

#takes 4 lines of user input and splits the lines by ',' to form a grid, lists inside of lists
for _ in range(row):
    grid.append(input("Enter row {0}: ".format(_ + 1)).split(','))

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

#prints the product of the original grid and its reflection
print('\nThe following is the product of the original grid and the reflection of the original grid')
printGrid(matrix_multiply(grid,reflectedGrid(grid)))