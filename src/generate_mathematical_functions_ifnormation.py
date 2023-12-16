import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from functions import *

# Function definitions (including the ones provided earlier)

functions = [
    ackley,
    sphere,
    rosenbrock,
    griewank,
    michalewicz,
    rastrigin,
    schwefel,
    bohachevsky,
    zakharov,
    styblinski_tang,
    himmelblau,
    easom,
    schaffer_n2,
    schaffer_n4,
    six_hump_camel,
    schwefel_problem_2_21,
    rotated_hyper_ellipsoid,
    generalized_penalized_1,
    generalized_penalized_2,
    modified_schwefel_problem_1_2,
    pinter_function_8,
    alpine_function,
    quartic_function,
    sum_of_different_powers,
    salomon_function
]

# Open a single text file for writing
with open("optimization_functions_combined.txt", "w") as file:
    for i, func in enumerate(functions, start=1):
        info = generate_mathematical_function_info(func) 
        # Generate sample points
        x = np.linspace(-100, 100, 400)
        y = np.linspace(-100, 100, 400)
        X, Y = np.meshgrid(x, y)
        Z = func(np.array([X, Y]))

        # Create 2D plot
        fig = plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.contourf(X, Y, Z, levels=50, cmap="viridis")
        plt.title(f"{info['name']} - 2D Plot")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.colorbar()

        # Create 3D plot
        ax = fig.add_subplot(1, 2, 2, projection='3d')
        surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis, edgecolors='k', linewidth=0.5)
        ax.set_title(f"{info['name']} - 3D Plot")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        plt.tight_layout()

        # Save the combined chart
        plt.savefig(f"function_{i}_combined.png")
        plt.close()

        # Write information to the text file
        file.write(f"Function {i}\n")
        file.write(f"Name: {info['name']}\n")
        file.write("Mathematical Formula:\n")
        file.write(f"{info['formula']}\n\n")
        file.write(f"Combined Plot: function_{i}_combined.png\n\n")

# Print success message
print("Plots and information saved to optimization_functions_combined.txt.")
