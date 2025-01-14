import numpy as np

def operacje(operation, matrix_a, matrix_b=None):
    if operation == "add":
        if matrix_a.shape != matrix_b.shape:
            raise ValueError("Matrices must have the same dimensions for addition.")
        return matrix_a + matrix_b
    elif operation == "multiply":
        if matrix_a.shape[1] != matrix_b.shape[0]:
            raise ValueError("Number of columns in A must match rows in B for multiplication.")
        return np.dot(matrix_a, matrix_b)
    elif operation == "transpose":
        return matrix_a.T
    else:
        raise ValueError("Unsupported operation.")

matrix_a = np.array([[10, 4], [8, 3]])
matrix_b = np.array([[15, 26], [32, 19]])
print(operacje("add", matrix_a, matrix_b))
print(operacje("multiply", matrix_a, matrix_b))
print(operacje("transpose", matrix_a))
