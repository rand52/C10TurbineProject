import numpy as np
import os
import matplotlib.pyplot as plt

# Importing data
from velocity_data_reader import get_probe_locations, get_velocity_data, Vx_index, Vy_index, Vz_index

velocity_data, time_steps = get_velocity_data(time_between_datapts=10)

directory = 'plots'
# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)

# Ensure matching dimensions
if velocity_data.shape[0] != len(time_steps):
    min_length = min(velocity_data.shape[0], len(time_steps))
    time_steps = time_steps[:min_length]
    velocity_data = velocity_data[:min_length, :, :]
    print("Adjusted time_steps and velocity_data to match dimensions.")

num_mesh_points = velocity_data.shape[1]  # Assuming columns are mesh points
num_time_steps = velocity_data.shape[0]    # Assuming rows are time steps

# Select three mesh points (specific indices)
selected_points = [85, 758, 3478]  # Change these indices as needed
Horizontal_points = [23, 1762, 3548] #Change these as the horizontal points
Vertical_points = [1739, 1762, 1785] #Change these as the vertical points

time = time_steps  # Use provided time steps from data

# Plot velocity for selected mesh points
def plot_velocity_random():
    plt.figure(figsize=(10, 5))
    offset = 0
    for idx in selected_points:
        plt.plot(time, velocity_data[:, idx, Vx_index], label=f'Mesh Point {idx}')

        # Add text in the bottom-right corner
        plt.text(0.98, 0.95-offset, f'Mesh pt {idx} V avg. {np.average(velocity_data[:, idx, Vx_index]):.2f} m/s',
                transform=plt.gca().transAxes,  # Use axis coordinates
                fontsize=10, color='black',
                ha='right', va='bottom')
        offset += 0.05


    plt.xlabel('Time [s]')
    plt.ylabel('Velocity (Vx) [m/s]')
    plt.title('Velocity vs Time for Randomly Selected Mesh Points')
    plt.legend()
    plt.grid()
    plt.savefig(directory + '/random_points_velocities.png')
    plt.show()

plot_velocity_random()


def plot_velocity_horizontal():
    plt.figure(figsize=(10, 5))

    offset = 0
    for idx in Horizontal_points:
        plt.plot(time, velocity_data[:, idx, Vx_index], label=f'Mesh Point {idx}')
       
        # Add text in the bottom-right corner
        plt.text(0.98, 0.95-offset, f'Mesh pt {idx} V avg. {np.average(velocity_data[:, idx, Vx_index]):.2f} m/s',
                transform=plt.gca().transAxes,  # Use axis coordinates
                fontsize=10, color='black',
                ha='right', va='bottom')
        offset += 0.05

    plt.xlabel('Time [s]')
    plt.ylabel('Velocity (Vx) [m/s]')
    plt.title('Velocity vs Time for Horizontal Mesh Points')
    plt.legend()
    plt.grid()
    plt.savefig(directory + '/horizontal_points_velocities.png')
    plt.show()

plot_velocity_horizontal()

def plot_velocity_vertical():
    plt.figure(figsize=(10, 5))
    offset = 0
    for idx in Vertical_points:
        plt.plot(time, velocity_data[:, idx, Vx_index], label=f'Mesh Point {idx}')
       
        # Add text in the bottom-right corner
        plt.text(0.98, 0.95-offset, f'Mesh pt {idx} V avg. {np.average(velocity_data[:, idx, Vx_index]):.2f} m/s',
                transform=plt.gca().transAxes,  # Use axis coordinates
                fontsize=10, color='black',
                ha='right', va='bottom')
        offset += 0.05


    plt.xlabel('Time [s]')
    plt.ylabel('Velocity (Vx) [m/s]')
    plt.title('Velocity vs Time for Vertical Mesh Points (lowest number is highest point)')
    plt.legend()
    plt.grid()
    plt.savefig(directory + '/vertical_points_velocities.png')
    plt.show()

plot_velocity_vertical()




