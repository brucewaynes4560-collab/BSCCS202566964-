import numpy as np
from scipy.optimize import root

# Circle: x^2 + y^2 = 4; parabola: y = x^2 - 1
def equations(z):
    x, y = z
    return [x**2 + y**2 - 4, y - (x**2 - 1)]

for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection (x, y):", solution.x)
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()

# Changed equation: circle radius increases from 2 to 3
def larger_circle(z):
    x, y = z
    return [x**2 + y**2 - 9, y - (x**2 - 1)]
changed = root(larger_circle, [1.0, 2.0])
print("Intersection for radius-3 circle:", changed.x)
