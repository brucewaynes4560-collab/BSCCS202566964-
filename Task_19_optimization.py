import numpy as np
from scipy.optimize import minimize

# x and y represent capacity units of two server types.
# Costs: A=12, B=18; capacities: A=100, B=170.
def cost(z):
    x, y = z
    return 12*x + 18*y

def capacity_constraint(z):
    x, y = z
    return 100*x + 170*y - 1000

constraints = {"type": "ineq", "fun": capacity_constraint}
bounds = [(0, None), (0, None)]

solution = minimize(
    cost, x0=[5, 3], method="SLSQP",
    bounds=bounds, constraints=constraints
)

x, y = solution.x
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100*x + 170*y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")

# Compare feasible integer allocations because actual servers are whole units.
best_integer = None
for a in range(0, 20):
    for b in range(0, 20):
        capacity = 100*a + 170*b
        if capacity >= 1000:
            total_cost = 12*a + 18*b
            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, capacity)
print("Best integer solution (cost, A, B, capacity):", best_integer)

# Changed input: require 1,200 capacity units
def higher_capacity(z):
    return 100*z[0] + 170*z[1] - 1200
changed = minimize(
    cost, x0=[6, 4], method="SLSQP",
    bounds=bounds, constraints={"type": "ineq", "fun": higher_capacity}
)
print("Cost for 1,200 capacity:", changed.fun)
