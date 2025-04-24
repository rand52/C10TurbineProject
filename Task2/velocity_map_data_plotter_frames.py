import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# imports of internal data from reader
from velocity_data_reader import get_probe_locations, get_velocity_data, Vx_index

##### Individual plot parameters #####
transparency = 0.7  # 0=completely transparent, 1=completely solid
size = 10
marker_type = 'o'  # 'o' = circles; 's' = squares; '*' = stars

##### Simulation parameters #####
data_time_step = 10  # seconds per time step

# Load probe locations
x, y, z = get_probe_locations()
# Load velocity data
velocity_data, time_steps = get_velocity_data(time_between_datapts=data_time_step)

# Create output directory if it doesn't exist
output_folder = "animation_frames"
os.makedirs(output_folder, exist_ok=True)

# Generate and save each frame
for frame in range(len(time_steps)):
    print(f"Saving frame {frame + 1}/{len(time_steps)}")
    v_z = velocity_data[frame, :, Vx_index]  # Velocity data for current frame

    # Create figure
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(x, y, z, c=v_z, cmap='viridis', marker=marker_type, alpha=transparency, s=size)

    # Add color bar
    cbar = plt.colorbar(sc, ax=ax, shrink=0.5, aspect=10)
    cbar.set_label("Vx [m/s]")

    # Labels
    ax.set_xlabel('X coord [m]')
    ax.set_ylabel('Y coord [m]')
    ax.set_zlabel('Z coord [m]')
    ax.set_title(f'Velocity 3D Map at time {time_steps[frame]} sec')

    # Save the frame
    frame_filename = os.path.join(output_folder, f"frame_{frame:04d}.png")
    plt.savefig(frame_filename, dpi=150, bbox_inches='tight')
    plt.close(fig)  # Close figure to free memory

print("All frames saved successfully!")