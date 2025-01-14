from functools import reduce
import numpy as np

def polacz(matrices, operation):
    return reduce(operation, matrices)

matrices = [np.array([[4, 7], [3, 2]]), np.array([[2, 6], [4, 5]])]
sum_matrices = polacz(matrices, lambda x, y: x + y)
print(sum_matrices)
