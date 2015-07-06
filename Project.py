from enum import Enum
import copy

def clear_screen():
    print('\n' * 30)  # prints new line 30 times to clear the screen

class MatrixType(Enum):  # creates an enumeration class to differentiate between matrix types
    scalar = 1
    horizontal_vector = 2
    vertical_vector = 3
    matrix = 4

class Matrix:
    def __init__(self, grid):
        self.grid = grid  # creates a grid for each Matrix object when initialized

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
                    temp_sub_grid.append(item)  # adds the original item to the new list only if there isn't already a copy in the same row
            temp_grid.append(temp_sub_grid)  # adds the temp row to the temp grid
        return Matrix(temp_grid)

    # formats and prints the input grid
    def print(self):
        for row in self.grid:
            temp_str = '['
            for x in range(len(row)):
                temp_str += str(round(row[x], 2)) + (',' if x != (len(row) - 1) else '')  # adds the current item of the matrix to the string and then a ','
            temp_str += ']'
            print(temp_str)

    # determines the matrix type of the input
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

    # calculates the determinant of the matrix
    def determinant(self):
        determinant = 0

        if len(self.grid) == 2 and len(self.grid[0]) == 2:  # checks to see if the matrix is 2x2
            return self.grid[0][0] * self.grid[1][1] - self.grid[0][1] * self.grid[1][0]  # returns the determinant of a 2x2 matrix using the mathematical formula
        else:
            for x in range(len(self.grid[0])):
                temp_grid = copy.deepcopy(self.grid)

                # removes the row and column of the current item (as described by the formula to calculate determinant of any matrix 3x3 or larger)
                for row in temp_grid:
                    row.pop(x)
                temp_grid.pop(0)

                if x % 2 == 0:
                    determinant += self.grid[0][x] * Matrix(temp_grid).determinant()
                else:
                    determinant -= self.grid[0][x] * Matrix(temp_grid).determinant()

        return determinant

    # multiplies scalar by matrix
    def scalar_matrix_multiply(input1, input2):
            temp_matrix = []

            for row in input2.grid:
                temp_row = []
                for item in row:
                    temp_row.append(item * input1)  # multiplies each item by the scalar
                temp_matrix.append(temp_row)

            return Matrix(temp_matrix)

    # multiples the two input matrices and returns the product
    def multiply(matrix_a, matrix_b):
        temp_matrix = []

        for m_1_y in range(len(matrix_a.grid)):
            temp_row = []
            for m_2_x in range(len(matrix_b.grid[0])):
                dot_product = 0
                for m_1_x in range(len(matrix_a.grid[m_1_y])):
                    dot_product += float(matrix_a.grid[m_1_y][m_1_x]) * float(matrix_b.grid[m_1_x][m_2_x])  # adds the product of the current items in the two matrices to the dot product
                temp_row.append(dot_product) # appends the dot product to temp_row
            temp_matrix.append(temp_row)  # appends the temp_row to temp_matrix

        return Matrix(temp_matrix)

    # determines the inverse of a matrix
    def inverse(self):
        if len(self.grid) == 2 and len(self.grid[0]) == 2:
            temp_matrix = [[self.grid[1][1], -1* self.grid[0][1]],[-1 * self.grid[1][0],self.grid[0][0]]]
            return Matrix.scalar_matrix_multiply(1/self.determinant(),Matrix(temp_matrix))

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
        if len(matrix_a.grid) == len(matrix_b.grid) and len(matrix_a.grid[0]) == len(matrix_b.grid[0]): #checks to make sure the matrices are the same size
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

    # divides the first matrix by the second
    def divide(matrix_a, matrix_b):
        return Matrix.multiply(matrix_a,matrix_b.inverse()) # multiplies the first matrix by the inverse of the second (equivalent to dividing)

    # function for entering a valid matrix
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
            temp_row = input("Enter row {}: ".format(_ + 1)).split(',')

            while True:  # checks to make sure all the values in the row are valid numbers
                try:
                    # checks to make sure row lengths are the same to get a consistent grid
                    while _ != 0 and len(temp_row) != len(user_grid.grid[_ - 1]):
                        print('The number of items in each row of the grid must remain consistent. Please reenter this row.')
                        temp_row = input("Enter row {}: ".format(_ + 1)).split(',')

                    for x in range(len(temp_row)):
                        temp_row[x] = float(temp_row[x])
                    break
                except ValueError:
                    print("You didn't enter a valid row. Please try again.")
                    temp_row = input("Enter row {}: ".format(_ + 1)).split(',')  # asks user to reenter row with valid numbers

            user_grid.grid.append(temp_row)

        clear_screen()
        return user_grid

    # function for entering a valid matrix with a set height in order to perform calculations properly
    def enter_constrained_height_matrix(text, height):

        clear_screen()
        # tells the user the requied specs for the matrix
        print("In order to perform the calculation, there must be {} rows in the matrix.".format(height))

        print('Please enter the contents of each row with each item separated by a ","')

        # creates an empty grid that will be used to store user input
        user_grid = Matrix([])

        # takes 4 lines of user input and splits the lines by ',' to form a grid, lists inside of lists
        for _ in range(height):
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

    # function for entering a valid matrix with a set height and width in order to perform calculations properly
    def enter_constrained_height_width_matrix(text, height, width):

        clear_screen()
        # tells the user the required specs for the matrix
        print("In order to perform the calculation, there must be {} rows and {} columns in the matrix.".format(height, width))

        print('Please enter the contents of each row with each item separated by a ","')

        # creates an empty grid that will be used to store user input
        user_grid = Matrix([])

        # takes 4 lines of user input and splits the lines by ',' to form a grid, lists inside of lists
        for _ in range(height):
            temp_row = input("Enter row {0}: ".format(_ + 1)).split(',')

            while True:  # checks to make sure all the values in the row are valid numbers
                try:
                    # checks to make sure row lengths are the same to get a consistent grid
                    while len(temp_row) != width:
                        print('The number of items in each row must be {}. Please reenter this row.'.format(width))
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

    def enter_matrix_with_min_width(text, min_width):

        clear_screen()

        # prompts user for grid specifications
        height = input('\nHow many rows would you like {} to have: '.format(text))

        while True: #checks to make sure user entered a valid number of rows
            try:
                height = int(height)
                while not height > 0:
                    print("You didn't enter a valid number. Please try again.")
                    height = int(input('How many rows would you like {} to have: '.format(text))) # user reenters value for valid number
                else:
                    break
            except ValueError:
                print("You didn't enter a valid number. Please try again.")
                height = input('How many rows would you like {} to have: '.format(text)) # user reenters value for valid number

        print('Please enter the contents of each row with each item separated by a ","')
        # tells the user the required specs for the matrix
        print("In order to perform the calculation, there must be at least {} items in each row.\n".format(min_width))

        # creates an empty grid that will be used to store user input
        user_grid = Matrix([])

        # takes 4 lines of user input and splits the lines by ',' to form a grid, lists inside of lists
        for _ in range(height):
            temp_row = input("Enter row {0}: ".format(_ + 1)).split(',')

            while True:  # checks to make sure all the values in the row are valid numbers
                try:
                    # checks to make sure row lengths are the same to get a consistent grid
                    while not len(temp_row) >= min_width:
                        print('The number of items in each row must be at least {}. Please reenter this row.'.format(min_width))
                        temp_row = input("Enter row {}: ".format(_ + 1)).split(',')

                    for x in range(len(temp_row)):
                        temp_row[x] = float(temp_row[x])
                    break
                except ValueError:
                    print("You didn't enter a valid row. Please try again.")
                    temp_row = input("Enter row {}: ".format(_ + 1)).split(',')  # asks user to reenter row with valid numbers

            user_grid.grid.append(temp_row)

        clear_screen()
        return user_grid

    def enter_square_matrix(text, spec = None): # spec is set to none to make it optional
        if spec == None:
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

            print("This must be a square matrix so there must also be {} numbers in each row.\n".format(row))
        else:
            row = spec
            print("This must be a square matrix so there must be {} rows and {} items in each row.\n".format(spec,spec))

        print('Please enter the contents of each row with each item separated by a ","')

        # creates an empty grid that will be used to store user input
        user_grid = Matrix([])

        # takes 4 lines of user input and splits the lines by ',' to form a grid, lists inside of lists
        for _ in range(row):
            temp_row = input("Enter row {}: ".format(_ + 1)).split(',')

            while True:  # checks to make sure all the values in the row are valid numbers
                try:
                    # checks to make sure row lengths are the same to get a consistent grid
                    while len(temp_row) != row:
                        print('The number of items in each row must be {}. Please reenter this row.'.format(row))
                        temp_row = input("Enter row {}: ".format(_ + 1)).split(',')

                    for x in range(len(temp_row)):
                        temp_row[x] = float(temp_row[x])
                    break
                except ValueError:
                    print("You didn't enter a valid row. Please try again.")
                    temp_row = input("Enter row {}: ".format(_ + 1)).split(',')  # asks user to reenter row with valid numbers

            user_grid.grid.append(temp_row)

        clear_screen()
        return user_grid

