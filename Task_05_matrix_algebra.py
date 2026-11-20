import numpy as np

# 2D points and a rotation matrix
points = np.array([[1, 1], [2, 1], [1, 3], [-1, 2]], dtype=float)
angle_degrees = 45
angle = np.deg2rad(angle_degrees)
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

transformed = points @ rotation.T
print("Original points:\n", points)
print("Rotation matrix:\n", rotation)
print("Rotated points:\n", np.round(transformed, 3))
print("Determinant:", np.linalg.det(rotation))

# Changed parameter: rotate by 90 degrees
angle_90 = np.deg2rad(90)
rotation_90 = np.array([
    [np.cos(angle_90), -np.sin(angle_90)],
    [np.sin(angle_90),  np.cos(angle_90)]
])
print("Points after 90-degree rotation:\n", np.round(points @ rotation_90.T, 3))
