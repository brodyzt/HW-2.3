import copy
import types
from enum import Enum

class Matrix_type(Enum):
        scalar = 1
        horizontal_vector = 2
        vertical_vector = 3
        matrix = 4

class Matrix:


    #following function returns a reflected version of the input grid
    def __init__(self, grid):
        self.grid = grid

    #returns a grid reflected over a line from top left to bottom right
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
            for x in range(len(row)):
                tempStr = tempStr + str(row[x]) + (',' if x != (len(row) - 1) else '')
            tempStr = tempStr + ']'
            print(tempStr)

    def type(input):
        if((type(input) is int or type(input) is float) or (len(input.grid) == 1 and len(input.grid[0]) == 1)):
            return Matrix_type.scalar
        elif(type(input.grid) is list and type(input.grid[0]) is not list):
            return Matrix_type.horizontal_vector
        elif(type(input.grid) is list and len(input.grid[0]) == 1):
            return Matrix_type.vertical_vector
        elif(type(input.grid) is list and len(input.grid[0]) > 1):
            return Matrix_type.matrix


    def vector_matrix_multiply(matrix_a,matrix_b):
        if(type(matrix_a[0]) is not list):
            temp_matrix = []
            temp_row = []
            dot_product = 0
            for m_1_x in range(len(matrix_a)):
                dot_product += matrix_a[m_1_x] * matrix_b[m_1_x][0]
            temp_row.append(dot_product)
            temp_matrix.append(temp_row)
        elif(type(matrix_b[0]) is not list):
            temp_matrix = []
            for m_1_y in range(len(matrix_a)):
                temp_row = []
                for m_2_x in range(len(matrix_b)):
                    dot_product = 0
                    for m_1_x in range(len(matrix_a[m_1_y])):
                        dot_product += int(matrix_a[m_1_y][m_1_x]) * int(matrix_b[m_2_x])
                    temp_row.append(dot_product)
                temp_matrix.append(temp_row)
        return Matrix(temp_matrix)

    def scalar_matrix_multiply(scalar, matrix_a):
        temp_matrix = []
        for row in matrix_a.grid:
            temp_row = []
            for item in row:
                temp_row.append(item * scalar)
            temp_matrix.append(temp_row)
        return Matrix(temp_matrix)

    #multiples the two input matrices and returns the product
    def multiply(matrix_a, matrix_b):
        temp_matrix = []
        if(Matrix.type(matrix_a) == Matrix_type.scalar and Matrix.type(matrix_b) == Matrix_type.matrix):
            temp_matrix = Matrix.scalar_matrix_multiply(matrix_a,matrix_b).grid
        elif((Matrix.type(matrix_a) == Matrix_type.horizontal_vector or Matrix.type(matrix_a) == Matrix_type.vertical_vector) and Matrix.type(matrix_b) == Matrix_type.matrix):
            temp_matrix = Matrix.vector_matrix_multiply(matrix_a,matrix_b).grid
        else:
            for m_1_y in range(len(matrix_a.grid)):
                temp_row = []
                for m_2_x in range(len(matrix_b.grid[0])):
                    dot_product = 0
                    for m_1_x in range(len(matrix_a.grid[m_1_y])):
                        dot_product += float(matrix_a.grid[m_1_y][m_1_x]) * float(matrix_b.grid[m_1_x][m_2_x])
                    temp_row.append(dot_product)
                temp_matrix.append(temp_row)
        return Matrix(temp_matrix)

    def divide(matrix_a,matrix_b):
        return Matrix.multiply(1/matrix_b,matrix_a)

    #adds the two input matrices and returns the sum
    def add(matrix_a, matrix_b):
        temp_matrix = []
        if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
            for row in range(len(matrix_a)):
                temp_row = []
                for column in range(len(matrix_a[0])):
                    temp_row.append(matrix_a[row][column] + matrix_b[row][column])
                temp_matrix.append(temp_row)
        return Matrix(temp_matrix)

    #subtracts the second input matrix from the first and returns the difference
    def subtract(matrix_a, matrix_b):
        temp_matrix = []
        if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
            for row in range(len(matrix_a)):
                temp_row = []
                for column in range(len(matrix_a[0])):
                    temp_row.append(matrix_a[row][column] - matrix_b[row][column])
                temp_matrix.append(temp_row)
        return Matrix(temp_matrix)

    def divide(matrix_a,matrix_b):
        pass
'''
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

#prints the product of the original grid and its reflection
print('\nThe following is the product of the original grid and the reflection of the original grid')
Matrix.multiply(user_grid, user_grid.reflect()).print()'''

matrix1 = Matrix([[1,5],[10,10],[40,5]])
matrix2 = Matrix([[4,1],[4,6],[3,7]])
Matrix.multiply(matrix1,matrix2).print()