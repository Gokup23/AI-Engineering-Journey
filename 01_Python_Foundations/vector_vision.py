import numpy as np
import matplotlib.pyplot as plt

def visualize_vectors(v1, v2):
    # Setup the 3D Plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Origin point
    origin = [0, 0, 0]

    # Plot the two basis vectors from your textbook
    ax.quiver(*origin, *v1, color='r', label='Vector V', linewidth=3)
    ax.quiver(*origin, *v2, color='b', label='Vector W', linewidth=3)

    # Calculate the Plane (Linear Combinations)
    # We create a grid of scalars 'c' and 'd'
    range_val = np.linspace(-1, 1, 10)
    c, d = np.meshgrid(range_val, range_val)
    
    # The Plane Equation: P = c*v + d*w
    # This is exactly what Strang's Lecture 1 is about!
    plane_x = c * v1[0] + d * v2[0]
    plane_y = c * v1[1] + d * v2[1]
    plane_z = c * v1[2] + d * v2[2]

    # Draw the Plane
    ax.plot_surface(plane_x, plane_y, plane_z, alpha=0.3, color='cyan')

    # Formatting the "Lab"
    ax.set_xlim([-2, 2]); ax.set_ylim([-2, 2]); ax.set_zlim([-2, 2])
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    plt.title("Visualizing the Span of v and w")
    plt.legend()
    plt.show()

# --- TRY STRANG'S PROBLEM 1.1A ---
# v = (1, 1, 0) and w = (0, 1, 1)
v = np.array([1, 1, 0])
w = np.array([0, 1, 1])

visualize_vectors(v, w)