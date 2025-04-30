import os
import matplotlib.pyplot as plt
import numpy as np

# imports of internal data from reader
from velocity_data_reader import get_probe_locations, get_velocity_data, Vx_index

##### Individual plot parameters #####
transparency = 0.5  # 0=completely transparent, 1=completely solid
size = 1
marker_type = 'o'  # 'o' = circles; 's' = squares; '*' = stars

##### Simulation parameters #####
data_time_step = 2 # seconds per time step

# Load probe locations
x, y, z = get_probe_locations()
# Load velocity data
print("Loading data...")
velocity_data, time_steps = get_velocity_data(time_between_datapts=data_time_step)
velocity_data_x = velocity_data[:, :, Vx_index]  # Velocity data perpendicular to rotor
# velocity and z locations data in first column only (y=1122)


##### Plot along Z #####
print("Processing average velocities Z ....")
# Load up just one set of coordinates and not the 3d mesh
z = z[:47]
y = y[::47]

# split velocity datapoints for each timestep first along z rows and then along y columns
# index 1: time
# index 2: row (z=const)
# index 3: column (y=const)
velocities_ordered = np.empty((len(time_steps), len(z), len(y)))
for time, vel_at_time in enumerate(velocity_data_x):
    for i, _ in enumerate(z):
        velocities_ordered[time,i] = vel_at_time[i::len(z)]
# Average the velocities along each row(z=const), so by the last axis
velocities_row_avg = velocities_ordered.mean(axis=2)

# Flatten the velocity array by columns for plotting, as we first plot by time, which is constant over rows, so it changes in columns
velocity = velocities_row_avg.flatten(order='F')

# Create a grid of time and height values and flatten to create a list of coordinates for scatter plot
time_grid, height_grid = np.meshgrid(time_steps, z)
time = time_grid.flatten()
height = height_grid.flatten()

# Create output directory if it doesn't exist
output_folder = "velocity_in_time_plots"
os.makedirs(output_folder, exist_ok=True)

# Create figure
print("Plotting Z ....")
plt.figure(figsize=(30, 8))
# Create scatter plot
sc = plt.scatter(time, height, c=velocity, cmap='viridis', alpha=0.7, s=100)
# Add color bar
cbar = plt.colorbar(sc)  # Add color bar to the scatter plot
cbar.set_label("Vx [m/s]", fontsize=20)  # Set label for the color bar
cbar.ax.tick_params(labelsize=20)  # Make numbers on color bar bigger
# Bigger labels numbers
plt.tick_params(axis='both', labelsize=14)
# Labels
plt.ylabel('Z coord [m]', fontsize=20)
plt.xlabel('Time [s]', fontsize=20)
plt.title('Velocity in time', fontsize=30)

# Save the fig
plt_name = os.path.join(output_folder, f"velocity_in_time_Z_plot.png")
plt.savefig(plt_name, dpi=150, bbox_inches='tight')
plt.close()  # Close figure to free memory



##### Plot along Y #####
print("Processing average velocities Y ....")
# split velocity datapoints for each timestep first along y columns and then along z rows
# index 1: time
# index 2: column (y=const)
# index 3: row (z=const)
velocities_ordered = np.empty((len(time_steps), len(y), len(z)))
for time, vel_at_time in enumerate(velocity_data_x):
    for i, _ in enumerate(y):
        velocities_ordered[time,i] = vel_at_time[i*len(z):(i+1)*len(z):]
# Average the velocities along each column(y=const), so by the last axis
velocities_col_avg = velocities_ordered.mean(axis=2)

# Flatten the velocity array by columns for plotting, as we first plot by time, which is constant over rows, so it changes in columns
velocity = velocities_col_avg.flatten(order='F')

# Create a grid of time and height values and flatten to create a list of coordinates for scatter plot
time_grid, width_grid = np.meshgrid(time_steps, y)
time = time_grid.flatten()
width = width_grid.flatten()

# Create output directory if it doesn't exist
output_folder = "velocity_in_time_plots"
os.makedirs(output_folder, exist_ok=True)

# Create figure
print("Plotting Y ....")
plt.figure(figsize=(30, 10))
# Create scatter plot
sc = plt.scatter(time, width, c=velocity, cmap='viridis', alpha=0.7, s=100)
# Add color bar
cbar = plt.colorbar(sc)  # Add color bar to the scatter plot
cbar.set_label("Vx [m/s]", fontsize=20)  # Set label for the color bar
cbar.ax.tick_params(labelsize=20)  # Make numbers on color bar bigger
# Bigger labels numbers
plt.tick_params(axis='both', labelsize=14)
# Labels
plt.ylabel('Y coord [m]', fontsize=20)
plt.xlabel('Time [s]', fontsize=20)
plt.title('Velocity in time', fontsize=30)

# Save the fig
plt_name = os.path.join(output_folder, f"velocity_in_time_Y_plot.png")
plt.savefig(plt_name, dpi=150, bbox_inches='tight')
plt.close()  # Close figure to free memory


print("Figures saved successfully!")