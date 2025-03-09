from typing import *

Number = Union[int, float]

class Matrix:
    def __init__(self, *args: Iterable[Number]):
        if isinstance(args[0][0], Iterable):
            self._rows = args[0]
        else:
            self._rows = list(args)
            
        for row in self._rows:
            for val in row:
                if not isinstance(val, Number):  raise TypeError(f"Tried to input a '{type(val).__name__}' into a Matrix")
            
    def __matmul__(self, matrix):
        if not issubclass(type(matrix), Matrix):  raise TypeError(f"Tried to multiply a matrix with type '{type(matrix).__name__}'")
        
        rowsA, colsA = self.getSize()
        rowsB, colsB = matrix.getSize()
        
        if colsA != rowsB:  raise ValueError(f"Matrices cannot be multiplied. Tried to multiply {rowsA}x{colsA} matrix by {rowsB}x{colsB} matrix")
        
        C = Matrix([[0 for _ in range(colsB)] for _ in range(rowsA)])
        
        # Perform matrix multiplication
        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    C[j, i] += self[k, i] * matrix[j, k]
        
        return Matrix(C)
    
    def __getitem__(self, index: int | tuple[int]):
        if isinstance(index, int):
            return self._rows[index]
        elif isinstance(index, tuple):
            if len(index) != 2 or not (isinstance(index[0], int) and isinstance(index[1], int)):
                raise ValueError(f"Tried to index a matrix with the value {index}")
            else:
                return self._rows[index[1]][index[0]]
            
    def __setitem__(self, index: tuple[int], value: Number):
        if not isinstance(index, tuple):  raise TypeError("Index is not a coordinate. Example input: 1, 2")
        if not isinstance(value, Number):  raise TypeError("Input value is not a number")
        
        if len(index) != 2 or not (isinstance(index[0], int) and isinstance(index[1], int)):
            raise ValueError(f"Tried to index a matrix with the value {index}")
        else:
            self._rows[index[1]][index[0]] = value
    
    
    def __str__(self) -> str:
        return str([list(map(float, row)) for row in self._rows])[1:-1].replace("], [", "]\n[")
    
    
    def dot(self, matrix):  return self @ matrix
    
    def getSize(self) -> tuple:
        rows = len(self._rows)
        cols = len(self._rows[0])
        
        return rows, cols
