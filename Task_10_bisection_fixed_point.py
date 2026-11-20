import numpy as np
from scipy.optimize import root_scalar

# Find break-even production level where revenue equals cost:
# f(q) = 50q - (200 + 30q) = 0
def profit_equation(q):
    return 50 * q - (200 + 30 * q)

bisect_result = root_scalar(
    profit_equation, bracket=[0, 20], method="bisect", xtol=1e-10
)
print(f"Break-even quantity (bisection): {bisect_result.root:.6f} units")
print("Profit at estimated root:", profit_equation(bisect_result.root))

# Fixed-point iteration for q = 200/20 = 10
def fixed_point(g, x0, tolerance=1e-10, max_iter=100):
    x = x0
    for i in range(1, max_iter + 1):
        new_x = g(x)
        if abs(new_x - x) < tolerance:
            return new_x, i
        x = new_x
    return x, max_iter

fixed_root, count = fixed_point(lambda q: 10.0, 1.0)
print(f"Fixed-point result: {fixed_root:.6f} after {count} iterations")

# Changed input: fixed costs increase from 200 to 300
changed_root = root_scalar(
    lambda q: 50*q - (300 + 30*q), bracket=[0, 30], method="bisect"
).root
print(f"Break-even quantity with fixed cost 300: {changed_root:.2f}")
