# BIT 2118 – Scientific Computing: Task Documentation

This report accompanies the Python programs in `code/`. Each task records the concept, input data, mathematical operation, changed input, output interpretation and a related application. Numerical values are illustrative assumptions for learning, not measurements from a real organization.

## Task 2: NumPy arrays and numerical computation

### 1. Mathematical concept
A NumPy array stores numerical measurements and supports element-wise operations. The program calculates mean, minimum, maximum and converts Celsius to Fahrenheit.

### 2. Input values and operations
24 hourly temperatures (°C); mean/min/max; F = 1.8C + 32.

### 3. Changed input / parameter
Adding 2°C to every measurement raises the mean, minimum and maximum by exactly 2°C.

### 4. Output interpretation
The output summarizes the day's temperature range. The converted array expresses the same readings in Fahrenheit.

### 5. Modified related real-world application
Use the same method to summarize hourly water-pH or humidity sensor readings.

**Program:** `code/Task_02_numpy_arrays.py`

## Task 3: Mathematical functions and vectorization

### 1. Mathematical concept
Vectorization applies an operation to a whole array without a Python-level loop.

### 2. Input values and operations
One million simulated network latency values in milliseconds; divide by 1000 and square.

### 3. Changed input / parameter
The experiment also evaluates only 100,000 readings to show how workload size changes processing time.

### 4. Output interpretation
The first five values are squared latency values in seconds squared. The timing comparison illustrates the runtime difference on the computer used.

### 5. Modified related real-world application
Apply vectorization to convert and analyze large batches of electricity meter readings.

**Program:** `code/Task_03_vectorization.py`

## Task 4: Floating-point arithmetic and numerical errors

### 1. Mathematical concept
Finite binary storage means some decimal fractions are approximations. Absolute and relative errors measure approximation quality.

### 2. Input values and operations
0.1, 0.2, 0.3 and approximations of √2; np.isclose; stable algebraic expressions.

### 3. Changed input / parameter
A more precise approximation of √2 reduces absolute error.

### 4. Output interpretation
Exact equality can fail for mathematically equal decimal expressions; tolerance comparison is safer for numerical work.

### 5. Modified related real-world application
Use tolerance-based comparisons in financial reconciliation or engineering sensor calibration; use decimal arithmetic where exact decimal representation is required.

**Program:** `code/Task_04_numerical_errors.py`

## Task 5: Matrix algebra and matrix operations

### 1. Mathematical concept
A matrix represents a linear transformation. Multiplying point coordinates by a rotation matrix rotates them in 2D.

### 2. Input values and operations
Four 2D points and a 45-degree rotation matrix; matrix multiplication and determinant.

### 3. Changed input / parameter
Changing the angle from 45° to 90° changes the transformed coordinates.

### 4. Output interpretation
The output gives each point's new coordinates. A rotation matrix has determinant approximately 1, indicating area preservation.

### 5. Modified related real-world application
Use transformation matrices to rotate map coordinates or reposition objects in a computer graphics application.

**Program:** `code/Task_05_matrix_algebra.py`

## Task 6: Solution of systems of linear equations

### 1. Mathematical concept
A system Ax=b is solved for unknown vector x using matrix methods.

### 2. Input values and operations
CPU and RAM resource totals; A=[[4,2],[8,12]], b=[20,72].

### 3. Changed input / parameter
CPU total changes from 20 to 24 while RAM stays 72; the allocation changes accordingly.

### 4. Output interpretation
The solution estimates the numbers of each server type consistent with both resource equations. The residual should be near zero.

### 5. Modified related real-world application
Estimate quantities of two ingredients from two measured nutrient totals in a production process.

**Program:** `code/Task_06_linear_systems.py`

## Task 7: Gaussian elimination and LU decomposition

### 1. Mathematical concept
Gaussian elimination reduces a linear system; LU factorization stores reusable lower and upper triangular factors.

### 2. Input values and operations
A 3×3 coefficient matrix and two right-hand-side measurement vectors.

### 3. Changed input / parameter
A second b vector is solved using the same LU factors.

### 4. Output interpretation
Both approaches should give matching solutions, and the residual verifies the system is satisfied.

### 5. Modified related real-world application
Reuse LU factors to solve repeated electrical circuit models with a fixed network and changing source measurements.

