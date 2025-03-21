import matplotlib.pyplot as plt
import os
from numpy.typing import NDArray
import numpy as np
def plot_data(data_arrays,labels = None, save =False, dataname:str="Unnamed"):
    for data in data_arrays:
        if not isinstance(data, np.ndarray):
            raise ValueError("All input data must be NumPy arrays")
    for i, data in enumerate(data_arrays):
        plt.plot(data_arrays[i][:, 0], data_arrays[i][:, 1], label=labels[i])
    plt.xlabel("Uref[m/s^2]")
    plt.ylabel("Power produced[W]")
    plt.legend()
    plt.title(f"Power curve for {dataname}")
    plt.grid(True)
    if not save:
        plt.show()
        plt.close()
        user_input = input("Do you want to save the plot? (yes/no): ").strip().lower()
        if user_input in ['yes', 'y']:
            plot_data(data_arrays, labels = labels, save = True)
    else:
        save_path = input("Enter the filename (e.g., plot.png): ").strip()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()

if __name__ == "__main__":
    data1 = np.array([[1, 2], [2, 4], [3, 1], [4, 3], [5, 5]])
    data2 = np.array([[1, 2], [2, 4], [3, 4], [4, 3], [5, 5]])
    data_arrays = [data1,data2]
    plot_data(*data_arrays,labels=["data1","data2"])
