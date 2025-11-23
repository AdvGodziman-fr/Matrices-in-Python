import numpy as np

def create_matrix():

    while True:
        try:
            rows = int(input('Enter the number of rows: '))
            break
        except ValueError:
            print('The value of rows should be an integer and not any other data type')

    while True:
        try:
            cols = int(input('Enter the number of columns: '))
            break
        except ValueError:
            print('The value of columns should be an integer and not any other data type')

    matrix = []
    print('Enter the elements for the matrix')
    print()
    for i in range(rows):
        while True:
            row_eles = input(f"Enter {cols} elements for row {i + 1} separating them using commas: ")
            raw_rows = row_eles.split(',')
            if len(raw_rows) != cols:
                print(f'Input of columns = {cols}, but number of elements entered is {len(raw_rows)}')
                continue
            try:
                float_row = [float(j) for j in raw_rows]
            except ValueError:
                print('Please enter only numbers.')
                continue
            matrix.append(float_row)
            break
    return np.array(matrix)
 

class Matrix_Operations(object):
    def __init__(self):
        print('INSTRUCTIONS FOR Matrix MATRIX OPERATIONS')
        print('\n1. For Addition and Subtraction of Matrix, the rows and columns of the matrices should be same.')
        print('2. For Multiplication (Matrix) of Mat1(n * m) and Mat2(p * q), m = p')
        print()
        print('*****************************************************************************')

        print('\nCreate the first Matrix:')
        print()
        self.mat1 = create_matrix()

        print('\nCreate the second Matrix:')
        print()
        self.mat2 = create_matrix()

    def addition(self):
        print('\nMatrix Addition:')
        print('------------------------------------')
        try:
            add = np.add(self.mat1, self.mat2)
            print(f'The addition of Mat1 {self.mat1} and Mat 2 {self.mat2} = {add}')
        except Exception:
            print('Error: There is a mismatch in the number of rows and columns in the matrices')
            mat_add1 = create_matrix()
            mat_add2 = create_matrix()
            add = np.add(mat_add1, mat_add2)
            print(f'The addition of Mat1 {mat_add1} and Mat 2 {mat_add2} = {add}')
        print('******************************************')
    
    def subtraction(self):
        print('\nMatrix Subtraction:')
        print('------------------------------------')
        try:
            sub = np.subtract(self.mat1, self.mat2)
            print(f'The subtraction of Mat1 {self.mat1} and Mat 2 {self.mat2} = {sub}')
        except Exception:
            print('Error: There is a mismatch in the number of rows and columns in the matrices')
            mat_sub1 = create_matrix()
            mat_sub2 = create_matrix()
            sub = np.subtract(mat_sub1, mat_sub2)
            print(f'The subtraction of Mat1 {mat_sub1} and Mat 2 {mat_sub2} = {sub}')
        print('\n******************************************')

    def scalar_matrix_multiplications(self):
        print('\nScalar-Matrix Multiplications:')
        print('------------------------------------')
        while True:
            try:
                scalar = float(input("Enter a scalar value: "))
                break
            except ValueError:
                print('Enter a proper numeric value to multiply with the Matrix')
        scalar_mul1 = scalar * self.mat1
        scalar_mul2 = scalar * self.mat2
        print(f'The Multiplication of {scalar} * {self.mat1} = {scalar_mul1}')
        print(f'The Multiplication of {scalar} * {self.mat2} = {scalar_mul2}')
        print('\n******************************************')
    
    def matrix_multiplication(self):
        print('\nMatrix Multiplication:')
        print('------------------------------------')
        shape1 = list(np.shape(self.mat1))
        shape2 = list(np.shape(self.mat2))
        try:
            result = np.matmul(self.mat1, self.mat2)
            print(f'The Multiplication of {self.mat1} * {self.mat2} = {result}')
        except Exception:
            print('Format Not Followed')
            print('Enter a Proper Format i.e. for matrices m*n and p*q, m = p')
            matmul1 = create_matrix()
            matmul2 = create_matrix()
            print(f'The Multiplication of {matmul1} * {matmul2} = {np.matmul(matmul1, matmul2)}')
        print('\n******************************************')

    def inverse_matrix(self):
        print('\nMatrix Inversion:')
        try:
            mat1_ = np.linalg.inv(self.mat1)
            mat2_ = np.linalg.inv(self.mat2)
        except Exception:
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
        trans_mat1_ = np.transpose(self.mat1)
        trans_mat2_ = np.transpose(self.mat2)
        print(f'Transposed Matrix 1 = {trans_mat1_}')
        print(f'Transposed Matrix 2 = {trans_mat2_}')
        print('\n******************************************')


    def determinants(self):
        print('\n Finding Determinants')
        print('--------------------------------------')
        try:
            det1 = np.linalg.det(self.mat1)
            det2 = np.linalg.det(self.mat2)
        except Exception:
            print('The Matrix should be a square Matrix')
            mat1 = create_matrix()
            mat2 = create_matrix()
            det1 = np.linalg.det(mat1)
            det2 = np.linalg.det(mat2)
        print(f'Determinants of Matrix 1 = {det1}')
        print(f'Determinants of Matrix 2 = {det2}')
        print('\n******************************************')


workspace = Matrix_Operations()
workspace.addition()
workspace.subtraction()
workspace.scalar_matrix_multiplications()
workspace.matrix_multiplication()
workspace.transpose_elements()
workspace.determinants()
workspace.inverse_matrix()

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')