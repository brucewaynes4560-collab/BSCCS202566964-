import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([
    [3.0, 1.0, -1.0],
    [2.0, 4.0, 1.0],
    [-1.0, 2.0, 5.0]
])
b = np.array([4.0, 1.0, 1.0])

# Gaussian elimination using NumPy's linear solver
gaussian_solution = np.linalg.solve(A, b)

# LU factorization: reuse the factorization for the right-hand side
lu, piv = lu_factor(A)
lu_solution = lu_solve((lu, piv), b)

print("Gaussian elimination solution:", gaussian_solution)
print("LU decomposition solution:", lu_solution)
print("A @ solution:", A @ lu_solution)
print("Residual norm:", np.linalg.norm(A @ lu_solution - b))

# Changed input vector; reuse the same LU factors
b2 = np.array([5.0, 2.0, 3.0])
print("Solution for second measurement vector:", lu_solve((lu, piv), b2))
