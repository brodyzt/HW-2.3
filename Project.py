from enum import Enum
import copy

class MatrixType(Enum):
    scalar = 1
    horizontal_vector = 2
    vertical_vector = 3
    matrix = 4


class Matrix:
    # following function returns a reflected version of the input grid
    def __init__(self, grid):
        self.grid = grid

    # returns a grid reflected over a line from top left to bottom right
    def reflect(self):
        reflected = []
        for x in range(len(self.grid[0])):
            temp_grid = []
            for y in range(len(self.grid)):
                temp_grid.append(self.grid[y][x])
            reflected.append(temp_grid)
        return Matrix(reflected)

    # returns a grid without horizontal repeats
    def remove_horizontal_repeats(self):
        temp_grid = []
        for row in self.grid:
            temp_sub_grid = []
            for item in row:
                if temp_sub_grid.__contains__(item) is False:
                    temp_sub_grid.append(item)
            temp_grid.append(temp_sub_grid)
        return Matrix(temp_grid)

    # formats and prints the input grid
    def print(self):
        for row in self.grid:
            temp_str = '['
            for x in range(len(row)):
                temp_str += str(row[x]) + (',' if x != (len(row) - 1) else '')
            temp_str += ']'
            print(temp_str)

    def type(input_object):
        if (type(input_object) is int or type(input_object) is float)\
                or (len(input_object.grid) == 1 and len(input_object.grid[0]) == 1):
            return MatrixType.scalar
        elif type(input_object.grid) is list and type(input_object.grid[0]) is not list:
            return MatrixType.horizontal_vector
        elif type(input_object.grid) is list and len(input_object.grid[0]) == 1:
            return MatrixType.vertical_vector
        elif type(input_object.grid) is list and len(input_object.grid[0]) > 1:
            return MatrixType.matrix

    def determinant(self):
        determinant = 0
        if len(self.grid) == 2 and len(self.grid[0]) == 2:
            return self.grid[0][0] * self.grid[1][1] - self.grid[0][1] * self.grid[1][0]
        else:
            for x in range(len(self.grid[0])):
                temp_grid = copy.deepcopy(self.grid)
                for row in temp_grid:
                    row.pop(x)
                temp_grid.pop(0)
                if x % 2 == 0:
                    determinant += self.grid[0][x] * Matrix(temp_grid).determinant()
                else:
                    determinant -= self.grid[0][x] * Matrix(temp_grid).determinant()
        return determinant

    def vector_matrix_multiply(matrix_a, matrix_b):
        temp_matrix = []
        if type(matrix_a.grid[0]) is not list:
            temp_row = []
            dot_product = 0
            for m_1_x in range(len(matrix_a.grid)):
                dot_product += matrix_a.grid[m_1_x] * matrix_b.grid[m_1_x][0]
            temp_row.append(dot_product)
            temp_matrix.append(temp_row)
        elif type(matrix_b[0]) is not list:
            for m_1_y in range(len(matrix_a.grid)):
                temp_row = []
                for m_2_x in range(len(matrix_b)):
                    dot_product = 0
                    for m_1_x in range(len(matrix_a.grid[m_1_y])):
                        dot_product += int(matrix_a.grid[m_1_y][m_1_x]) * int(matrix_b[m_2_x])
                    temp_row.append(dot_product)
                temp_matrix.append(temp_row)
        return Matrix(temp_matrix)

    def scalar_matrix_multiply(input1, input2):
        temp_matrix = []
        if Matrix.type(input1) == MatrixType.scalar:
            for row in input2.grid:
                temp_row = []
                for item in row:
                    temp_row.append(item * input1)
                temp_matrix.append(temp_row)
        else:
            for row in input1.grid:
                temp_row = []
                for item in row:
                    temp_row.append(item * input2)
                temp_matrix.append(temp_row)
        return Matrix(temp_matrix)

    def matrix_matrix_multiply(matrix_a, matrix_b):
        temp_matrix = []
        for m_1_y in range(len(matrix_a.grid)):
            temp_row = []
            for m_2_x in range(len(matrix_b.grid[0])):
                dot_product = 0
                for m_1_x in range(len(matrix_a.grid[m_1_y])):
                    dot_product += float(matrix_a.grid[m_1_y][m_1_x]) * float(matrix_b.grid[m_1_x][m_2_x])
                temp_row.append(dot_product)
            temp_matrix.append(temp_row)
        return Matrix(temp_matrix)

    # multiples the two input matrices and returns the product
    def multiply(matrix_a, matrix_b):
        if ((Matrix.type(matrix_a) == MatrixType.scalar and Matrix.type(matrix_b) == MatrixType.matrix)
                or (Matrix.type(matrix_b) == MatrixType.scalar and Matrix.type(matrix_a) == MatrixType.matrix)):
            return Matrix.scalar_matrix_multiply(matrix_a, matrix_b)
        elif ((Matrix.type(matrix_a) == MatrixType.horizontal_vector
               or Matrix.type(matrix_a) == MatrixType.vertical_vector)
                and Matrix.type(matrix_b) == MatrixType.matrix):
            return Matrix.vector_matrix_multiply(matrix_a, matrix_b)
        elif Matrix.type(matrix_a) == MatrixType.matrix and Matrix.type(matrix_b) == MatrixType.matrix:
            return Matrix.matrix_matrix_multiply(matrix_a, matrix_b)

    # adds the two input matrices and returns the sum
    def add(matrix_a, matrix_b):
        temp_matrix = []
        if len(matrix_a.grid) == len(matrix_b) and len(matrix_a.grid[0]) == len(matrix_b[0]):
            for row in range(len(matrix_a.grid)):
                temp_row = []
                for column in range(len(matrix_a.grid[0])):
                    temp_row.append(matrix_a.grid[row][column] + matrix_b[row][column])
                temp_matrix.append(temp_row)
        return Matrix(temp_matrix)

    # subtracts the second input matrix from the first and returns the difference
    def subtract(matrix_a, matrix_b):
        temp_matrix = []
        if len(matrix_a.grid) == len(matrix_b) and len(matrix_a.grid[0]) == len(matrix_b[0]):
            for row in range(len(matrix_a.grid)):
                temp_row = []
                for column in range(len(matrix_a.grid[0])):
                    temp_row.append(matrix_a.grid[row][column] - matrix_b[row][column])
                temp_matrix.append(temp_row)
        return Matrix(temp_matrix)

    def divide(matrix_a, matrix_b):
        pass


