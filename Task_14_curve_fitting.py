import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

def model(x, a, b, c):
    return a*x**2 + b*x + c

parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters
predicted = model(users, *parameters)
rmse = np.sqrt(np.mean((response_ms - predicted)**2))

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {model(400, *parameters):.2f} ms")

x_plot = np.linspace(users.min(), 400, 300)
plt.scatter(users, response_ms, label="Measurements")
plt.plot(x_plot, model(x_plot, *parameters), label="Fitted curve")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/graphs/task_14_curve_fitting.png", dpi=150)
plt.show()

# Changed-input experiment: predict for 450 concurrent users
print(f"Prediction at 450 users: {model(450, *parameters):.2f} ms")
