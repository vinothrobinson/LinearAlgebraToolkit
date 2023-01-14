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


def matrix_addition(self, other):
    # newMatrix = Matrix(self.nun)
    if (self.num_of_cols != other.num_of_cols) or (self.num_of_rows != other.num_of_rows):
        return
    for i in range(num_of_rows):
        for j in range(num_of_cols):
            self.matrix[i][j] += other.matrix[i][j]


def matrix_mult(self, other):
    if (self.num_of_cols != other.num_of_rows) or (self.num_of_rows != other.num_of_cols):
        return
    newMatrix = Matrix(self.num_of_rows, other.num_of_cols)
    for i in range(self.num_of_rows):  # Initializing all the elements in the matrix to 0
        for j in range(other.num_of_cols):
            newMatrix[i].append(0)
    for i in range(self.num_of_rows):  # Matrix Multiplication computation
        for j in range(self.num_of_cols):
            newMatrix.matrix[i][j] += self.matrix[i][j] * other.matrix[j][i]


def det(self) -> float:
    if not self.isSquare:
        return


def get_eigenvalues(self) -> float:
    if not self.isSquare:
        return


class Window:
    root = tk.Tk()
    root.geometry('1000x800')
    main_frame = ttk.Frame(root)
    main_frame['padding'] = (50, 10, 50, 10)
    main_frame.pack()

    scalar_mult_button = ttk.Button(main_frame, text='Scalar Multiplication')
    scalar_mult_button.pack()
    root.mainloop()


def main():
    window = Window()


main()
