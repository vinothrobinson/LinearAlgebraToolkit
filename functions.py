from tkinter import ttk


class Matrix:
    def __init__(self, num_of_rows: int, num_of_cols: int) -> None:
        self.matrix = [[] * num_of_rows]
        self.isSquare = num_of_rows == num_of_cols

    def scalar_mult(self, scalar: float):
        pass

    def matrix_addition(self, other):
        pass

    def matrix_mult(self):
        pass

    def det(self) -> float:
        if not self.isSquare:
            return

    def get_eigenvalues(self) -> float:
        if not self.isSquare:
            return


class Window:
    pass