**Program:** `code/Task_07_gaussian_lu.py`

## Task 8: Iterative methods for linear systems

### 1. Mathematical concept
Jacobi iteration repeatedly updates each unknown using the latest previous iteration values.

### 2. Input values and operations
Diagonally dominant 3×3 matrix, right-hand-side vector and tolerance.

### 3. Changed input / parameter
Tightening tolerance from 1e-10 to 1e-12 generally requires additional iterations.

### 4. Output interpretation
The result approximates the solution; the residual norm measures how closely it satisfies Ax=b.

### 5. Modified related real-world application
Use iterative solvers for large sparse heat-transfer or power-network models.

**Program:** `code/Task_08_iterative_linear.py`

## Task 9: Eigenvalues and eigenvectors

### 1. Mathematical concept
An eigenvector changes only by a scale factor under matrix multiplication; its eigenvalue is that scale factor.

### 2. Input values and operations
A small matrix representing weighted connections among three pages.

### 3. Changed input / parameter
A link weight is changed and the eigenvalues are recalculated.

### 4. Output interpretation
The dominant eigenvector is normalized into relative page scores. This illustrates a simplified network-centrality idea, not a production PageRank implementation.

### 5. Modified related real-world application
Use eigenvector centrality to rank influential nodes in a communication or transport network.

**Program:** `code/Task_09_eigenvalues.py`

## Task 10: Root finding: bisection and fixed-point methods

### 1. Mathematical concept
Root finding locates x for which f(x)=0. Bisection narrows an interval with opposite signs; fixed-point iteration uses x=g(x).

### 2. Input values and operations
Revenue 50q, fixed cost 200 and variable cost 30q; bracket [0,20].

### 3. Changed input / parameter
Fixed cost increases from 200 to 300, moving the break-even quantity upward.

### 4. Output interpretation
The root is the production quantity at which profit is zero. Bisection is robust when the bracket contains a sign change.

### 5. Modified related real-world application
Find a water-pump operating threshold where supply and demand curves intersect.

**Program:** `code/Task_10_bisection_fixed_point.py`

## Task 11: Root finding: Newton-Raphson and secant methods

### 1. Mathematical concept
Newton's method and the secant method iteratively estimate a root of a nonlinear function.

### 2. Input values and operations
Cash flows [-1000,300,400,500,400]; NPV as a function of discount rate.

### 3. Changed input / parameter
The final cash flow is increased from 400 to 600; the estimated IRR changes.

### 4. Output interpretation
IRR is the discount rate at which NPV is approximately zero. Newton and secant estimates should be close when convergent.

### 5. Modified related real-world application
Estimate the yield or break-even discount rate for a small investment project.

**Program:** `code/Task_11_newton_secant.py`

## Task 12: Polynomial and nonlinear equation solving

### 1. Mathematical concept
A nonlinear solver finds values that make a set of residual equations close to zero.

### 2. Input values and operations
Circle x²+y²=4 and parabola y=x²−1; two initial guesses.

### 3. Changed input / parameter
Circle radius changes from 2 to 3.

### 4. Output interpretation
The returned coordinates are intersection points; small residuals and a success flag indicate convergence.

### 5. Modified related real-world application
Find where a road alignment curve intersects a circular boundary or plot boundary.

**Program:** `code/Task_12_nonlinear_equations.py`

## Task 13: Interpolation

### 1. Mathematical concept
Interpolation estimates values between measured data points. Linear interpolation joins points with straight segments; cubic splines use smooth cubic pieces.

### 2. Input values and operations
Hourly temperatures from 08:00 to 14:00; estimate at 10:30 and every ten minutes.

### 3. Changed input / parameter
The requested estimate time changes to 11:30.

### 4. Output interpretation
The plotted curves pass through the measured points and estimate intermediate temperatures. Interpolation should not be treated as reliable extrapolation beyond the data range.

### 5. Modified related real-world application
Estimate missing water-level or humidity sensor readings between scheduled measurements.

**Program:** `code/Task_13_interpolation.py`

## Task 14: Curve fitting and approximation

### 1. Mathematical concept
Least-squares curve fitting chooses parameters to minimize squared differences between observed and predicted values.

### 2. Input values and operations
Concurrent server users and measured response times; quadratic model.

