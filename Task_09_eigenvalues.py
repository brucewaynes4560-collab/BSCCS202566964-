import numpy as np

# Link-transition-like matrix for a small network
A = np.array([
    [0.0, 0.5, 0.5],
    [1.0, 0.0, 0.0],
    [0.5, 0.5, 0.0]
])

eigenvalues, eigenvectors = np.linalg.eig(A)
dominant_index = np.argmax(np.abs(eigenvalues))
dominant_value = eigenvalues[dominant_index]
dominant_vector = np.real(eigenvectors[:, dominant_index])
ranking = np.abs(dominant_vector)
ranking = ranking / ranking.sum()

print("Eigenvalues:", eigenvalues)
print("Dominant eigenvalue:", dominant_value)
print("Normalized dominant eigenvector:", ranking)
print("Largest score belongs to page:", np.argmax(ranking) + 1)

# Changed matrix: change the link weight from page 1 to page 2
A_changed = A.copy()
A_changed[1, 0] = 0.5
values_changed = np.linalg.eigvals(A_changed)
print("Eigenvalues after matrix change:", values_changed)
