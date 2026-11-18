import numpy as np
from networkx import DiGraph # the exact datatype for the map
from collections.abc import Sequence
from dataclasses import dataclass

# maybe better to use own class
# for considering distance and some custom interface

class Matrix:
    def __init__(self, array: Sequence | np.ndarray, shape: tuple[int, int]) -> None:
        n, m = shape

        if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
            raise ValueError("Matrix shape dimensions must be non-negative integers")

        if len(array) != n * m:
            raise ValueError("The array length must equal rows * columns")

        self._M = np.array(array, dtype = float)
        self._row, self._col = n, m

    def row_mul(self, scalar: int | float, r: int):
        for j in range(self._col):
            self._M[r * self._col + j] *= scalar

    def col_mul(self, scalar: int | float, c: int):
        for i in range(self._row):
            self._M[self._col * i + c] *= scalar

    def get_shape(self) -> tuple[int, int]:
        return self._row, self._col

    def get_row(self, r: int):
        start = r * self._col
        end = start + self._col
        return self._M[start:end]

    def get_col(self, c: int):
        return [self._M[row * self._col + c] for row in range(self._row)]

    def __getitem__(self, key):

        """
        Handles indexing and slicing only of these forms M[i, j], M[i, :], or M[:, j]
        """

        if not isinstance(key, tuple) or len(key) != 2:
            raise TypeError("Index must be a pair like M[i, j], M[i, :], or M[:, j]")

        row, col = key

        # single item M[i, j]
        if isinstance(row, int) and isinstance(col, int):
            return self._M[row * self._col + col]

        # entire row M[i, :]
        elif isinstance(row, int) and isinstance(col, slice):
            start = row * self._col
            end = start + self._col
            return self._M[start:end]

        # entire column M[:, j]
        elif isinstance(row, slice) and isinstance(col, int):
            return [self._M[r * self._col + col] for r in range(self._row)]

        raise TypeError("Unsupported index form; use M[i, j], M[i, :], or M[:, j]")

    def __imul__(self, scalar: int | float) -> "Matrix":
        self._M *= scalar
        return self

    def update_matrix(self, new_arr: Sequence | np.ndarray, new_shape: tuple[int, int]) -> None:
        n, m = new_shape

        if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
            raise ValueError("Matrix shape dimensions must be non-negative integers")

        if len(new_arr) != n * m:
            raise ValueError("The array length must equal rows * columns")

        self._M = np.array(new_arr, dtype=float)
        self._row, self._col = n, m

    def __repr__(self) -> str:
        return ""

@dataclass
class RoadData:

    # the class for representing a path from A to B
    # using distance and amount of bougth tickets from A to B

    distance: int | float
    tickets: int

def convert_graph_to_matrix(G: DiGraph) -> Matrix:
    arr = np.array([])

    pass

    V = G.number_of_nodes()
    return Matrix(arr, (V, V))

def get_dist_matrix(G: DiGraph) -> Matrix:
    # maybe not needed at all
    arr = np.array([])

    pass

    V = G.number_of_nodes()
    return Matrix(arr, (V, V))
