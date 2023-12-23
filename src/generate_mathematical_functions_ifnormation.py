import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from functions.functions import *

# Create a folder for charts if it doesn't exist
if not os.path.exists("charts"):
    os.makedirs("charts")

def PlotFunction2D(fun, siz=10):
    x = np.linspace(-siz, siz, 500)
    points = np.column_stack((x, np.zeros_like(x)))
    y = np.apply_along_axis(fun, 1, points)

   # Calculate function values
    y = np.apply_along_axis(fun, 1, points)

    # Set np.inf values to a very large value
    y[np.isinf(y)] = np.nanmax(y)

    plt.plot(x, y)
    title = str(fun.__name__) + ' - 2D'
    plt.title(str(title))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig('./charts/'+str(title)+'.png')
    plt.close()

def PlotFunction3D(fun, siz=10):
    x = y = np.linspace(-siz, siz, 500)
    X, Y = np.meshgrid(x, y)
    points = np.column_stack((X.flatten(), Y.flatten()))
    Z = np.apply_along_axis(fun, 1, points)

    Z = Z.reshape(X.shape)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    title = str(fun.__name__) + ' - 3D'
    ax.set_title(str(title))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.savefig('./charts/'+str(title)+'.png')
    plt.close()

# Open a single text file for writing
for i, func in enumerate(functions_list, start=1):
    PlotFunction2D(func)
    PlotFunction3D(func)

# Print success message
print("Plots and information saved to optimization_functions_combined.txt.")
