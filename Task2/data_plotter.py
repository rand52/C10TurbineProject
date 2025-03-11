import matplotlib.pyplot as plt
import matplotlib.animation as animation

# imports of internal data from reader
from data_reader import x, y, z, velocity_data, time_steps, Vx_index, Vy_index, Vz_index

##### selecting the desired time steps for the animation
simulation_time_between_frames = 10 # sec between two consecutive frames in the simulation data
simulation_time_step = 0.5 # sec

##### individual plot parameters ######
transparency = 0.7  # 0=completely transparent 1=completely solid
size = 10
marker_type = 'o'  # 'o' = circles ; 's' = squares; '*'= stars

##### animation parameters #####
interval = 200  # time in milliseconds between two frames in gif


# select data to be plotted
splitter = round(simulation_time_between_frames/simulation_time_step)
time_steps = time_steps [::splitter]
velocity_data = velocity_data [::splitter,:,:]


# Initialize plot with first frame
v_z = velocity_data[0, :, Vx_index]  # First time step
# Create a 3d figure
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
# set the title as an object to update it with the update func for the animation
title = ax.set_title(f'Velocity 3D Map at time {time_steps[0]} sec')


def update(frame):
    print(f"Drawing frame {frame}/{len(time_steps)}")
    v_z = velocity_data[frame, :, Vx_index]  # Update velocity data
    sc.set_array(v_z)  # Update color values for new v data
    title.set_text(f'Velocity 3D Map at time {time_steps[frame]} sec')  # update the title
    return sc, title


# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(time_steps), interval=200, blit=False)

# Save as GIF
ani.save('3d_animation.gif', writer='pillow', fps=10)

