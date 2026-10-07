import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import os

# 1. Analytical Solver using SymPy
k = sp.symbols('k')
A = sp.Matrix([[1, k], [k, 1]])
B = sp.Matrix([1, -1])

# Find critical values where determinant is zero
det_A = A.det()
critical_k = sp.solve(det_A, k)

print("--- System Analysis ---")
print(f"Determinant of A: {det_A}")
print(f"Critical values of k (det(A) = 0): {critical_k}\n")

for kv in critical_k:
    A_sub = A.subs(k, kv)
    B_sub = B.subs(k, kv)
    Aug = A_sub.row_join(B_sub)
    
    rank_A = A_sub.rank()
    rank_Aug = Aug.rank()
    
    if rank_A == rank_Aug:
        print(f"For k = {kv}: INFINITE SOLUTIONS (Lines coincide)")
    else:
        print(f"For k = {kv}: NO SOLUTION (Lines are parallel)")

print(f"For any other value of k (k ≠ {list(critical_k)}): UNIQUE SOLUTION (Lines intersect)\n")

# 2. Visualization Function
def plot_system(k_val, ax, title):
    x_vals = np.linspace(-3, 3, 400)
    
    # Equation 1: x + ky = 1  -> y = (1 - x)/k
    # Equation 2: kx + y = -1 -> y = -1 - kx
    if k_val == 0:
        ax.axvline(x=1, color='blue', label='x = 1')
        ax.axhline(y=-1, color='crimson', label='y = -1')
    else:
        y1 = (1 - x_vals) / k_val
        y2 = -1 - k_val * x_vals
        ax.plot(x_vals, y1, color='blue', label=f'x + ({k_val})y = 1')
        ax.plot(x_vals, y2, color='crimson', linestyle='--', label=f'({k_val})x + y = -1')
        
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

# Generate and display the interactive side-by-side subplots grid
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
plot_system(1, axes[0], "No Solution (k = 1)\n[Parallel Lines]")
plot_system(-1, axes[1], "Infinite Solutions (k = -1)\n[Coinciding Lines]")
plot_system(2, axes[2], "Unique Solution (k = 2)\n[Intersecting Lines]")

plt.tight_layout()

# --- NEW: SAVE THE COMBINED TIMELINE IMAGE ---
# This saves the full side-by-side 3-panel layout as a single image file.
plt.savefig('linear_system_cases.png', dpi=300, bbox_inches='tight')
print("Saved combined plot as 'linear_system_cases.png'\n")
os.system("termux-open linear_system_cases.png")


# --- OPTIONAL: SAVE INDIVIDUAL PLOTS ---
# If you prefer having separate image files for each condition, use this method:
cases = {
    "no_solution_k1.png": (1, "No Solution (k = 1)"),
    "infinite_solutions_k_minus1.png": (-1, "Infinite Solutions (k = -1)"),
    "unique_solution_k2.png": (2, "Unique Solution (k = 2)")
}

for filename, (k_val, title) in cases.items():
    fig_single, ax_single = plt.subplots(figsize=(6, 6))
    plot_system(k_val, ax_single, title)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig_single)
    print(f"Saved individual plot as '{filename}'")

