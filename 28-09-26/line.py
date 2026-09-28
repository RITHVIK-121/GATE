import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines as mlines
from matplotlib.patches import Patch

# 1. Define the grid for the two planes
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

# Equation 1: x1 + x2 + x3 = 0 -> x3 = -x1 - x2
Z1 = -X - Y

# Equation 2: x1 + 2*x3 = 0 -> x3 = -0.5*x1
Z2 = -0.5 * X

# 2. Define the parametric line of intersection
# From solving the system: x1 = -2t, x2 = t, x3 = t
t = np.linspace(-2, 2, 100)
x_line = -2 * t
y_line = t
z_line = t

# 3. Set up the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surfaces representing the planes
surf1 = ax.plot_surface(X, Y, Z1, alpha=0.4, color='cyan')
surf2 = ax.plot_surface(X, Y, Z2, alpha=0.4, color='orange')

# Plot the intersection line
ax.plot(x_line, y_line, z_line, color='red', linewidth=3)

# Plot the origin point (0,0,0)
ax.scatter(0, 0, 0, color='black', s=50)

# 4. Labeling and Aesthetics
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$x_3$')
ax.set_title('Intersection of Two Planes Forming a Line')

# Create a custom legend
legend_elements = [
    Patch(facecolor='cyan', alpha=0.4, label='$x_1 + x_2 + x_3 = 0$ (Plane 1)'),
    Patch(facecolor='orange', alpha=0.4, label='$x_1 + 2x_3 = 0$ (Plane 2)'),
    mlines.Line2D([], [], color='red', linewidth=3, label='Intersection Line'),
    mlines.Line2D([], [], color='black', marker='o', linestyle='None', markersize=8, label='Origin (0,0,0)')
]
ax.legend(handles=legend_elements, loc='upper left')

# Adjust the camera viewing angle for better visualization
ax.view_init(elev=20, azim=45)

# 5. Save the figure to a file
# Change 'planes_intersection.png' to your preferred filename or path
plt.savefig('planes_intersection.png', dpi=300, bbox_inches='tight')
print("Figure successfully saved as 'planes_intersection.png'")
os.system("termux-open planes_intersection.png")
# Close the plot to free up system memory
plt.close()

