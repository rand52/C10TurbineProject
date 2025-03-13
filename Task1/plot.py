import matplotlib.pyplot as plt
from numpy.typing import NDArray
import numpy as np
def plot_data(data:NDArray, dataname:str):
    """
    Plots a 2D scatter plot from a numpy array with 2 columns.

    Parameters:
        data (np.ndarray): An (n, 2) numpy array where:
            - Column 0 is the x-axis values.
            - Column 1 is the y-axis values.
    """
    if data.shape[1] != 2:
        raise ValueError("Input array must have exactly 2 columns")

    x = data[:, 0]  # First column as x values
    y = data[:, 1]  # Second column as y values

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker='o', linestyle='-')  # Line plot with markers
    plt.xlabel("Uref[m/s^2]")
    plt.ylabel("Power produced[W]")
    plt.title(f"Power curve for {dataname}")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    data = np.array([[1, 2], [2, 4], [3, 1], [4, 3], [5, 5]])
    plot_data(data)
    
