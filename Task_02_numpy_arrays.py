import numpy as np

# 24 hourly sensor readings in degrees Celsius
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)
temperatures_f = 1.8 * temperatures_c + 32

print("Daily mean temperature: {:.2f} °C".format(mean_temp))
print("Minimum temperature: {:.2f} °C".format(min_temp))
print("Maximum temperature: {:.2f} °C".format(max_temp))
print("First six Fahrenheit readings:", np.round(temperatures_f[:6], 2))

# Changed-input experiment: add 2°C to every reading
warmer_readings = temperatures_c + 2
print("Mean after adding 2°C: {:.2f} °C".format(np.mean(warmer_readings)))