# asks the user if they want to continue
def ask_to_continue():
    print('\n' * 3)
    choice = input('Would you like to perform another calculation?: ').lower()
    clear_screen()
    return choice in ['y','ye','yes'] # returns whether the user wants to continue or not

running = True
while(running):
    print('Welcome to the matrix calculator. Which of the following functions would you like to perform')
    print('\n1.Calculate Determinant\n2.Calculate Inverse\n3.Determine Reflection of Grid\n4.Determine if Matrix is Symmetric\n5.Add Matrices\n6.Subtract Matrices\n7.Multiply Matrices\n8.Divide Matrices')
    choice = input('\nChoice: ')

    if(choice == '1'):
        matrix1 = Matrix.enter_grid('the matrix')
        if len(matrix1.grid) < 2 or len(matrix1.grid[0]) < 2:
            print("The determinant can't be calculated because the matrix must be at least 2x2.")
        else:
            print('The determinant of the matrix is: ' + str(matrix1.determinant()))

    elif(choice == '2'):
        clear_screen()
        print('The matrix must be square and be larger than 2x2 to calculate the determinant.')
        size = input('What is the number of rows: ')
        while True:
            try:
                size = int(size)
                while size < 2:
                    print('The matrix must be at least 2x2. Please try again')
                    size = int(input('What is the number of rows: '))
                break
            except ValueError:
                print("You didn't enter a valid number please try again.")
                size = input('What is the number of rows: ')

        matrix1 = Matrix.enter_square_matrix('the matrix', size)
        if(matrix1.determinant() == 0):
            print("The determinant of the matrix is 0, so an inverse can't be calculated")
        else:
            print('The inverse of the matrix is:\n')
            matrix1.inverse().print()

    elif(choice == '3'):
        matrix1 = Matrix.enter_grid('the matrix')
        print('The reflection of the grid is:\n')
        matrix1.reflect().print()

    elif(choice == '4'):
        matrix1 = Matrix.enter_grid('the matrix')
        print("The matrix is " + ("not symmetric","symmetric")[matrix1.is_symmetric()])

    elif(choice == '5'):
        matrix1 = Matrix.enter_grid('the first matrix')
        matrix2 = Matrix.enter_constrained_height_width_matrix('the second matrix',len(matrix1.grid),len(matrix1.grid[0]))
        print('The sum of the two matrices is:\n')
        Matrix.add(matrix1,matrix2).print()

    elif(choice == '6'):
        matrix1 = Matrix.enter_grid('the first matrix')
        matrix2 = Matrix.enter_constrained_height_width_matrix('the second matrix',len(matrix1.grid),len(matrix1.grid[0]))
        print('The difference of the two matrices is:\n')
        Matrix.subtract(matrix1,matrix2).print()

    elif(choice == '7'):
        clear_screen()
        input_text = input('Will you be multiplying by a scalar?')
        clear_screen()

        if(input_text in ['y','ye','yes']):
            scalar = input('Please enter a scalar: ')

            while True:
                try:
                    scalar = float(scalar)
                    break
                except ValueError:
                    print("You didn't enter a valid scalar. Please try again.")
                    scalar = input('Please enter a scalar: ')

            matrix2 = Matrix.enter_grid('the matrix')
            print('The product of the scalar and matrix is:\n')
            Matrix.scalar_matrix_multiply(scalar,matrix2).print()
        else:
            matrix1 = Matrix.enter_grid('the first matrix')
            matrix2 = Matrix.enter_constrained_height_matrix('the second matrix', len(matrix1.grid[0]))
            print('The product of the two matrices is:\n')
            Matrix.multiply(matrix1,matrix2).print()

    elif(choice == '8'):
        matrix1 = Matrix.enter_matrix_with_min_width('the first matrix', 2)
        matrix2 = Matrix.enter_square_matrix('the second matrix',len(matrix1.grid[0]))
        print('The quotient of the two matrices is:\n')

        if matrix2.determinant() == 0:
            print('A quotient cannot be calculated because the determinant of the second matrix is equal to 0')
        else:
            Matrix.divide(matrix1,matrix2).print()

    running = ask_to_continue()