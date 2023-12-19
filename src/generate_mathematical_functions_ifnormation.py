import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from functions.functions import *



# Create a folder for charts if it doesn't exist
if not os.path.exists("charts"):
    os.makedirs("charts")

# Open a single text file for writing
for i, func in enumerate(functions_list, start=1):
    info = generate_mathematical_function_info(func) 
        # Generate sample points
    # Create a meshgrid for plotting
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[func(np.array([xi, yi])) for xi, yi in zip(x_row, y_row)] for x_row, y_row in zip(X, Y)])

    # Plot the 2D chart
    plt.subplot(1, 2, 1)
    plt.plot(x, Z[50, :], color='blue')  # Adjusted y index to plot, you can change it as needed
    plt.title('2D Plot')

    # Plot the 3D chart
    fig = plt.figure()
    ax_3d = fig.add_subplot(111, projection='3d')
    ax_3d.plot_surface(X, Y, Z, cmap='viridis')
    ax_3d.set_title('3D Plot')

    # Adjust layout and save the figure to the 'charts' folder
    output_folder = 'charts'
    os.makedirs(output_folder, exist_ok=True)  # Create the 'charts' folder if it doesn't exist
    output_path = os.path.join(output_folder, f'{info["name"]}.png')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# Print success message
print("Plots and information saved to optimization_functions_combined.txt.")
