import copy
class Matrix:
    #following function returns a reflected version of the input grid
    def __init__(self, grid):
        self.grid = grid

    def reflect(self):
        reflected = []
        for x in range(len(self.grid[0])):
            temp_grid = []
            for y in range(len(self.grid)):
                temp_grid.append(self.grid[y][x])
            reflected.append(temp_grid)
        return Matrix(reflected)

    #returns a grid without horizontal repeats
    def remove_horizontal_repeats(self):
        temp_grid = []
        for row in self.grid:
            temp_sub_grid = []
            for item in row:
                if(temp_sub_grid.__contains__(item) == False):
                    temp_sub_grid.append(item)
            temp_grid.append(temp_sub_grid)
        return Matrix(temp_grid)

    #formats and prints the input grid
    def print(self):
        for row in self.grid:
            tempStr = '['
            for item in row:
                tempStr = tempStr + str(item) + (',','')[row.index(item) == len(row) - 1]
            tempStr = tempStr + ']'
            print(tempStr)

    #multiples the two input matrices and returns the product
    def multiply(self,matrix_a, matrix_b):
        temp_matrix = []
        for m_1_y in range(len(matrix_a)):
            temp_row = []
            for m_2_x in range(len(matrix_a)):
                dot_product = 0
                for m_1_x in range(len(matrix_a[m_1_y])):
                    dot_product += int(matrix_a[m_1_y][m_1_x]) * int(matrix_b[m_1_x][m_2_x])
                temp_row.append(dot_product)
            temp_matrix.append(temp_row)
        return self(temp_matrix)

#prompts user for grid specifications
row = int(input('How many rows would you like the grid to have: '))
print('Please enter the contents of each row with each item separated by a ","')

#creates an empty grid that will be used to store user input
user_grid = Matrix([])

#takes 4 lines of user input and splits the lines by ',' to form a grid, lists inside of lists
for _ in range(row):
    temp_row = input("Enter row {0}: ".format(_ + 1)).split(',')
    while _ != 0 and len(temp_row) != len(user_grid.grid[_ - 1]): #checks to make sure row lenths are the same to get a consistent grid
        print('The number of items in each row of the grid must remain consistent. Please reenter this row.')
        temp_row = input("Enter row {0}: ".format(_ + 1)).split(',')
    user_grid.grid.append(temp_row)

#prints (a): the original grid
print('\nThe Following is part (a), the original grid:')
user_grid.print()

#prints (b): the reflected grid
print('\nThe Following is (b), the original grid reflected over the diagonal running from top left to bottom right:')
user_grid.reflect().print()

#prints (c): Both versions of the grid with horizontal repeats removed
print('\nThe Following is part (c):')

print('The original grid with repeats removed:')
user_grid.remove_horizontal_repeats().print()

print('The reflected grid with repeats removed:')
user_grid.reflect().remove_horizontal_repeats().print()
'''
#prints the product of the original grid and its reflection
print('\nThe following is the product of the original grid and the reflection of the original grid')
Matrix.multiply(user_grid, user_grid.reflect()).print()'''