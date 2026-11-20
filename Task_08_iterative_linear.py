import numpy as np

# Diagonally dominant system suitable for Jacobi iteration
A = np.array([
    [10.0, -1.0, 2.0],
    [-1.0, 11.0, -1.0],
    [2.0, -1.0, 10.0]
])
b = np.array([6.0, 25.0, -11.0])

def jacobi(A, b, tolerance=1e-10, max_iterations=1000):
    x = np.zeros_like(b, dtype=float)
    D = np.diag(A)
    R = A - np.diagflat(D)
    for iteration in range(1, max_iterations + 1):
        new_x = (b - R @ x) / D
        if np.linalg.norm(new_x - x, ord=np.inf) < tolerance:
            return new_x, iteration, True
        x = new_x
    return x, max_iterations, False

solution, iterations, converged = jacobi(A, b)
print("Jacobi solution:", solution)
print("Iterations:", iterations)
print("Converged:", converged)
print("Residual norm:", np.linalg.norm(A @ solution - b))

# Changed parameter: stricter tolerance
strict_solution, strict_iterations, _ = jacobi(A, b, tolerance=1e-12)
print("Iterations with 1e-12 tolerance:", strict_iterations)