'''
# prompts user for grid specifications
row = int(input('How many rows would you like the grid to have: '))
print('Please enter the contents of each row with each item separated by a ","')

# creates an empty grid that will be used to store user input
user_grid = Matrix([])

# takes 4 lines of user input and splits the lines by ',' to form a grid, lists inside of lists
for _ in range(row):
    temp_row = input("Enter row {0}: ".format(_ + 1)).split(',')

    #checks to make sure row lengths are the same to get a consistent grid
    while _ != 0 and len(temp_row) != len(user_grid.grid[_ - 1]):
        print('The number of items in each row of the grid must remain consistent. Please reenter this row.')
        temp_row = input("Enter row {0}: ".format(_ + 1)).split(',')
    user_grid.grid.append(temp_row)

# prints (a): the original grid
print('\nThe Following is part (a), the original grid:')
user_grid.print()

# prints (b): the reflected grid
print('\nThe Following is (b), the original grid reflected over the diagonal running from top left to bottom right:')
user_grid.reflect().print()

# prints (c): Both versions of the grid with horizontal repeats removed
print('\nThe Following is part (c):')

print('The original grid with repeats removed:')
user_grid.remove_horizontal_repeats().print()

print('The reflected grid with repeats removed:')
user_grid.reflect().remove_horizontal_repeats().print()

# prints the product of the original grid and its reflection
print('\nThe following is the product of the original grid and the reflection of the original grid')
Matrix.multiply(user_grid, user_grid.reflect()).print()'''

matrix1 = Matrix([[1,5,5,6],[10,10,11,6],[5,2,5,7],[4,6,3,4]])
matrix2 = Matrix([[1,2],[15,6]])
print(matrix1.determinant())

