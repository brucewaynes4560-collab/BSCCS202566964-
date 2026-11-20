# BIT 2118 – SCIENTIFIC COMPUTING

## Individual GitHub Repository

This repository contains Python implementations for **Tasks 2–20** in the BIT 2118 Scientific Computing group-work brief. It includes mathematical explanations, source code, changed-input experiments, interpretations and alternative related real-world applications.

## Repository contents

- `code/` — one runnable Python file for each task, retaining the task numbers from the brief.
- `documentation/project_report.md` — task-by-task concepts, inputs, parameter changes, output interpretations and alternative applications.
- `results/graphs/` — location where graph-producing programs save their figures when run from the repository root.
- `requirements.txt` — required Python libraries.

## Requirements

- Python 3.9 or later
- NumPy
- SciPy
- Matplotlib

## Installation

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\\Scripts\\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run a task

Run commands from the repository root. For example:

```bash
python code/Task_02_numpy_arrays.py
python code/Task_13_interpolation.py
python code/Task_20_monte_carlo.py
```

Graph-producing programs display a graph and save a PNG in `results/graphs/`.

## Task list

| Task | Topic | Program |
|---:|---|---|
| 2 | NumPy arrays and numerical computation | `Task_02_numpy_arrays.py` |
| 3 | Mathematical functions and vectorization | `Task_03_vectorization.py` |
| 4 | Floating-point arithmetic and numerical errors | `Task_04_numerical_errors.py` |
| 5 | Matrix algebra and matrix operations | `Task_05_matrix_algebra.py` |
| 6 | Systems of linear equations | `Task_06_linear_systems.py` |
| 7 | Gaussian elimination and LU decomposition | `Task_07_gaussian_lu.py` |
| 8 | Iterative methods for linear systems | `Task_08_iterative_linear.py` |
| 9 | Eigenvalues and eigenvectors | `Task_09_eigenvalues.py` |
| 10 | Bisection and fixed-point methods | `Task_10_bisection_fixed_point.py` |
| 11 | Newton-Raphson and secant methods | `Task_11_newton_secant.py` |
| 12 | Polynomial and nonlinear equation solving | `Task_12_nonlinear_equations.py` |
| 13 | Interpolation | `Task_13_interpolation.py` |
| 14 | Curve fitting and approximation | `Task_14_curve_fitting.py` |
| 15 | Numerical differentiation | `Task_15_numerical_differentiation.py` |
| 16 | Numerical integration | `Task_16_numerical_integration.py` |
| 17 | ODEs – Euler method | `Task_17_euler_ode.py` |
| 18 | Numerical solution of ODEs using SciPy | `Task_18_scipy_ode.py` |
| 19 | Numerical optimization | `Task_19_optimization.py` |
| 20 | Random numbers and Monte Carlo methods | `Task_20_monte_carlo.py` |

## Assignment requirements covered

Each task has:
1. The mathematical concept.
2. Input values and mathematical operations.
3. At least one changed input or parameter and an explanation.
4. Output interpretation and graph interpretation where applicable.
5. A modified, related real-world application with assumptions and data described in the report.

## Important notes

- All sample datasets are illustrative and are clearly defined in each program.
- Numerical results can vary slightly by Python, NumPy and SciPy version.
- Monte Carlo results are reproducible because a random seed is set.
- This is an individual repository. Create and submit your own GitHub repository link through VLMS, as required by the course brief.
- Review the assumptions and run each program before submission. Add your own name, admission number and any lecturer-specific requirements if requested.

## Author

**Student name:** [Enter your full name]  
**Admission number:** [Enter your admission number]  
**Course:** BIT 2118 – Scientific Computing
