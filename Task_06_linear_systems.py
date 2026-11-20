import numpy as np

# x = number of Type A servers; y = number of Type B servers
# Type A: 4 CPU units, 8 GB RAM; Type B: 2 CPU units, 12 GB RAM
A = np.array([[4.0, 2.0], [8.0, 12.0]])
b = np.array([20.0, 72.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution
print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

# Changed input: increased CPU total from 20 to 24 units
b_changed = np.array([24.0, 72.0])
print("Allocation for changed resource totals:",
      np.linalg.solve(A, b_changed))
