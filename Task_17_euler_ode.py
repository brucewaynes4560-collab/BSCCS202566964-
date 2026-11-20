import numpy as np
import matplotlib.pyplot as plt

# Newton's law of cooling: dT/dt = -k(T - T_ambient)
T_ambient = 25.0
T_initial = 90.0
k = 0.12
h = 1.0
end_time = 30.0

def cooling_rate(T):
    return -k * (T - T_ambient)

time = np.arange(0, end_time + h, h)
temperature = np.zeros_like(time)
temperature[0] = T_initial

for i in range(len(time) - 1):
    temperature[i + 1] = temperature[i] + h * cooling_rate(temperature[i])

exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)
print(f"Euler temperature after 30 min: {temperature[-1]:.2f} °C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} °C")
print(f"Final absolute error: {abs(temperature[-1]-exact[-1]):.4f} °C")

plt.plot(time, temperature, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Cooling of a hot object")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/graphs/task_17_euler_cooling.png", dpi=150)
plt.show()

# Changed step size: smaller h gives a more accurate approximation
h_small = 0.25
t_small = np.arange(0, end_time + h_small, h_small)
T_small = np.zeros_like(t_small)
T_small[0] = T_initial
for i in range(len(t_small) - 1):
    T_small[i+1] = T_small[i] + h_small * cooling_rate(T_small[i])
print("Final error with 0.25-minute step:",
      abs(T_small[-1] - exact[-1]))
