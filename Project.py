from enum import Enum
import copy
import math

def clear_screen():
    print('\n' * 30)

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

    # determines whether the matrix is symmetric or not
    def is_symmetric(self):
        return self.grid == Matrix(self.grid).reflect().grid # checks if original grid is equal to the transposed grid

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
                temp_str += str(round(row[x], 2)) + (',' if x != (len(row) - 1) else '')
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

    def inverse(self):
        if len(self.grid) == 2 and len(self.grid[0]) == 2:
            temp_matrix = [[self.grid[1][1], -1* self.grid[0][1]],[-1 * self.grid[1][0],self.grid[0][0]]]
            return Matrix.multiply(1/self.determinant(),Matrix(temp_matrix))

        else:
            total_determinant = self.determinant()
            temp_matrix = []
            for row in range(len(self.grid)):
                temp_row = []
                for column in range(len(self.grid)):
                    temp_grid = copy.deepcopy(self.grid)
                    for temp_grid_row in range(len(temp_grid)):
                        temp_grid[temp_grid_row].pop(row)
                    temp_grid.pop(column)
                    temp_row.append(Matrix(temp_grid).determinant()/total_determinant * ((-1) ** ((row + 1 + column + 1))))
                temp_matrix.append(temp_row)
            return Matrix(temp_matrix)

    # adds the two input matrices and returns the sum
    def add(matrix_a, matrix_b):
        temp_matrix = []
        if len(matrix_a.grid) == len(matrix_b.grid) and len(matrix_a.grid[0]) == len(matrix_b.grid[0]):
            for row in range(len(matrix_a.grid)):
                temp_row = []
                for column in range(len(matrix_a.grid[0])):
                    temp_row.append(matrix_a.grid[row][column] + matrix_b.grid[row][column])
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
        return Matrix.multiply(matrix_a,matrix_b.inverse())

    def enter_grid(text):
        clear_screen()
        # prompts user for grid specifications
        row = input('How many rows would you like {} to have: '.format(text))

        while True: #checks to make sure user entered a valid number of rows
            try:
                row = int(row)
                while not row > 0:
                    print("You didn't enter a valid number. Please try again.")
                    row = int(input('How many rows would you like {} to have: '.format(text))) # user reenters value for valid number
                else:
                    break
            except ValueError:
                print("You didn't enter a valid number. Please try again.")
                row = input('How many rows would you like {} to have: '.format(text)) # user reenters value for valid number

        print('Please enter the contents of each row with each item separated by a ","')

        # creates an empty grid that will be used to store user input
        user_grid = Matrix([])

        # takes 4 lines of user input and splits the lines by ',' to form a grid, lists inside of lists
        for _ in range(row):
            temp_row = input("Enter row {0}: ".format(_ + 1)).split(',')

            while True:  # checks to make sure all the values in the row are valid numbers
                try:
                    # checks to make sure row lengths are the same to get a consistent grid
                    while _ != 0 and len(temp_row) != len(user_grid.grid[_ - 1]):
                        print('The number of items in each row of the grid must remain consistent. Please reenter this row.')
                        temp_row = input("Enter row {0}: ".format(_ + 1)).split(',')

                    for x in range(len(temp_row)):
                        temp_row[x] = float(temp_row[x])
                    break
                except ValueError:
                    print("You didn't enter a valid row. Please try again.")
                    temp_row = input("Enter row {0}: ".format(_ + 1)).split(',')  # asks user to reenter row with valid numbers

            user_grid.grid.append(temp_row)

        clear_screen()
        return user_grid

def ask_to_continue():
    print('\n' * 3)
    choice = input('Would you like to perform another calculation?: ').lower()
    clear_screen()
    return choice in ['y','ye','yes']



'''running = True
while(running):
    print('Welcome to the matrix calculator. Which of the following functions would you like to perform')
    print('\n1.Calculate Determinant\n2.Calculate Inverse\n3.Determine Reflection of Grid\n4.Add Matrices\n5.Subtract Matrices\n6.Multiply Matrices\n7.Divide Matrices')
    choice = input('\nChoice: ')

    if(choice == '1'):
        matrix1 = Matrix.enter_grid('the matrix')
        print('The determinant of the matrix is: ' + str(matrix1.determinant()))

    elif(choice == '2'):
        matrix1 = Matrix.enter_grid('the matrix')
        if(matrix1.determinant() == 0):
            print('The determinant of the matrix is 0, so an inverse cannnot be calculated')
        else:
            print('The inverse of the matrix is:\n')
            matrix1.inverse().print()

    elif(choice == '3'):
        matrix1 = Matrix.enter_grid('the matrix')
        print('The reflection of the grid is:\n')
        matrix1.reflect().print()

    elif(choice == '4'):
        matrix1 = Matrix.enter_grid('the first matrix')
        matrix2 = Matrix.enter_grid('the second matrix')
        print('The sum of the two matrices is:\n')
        Matrix.add(matrix1,matrix2).print()

    elif(choice == '5'):
        matrix1 = Matrix.enter_grid('the first matrix')
        matrix2 = Matrix.enter_grid('the second matrix')
        print('The difference of the two matrices is:\n')
        Matrix.subtract(matrix1,matrix2).print()

    elif(choice == '6'):
        matrix1 = Matrix.enter_grid('the first matrix')
        matrix2 = Matrix.enter_grid('the second matrix')
        print('The product of the two matrices is:\n')
        Matrix.multiply(matrix1,matrix2).print()

    elif(choice == '7'):
        matrix1 = Matrix.enter_grid('the first matrix')
        matrix2 = Matrix.enter_grid('the second matrix')
        print('The quotient of the two matrices is:\n')
        if matrix2.determinant() == 0:
            print('A quotient cannot be calculated because the determinant of the second matrix is equal to 0')
        else:
            Matrix.divide(matrix1,matrix2).print()

    running = ask_to_continue()'''


'''matrix4_4 = Matrix([[1,2,5,6],[5,2,1,7],[4,5,2,6],[2,6,7,8]])
matrix3_3 = Matrix([[1,5,2],[5,5,3],[2,3,5]])
matrix2_2 = Matrix([[5,4],[2,4]])
matrix3_3.print()
print(matrix3_3.is_symmetric())'''