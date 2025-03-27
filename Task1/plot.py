import matplotlib.pyplot as plt
import os
from numpy.typing import NDArray
import numpy as np
from tkinter import simpledialog

def plot_data(data_arrays,labels = None, save =False, dataname:str="Unnamed"):
    for data in data_arrays:
        if not isinstance(data, np.ndarray):
            raise ValueError("All input data must be NumPy arrays")
    markers = ['o', 's', '^', 'd', '*', 'x', 'v', '>', '<', 'p', 'h', '+', '1', '2', '3', '4', '|', '_', 'D', 'H', '.', ',', 'P', 'X']
    for i, data in enumerate(data_arrays):
        plt.plot(data_arrays[i][:, 0], data_arrays[i][:, 1], label=labels[i], marker=markers[i % len(markers)])
    plt.xlabel(r'Velocity $\left[\frac{\mathit{m}}{\mathit{s}}\right]$', fontsize=15)
    plt.ylabel("Power produced[W]", fontsize=15)
    plt.legend()
    plt.title(f"Power curve for {dataname}")
    plt.grid(True)
    if not save:
        plt.show()
        plt.close()
        user_input = simpledialog.askstring("save plot", "Do you want to save the plot? (yes/no): ").strip().lower()
        if user_input in ['yes', 'y']:
            plot_data(data_arrays, labels = labels,dataname =dataname, save = True)
    else:
        save_path = simpledialog.askstring("Filename", "Enter the filename (e.g., plot.png): ").strip()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()

if __name__ == "__main__":
    data1 = np.array([[1, 2], [2, 4], [3, 1], [4, 3], [5, 5]])
    data2 = np.array([[1, 2], [2, 4], [3, 4], [4, 3], [5, 5]])
    data_arrays = [data1,data2]
    plot_data(*data_arrays,labels=["data1","data2"])
