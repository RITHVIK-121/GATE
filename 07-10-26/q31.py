#code by rithvik ,07-10-26
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# 1. Solve for 'a' and 'b' analytically using SymPy
x, a, b = sp.symbols("x a b")

# Define the two parts of the piecewise function
f1 = a * x + b
f2 = x**3 + x**2 + 1

# Differentiate both parts
df1 = sp.diff(f1, x)
df2 = sp.diff(f2, x)

# Differentiability condition at x = 1: derivatives must match
# a = 3(1)^2 + 2(1)
eq1 = sp.Eq(df1.subs(x, 1), df2.subs(x, 1))

# Solve for 'a' first
sol_a = sp.solve(eq1, a)[0]

# Continuity condition at x = 1: function values must match
# a(1) + b = 1^3 + 1^2 + 1
eq2 = sp.Eq(f1.subs({x: 1, a: sol_a}), f2.subs(x, 1))

# Solve for 'b'
sol_b = sp.solve(eq2, b)[0]

print(f"Calculated Values:")
print(f"a = {float(sol_a):.1f}")
print(f"b = {float(sol_b):.1f}\n")


# 2. Plotting the function
# Convert SymPy expressions to numpy functions for numerical evaluation
a_val, b_val = float(sol_a), float(sol_b)


def piecewise_f(x_arr):
    # Vectorized piecewise evaluation
    return np.where(x_arr < 1, a_val * x_arr + b_val, x_arr**3 + x_arr**2 + 1)


# Generate x values spanning across x = 1
x_vals = np.linspace(-1, 2, 400)
y_vals = piecewise_f(x_vals)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the linear part (x < 1)
x_left = x_vals[x_vals <= 1]
plt.plot(
    x_left,
    a_val * x_left + b_val,
    "r--",
    linewidth=2,
    label=f"Linear part: ${a_val:.0f}x {b_val:+.0f}$ ($x < 1$)",
)

# Plot the cubic part (x >= 1)
x_right = x_vals[x_vals >= 1]
plt.plot(
    x_right,
    x_right**3 + x_right**2 + 1,
    "b-",
    linewidth=2,
    label="Cubic part: $x^3 + x^2 + 1$ ($x \geq 1$)",
)

# Mark the transition point at x = 1
plt.plot(1, piecewise_f(np.array([1]))[0], "go", markersize=8, label="Point (1, 3)")

# Formatting the graph
plt.axhline(0, color="black", linewidth=0.5, linestyle=":")
plt.axvline(0, color="black", linewidth=0.5, linestyle=":")
plt.title("Graph of the Smooth Piecewise Function $f(x)$", fontsize=14)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$f(x)$", fontsize=12)
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.6)

# Show the plot
plt.show()

