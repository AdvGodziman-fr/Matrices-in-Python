import numpy as np

def create_matrix():
    rows = int(input('Enter the number of rows: '))
    cols = int(input('Enter the number of columns: '))
    matrix = []
    print('Enter the elements for the matrix')
    print('-------------------------------')
        
    for i in range(rows):
        while True:
            row_eles = input(f'Enter the elements for row {i + 1}: ')
            raw_rows = row_eles.split()

            if len(raw_rows) != cols:
                print(f'Input of columns = {cols}, but no. of elements is greater pf le')
                continue

            float_row = [float(j) for j in raw_rows]
            np.array(matrix.append(float_row))
            break

    return matrix
 
class Matrix_Operations(object):
    def __init__(self):
        print('Instructions for Matrix Operations:')
        print('1. For Addition and Subtraction of Matrix, the rows and columns of the matrices should be same.')
        print('2. For Multiplication (Matrix) of Mat1(n * m) and Mat2(p * q), n = q and m = p')
        
        global mat1
        global mat2

        print('Create Matrix 1')
        mat1 = create_matrix()

        print('Create Matrix 2')
        mat2 = create_matrix()

    def addition(self):
        try:
            add = np.add(mat1, mat2)
            print(add)
        except:
            print('Error: There is a mismatch in the number of rows and columns in the matrices')
            mat_add1 = create_matrix()
            mat_add2 = create_matrix()
            add = mat_add1 + mat_add2
            return add
    
    def subtraction(self):
        try:
            sub = np.subtract(mat1, mat2)
            print(sub)
        except:
            print('Error: There is a mismatch in the number of rows and columns in the matrices')
            mat_sub1 = create_matrix()
            mat_sub2 = create_matrix()
            sub = np.subtract(mat_sub1, mat_sub2)
            print(sub)

    def scalar_matric_multiplications(self):
        scalar = int(input("Enter a scalar value: "))
        scalar_mul1 = scalar * mat1
        scalar_mul2 = scalar * mat2
        
        print(scalar_mul1, scalar_mul2)
    
    def matrix_multiplication(self):
        shape1 = list(np.shape(mat1))
        shape2 = list(np.shape(mat2))
        if shape1 == shape2:
            print(np.matmul(mat1, mat2))
        else:
            matmul1 = create_matrix()
            matmul2 = create_matrix()
            print(np.matmul(matmul1, matmul2))

    def inverse_matrix(self):
        mat1_ = np.linalg.inv(mat1)
        mat2_ = np.linalg.inv(mat2)
        print(mat1_, mat2_)

    def transpose_elements(self):
        trans_mat1_ = np.transpose(mat1)
        trans_mat2_ = np.transpose(mat2)
        print(trans_mat1_, trans_mat2_)

        

workspace = Matrix_Operations()
workspace.addition()
workspace.subtraction()
workspace.scalar_matric_multiplications()
workspace.matrix_multiplication()


workspace.transpose_elements()
workspace.matrix_multiplication()