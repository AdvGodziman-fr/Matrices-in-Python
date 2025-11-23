import numpy as np

def create_matrix():

    global rows
    global cols

    print
    try:
        rows = int(input('Enter the number of rows: '))
    except ValueError:
        print('The value of rows should be a integer and not any other data type')
        cols = int(input('Enter the number of columns: '))

    try:
        cols = int(input('Enter the number of columns: '))
    except:
        print('The value of rows should be a integer and not any other data type')
        

    matrix = []
    print('Enter the elements for the matrix: ')
    print()
        
    for i in range(rows):
        while True:
            row_eles = input(f"Enter {cols} elements for row {i + 1} separating them using commas: ")
            raw_rows = row_eles.split(',')

            if len(raw_rows) != cols:
                print(f'Input of columns = {cols}, but no. of elements is greater pf le')
                continue

            float_row = [3 for j in raw_rows]
            np.array(matrix.append(float_row))
            break

    return matrix
 
class Matrix_Operations(object):
    def __init__(self):
        print('INSTRUCTIONS FOR MATRIX OPERATIONS')
        print('\n1. For Addition and Subtraction of Matrix, the rows and columns of the matrices should be same.')
        print('2. For Multiplication (Matrix) of Mat1(n * m) and Mat2(p * q), n = q and m = p')
        print()
        print('*****************************************************************************')
        
        global mat1
        global mat2

        print('\nCreate the first Matrix:')
        print()
        mat1 = create_matrix()

        print('\nCreate the second Matrix:')
        print()
        mat2 = create_matrix()

    def addition(self):
        print('\nMatrix Addition:')
        print('------------------------------------')
        try:
            add = np.add(mat1, mat2)
            print(f'The addition of Mat1 {mat1} and Mat 2 {mat2} = {add}')
        except:
            print('Error: There is a mismatch in the number of rows and columns in the matrices')
            mat_add1 = create_matrix()
            mat_add2 = create_matrix()
            np.add(mat_add1, mat_add2)
            print(f'The addition of Mat1 {mat_add1} and Mat 2 {mat_add2} = {add}')
            print('******************************************')
    
    def subtraction(self):
        print('\nMatrix Subtraction:')
        print('------------------------------------')
        try:
            sub = np.subtract(mat1, mat2)
            print(f'The subtraction of Mat1 {mat1} and Mat 2 {mat2} = {sub}')
        except:
            print('Error: There is a mismatch in the number of rows and columns in the matrices')
            mat_sub1 = create_matrix()
            mat_sub2 = create_matrix()
            sub = np.subtract(mat_sub1, mat_sub2)
            print(f'The subtraction of Mat1 {mat_sub1} and Mat 2 {mat_sub2} = {sub}')
            print('\n******************************************')

    def scalar_matrix_multiplications(self):
        print('\nScalar-Matrix Multiplications:')
        print('------------------------------------')
        try:
            scalar = int(input("Enter a scalar value: "))
        except:
            print('Enter a proper Integer Value to Multipy with the Matrix')
            scalar = int(input("Enter a scalar value: "))
        scalar_mul1 = scalar * mat1
        scalar_mul2 = scalar * mat2
        
        print(f'The Muliplication of {scalar} * {mat1} = {scalar_mul1}')
        print(f'The Muliplication of {scalar} * {mat2} = {scalar_mul2}')
        print('\n******************************************')
    
    def matrix_multiplication(self):
        print('\nMatrix Multiplication:')
        print('------------------------------------')
        shape1 = list(np.shape(mat1))
        shape2 = list(np.shape(mat2))
        print(shape1, shape2)
        try:
            print(np.matmul(mat1, mat2))
        except:
            print('Format Not Followed')
            print('Enter a Proper Format i.e. for matricies m*n and p*q, m = q and n = p')
            print('Shape of Matrix 1 = ', shape1)
            print('Shape of Matrix 2 = ', shape2)
            matmul1 = create_matrix()
            matmul2 = create_matrix()
            print(f'The Multiplication of {mat1} * {mat2} = {np.matmul(matmul1, matmul2)}')
            print('\n******************************************')

    def inverse_matrix(self):
        print('\nMatrix Inversion:')
        try:
            mat1_ = np.linalg.inv(mat1)
            mat2_ = np.linalg.inv(mat2)
        except:
            print('Matrix is singular and cannot be inverted. Please enter new matrices.')
            mat1 = create_matrix()
            mat2 = create_matrix()
            mat1_ = np.linalg.inv(mat1)
            mat2_ = np.linalg.inv(mat2)


        print(f'Inverse of Matrix 1 = {mat1_}')
        print(f'Inverse of Matrix 2 = {mat2_}')
        print('\n******************************************')

    def transpose_elements(self):
        print('\nMatrix Transposition:')
        print('--------------------------------------')
        trans_mat1_ = np.transpose(mat1)
        trans_mat2_ = np.transpose(mat2)
        print(f'Transposef Matrix 1 = {trans_mat1_}')
        print(f'Transposed Matrix 2 = {trans_mat2_}')

        print('\n******************************************')

    def determinants(self):
        print('\n Finding Determinants')
        print('--------------------------------------')
        try:
            det1 = np.linalg.det(mat1)
            det2 = np.linalg.det(mat2)
        except:
            print('The Matrix should be a square Matrix')
            mat1 = create_matrix()
            mat2 = create_matrix()
            det1 = np.linalg.det(mat1)
            det2 = np.linalg.det(mat2)


        print(f'Determinants of Matrix 1 = {det1}')
        print(f'Determinants of Matrix 2 = {det2}')
        print('\n******************************************')


workspace = Matrix_Operations()

print('Matrix Addition:')
workspace.addition()
print('Matrix Subtraction:')
workspace.subtraction()
print('Scalar-Matrix Multiplications:')
workspace.scalar_matrix_multiplications()
print('Matrix Multiplication:')
workspace.matrix_multiplication()
print('Matrix Transposition:')
workspace.transpose_elements()
print('Finding Determinants:')
workspace.determinants()
print('Matrix Inversion:')
workspace.inverse_matrix()

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')