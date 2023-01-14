import tkinter as tk
from tkinter import ttk


class Matrix:
    def __init__(self, num_of_rows: int, num_of_cols: int) -> None:
        self.matrix = [[] * num_of_rows]
        self.isSquare = num_of_rows == num_of_cols
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols


def scalar_mult(matrix: Matrix, scalar: float) -> Matrix:
    result = matrix
    for i in range(matrix.num_of_rows):
        for j in range(matrix.num_of_cols):
            result.matrix[i][j] *= scalar
    return result


def matrix_addition(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    result = matrix1
    if (matrix1.num_of_cols != matrix2.num_of_cols) or (matrix1.num_of_rows != matrix2.num_of_rows):
        return None
    for i in range(matrix1.num_of_rows):
        for j in range(matrix1.num_of_cols):
            result.matrix[i][j] += matrix2.matrix[i][j]


def matrix_mult(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    if matrix1.num_of_cols != matrix2.num_of_rows:
        return None
    result = Matrix(matrix1.num_of_rows, matrix2.num_of_cols)
    for i in range(matrix1.num_of_rows):  # Initializing all the elements in the matrix to 0
        for j in range(matrix2.num_of_cols):
            result.matrix[i].append(0)
    for i in range(matrix1.num_of_rows):  # Matrix Multiplication computation
        for j in range(matrix1.num_of_cols):
            result.matrix[i][j] += matrix1.matrix[i][j] * matrix2.matrix[j][i]
    return result


def det(matrix: Matrix, sum = 0: int) -> float:
    if not matrix.isSquare:
        return None
    if (matrix.num_of_rows > 2):
        for i in range(matrix.num_of_rows):
            for j in range(matrix.num_of_cols):
                sum += (-1)**(i + j)*det(helperDet(matrix, i, j), sum)
    if (matrix.num_of_rows == 2):
        sum += (matrix.matrix[0][0] * matrix.matrix[1][1]) - (matrix.matrix[0][1] * matrix.matrix[1][0])
    if (matrix.num_of_rows == 1):
        sum += matrix.matrix[0][0]
    return sum

def helperDet(matrix: Matrix, rows: int, cols: int) -> Matrix:
    result = Matrix(matrix.num_of_rows, matrix.num_of_cols)
    indX, indY = 0
    for i in range(result.num_of_rows):
        for j in range(result.num_of_cols):
            if (i != rows) and (j != cols):
                result.matrix[i][j] = matrix.matrix[indX][indY]
                indX += 1
                indY += 1
    return result

def get_eigenvalues(self) -> float:
    if not self.isSquare:
        return


class Window:
    def __init__(self, ):
        root = tk.Tk()
        root.geometry('1000x800')
        main_frame = ttk.Frame(root)
        main_frame['padding'] = (50, 10, 50, 10)
        main_frame.pack()

        scalar_mult_button = ttk.Button(main_frame, text='Scalar Multiplication', command=lambda: 5+5) # ignore the lambda
        scalar_mult_button.pack()
        root.mainloop()


Window()
