import numpy as np
from scipy.integrate import simpson

# Smart-meter readings every two hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

energy_trapezoid = np.trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.3f} kWh")
print(f"Difference: {abs(energy_simpson-energy_trapezoid):.3f} kWh")

# Changed input: power readings increase by 10%
higher_power = 1.10 * power_kw
print("Energy after 10% increase (Simpson):",
      f"{simpson(higher_power, x=time_hours):.3f} kWh")