### 3. Changed input / parameter
Prediction is evaluated at 450 rather than 400 users.

### 4. Output interpretation
The fitted curve summarizes the observed trend; RMSE measures typical fitting error in milliseconds. Predictions outside observed data are less certain.

### 5. Modified related real-world application
Fit a demand curve to historical customer counts and service times.

**Program:** `code/Task_14_curve_fitting.py`

## Task 15: Numerical differentiation

### 1. Mathematical concept
Finite differences approximate derivatives from discrete measurements. Central differences use values on both sides of a point.

### 2. Input values and operations
GPS time and position samples; forward, central and backward differences.

### 3. Changed input / parameter
Small measurement noise is added to the positions.

### 4. Output interpretation
The estimated derivative is speed in metres per second. Differentiation can amplify measurement noise.

### 5. Modified related real-world application
Estimate the rate of change of river level from readings taken at regular time intervals.

**Program:** `code/Task_15_numerical_differentiation.py`

## Task 16: Numerical integration

### 1. Mathematical concept
Numerical integration estimates accumulated area under a curve. The program compares trapezoidal and Simpson's rules.

### 2. Input values and operations
Power readings in kW every two hours; integration over time gives kWh.

### 3. Changed input / parameter
Every power reading is increased by 10%, so estimated energy also increases by 10%.

### 4. Output interpretation
The estimates represent energy consumed over the measured interval. Differences arise because the methods approximate the curve differently.

### 5. Modified related real-world application
Estimate total water flow from periodic flow-rate measurements.

**Program:** `code/Task_16_numerical_integration.py`

## Task 17: Ordinary differential equations: Euler method

### 1. Mathematical concept
Euler's method advances an approximate solution using y_next = y + h f(t,y).

### 2. Input values and operations
Ambient temperature 25°C, initial temperature 90°C, cooling constant 0.12 per minute, step 1 minute.

### 3. Changed input / parameter
The step size is reduced to 0.25 minutes.

### 4. Output interpretation
The graph shows the hot object cooling toward ambient temperature. A smaller step usually reduces discretization error.

### 5. Modified related real-world application
Model the cooling of stored food or a machine component over time.

**Program:** `code/Task_17_euler_ode.py`

## Task 18: Numerical solution of ODEs using SciPy

### 1. Mathematical concept
solve_ivp numerically solves differential equations with adaptive numerical methods.

### 2. Input values and operations
RC circuit: supply 5 V, resistance 1000 Ω, capacitance 0.001 F and initial voltage 0 V.

### 3. Changed input / parameter
Resistance is doubled; the circuit charges more slowly because the time constant RC increases.

### 4. Output interpretation
The graph compares numerical and exact charging curves. The capacitor voltage approaches the supply voltage.

### 5. Modified related real-world application
Model charging or discharging in a different electronic circuit by changing resistance, capacitance or supply voltage.

**Program:** `code/Task_18_scipy_ode.py`

## Task 19: Numerical optimization

### 1. Mathematical concept
Optimization minimizes an objective function subject to constraints and bounds.

### 2. Input values and operations
Two server types with costs 12 and 18 and capacities 100 and 170; minimum capacity 1000.

### 3. Changed input / parameter
Required capacity is increased to 1200, increasing the minimum cost.

### 4. Output interpretation
The optimizer finds a least-cost continuous allocation; the integer search compares whole-server combinations because physical servers cannot be fractional.

### 5. Modified related real-world application
Minimize transport or production costs while meeting a required delivery or output target.

**Program:** `code/Task_19_optimization.py`

## Task 20: Random numbers and Monte Carlo methods

### 1. Mathematical concept
Monte Carlo simulation estimates probabilities through repeated random sampling.

### 2. Input values and operations
100,000 normally distributed demand scenarios; mean 850, standard deviation 120 and capacity 1000.

### 3. Changed input / parameter
Mean demand is increased to 900 while capacity and standard deviation remain unchanged.

### 4. Output interpretation
The fraction of simulations exceeding capacity estimates overload probability. The running estimate tends to stabilize as simulations increase.

### 5. Modified related real-world application
Estimate stockout risk, equipment failure probability or queue overload under uncertain demand.

**Program:** `code/Task_20_monte_carlo.py`
