import matplotlib.pyplot as plt
import matplotlib.animation as animation

# imports of internal data from reader
from data_reader import get_probe_locations, get_velocity_data, Vx_index, Vy_index, Vz_index

# test
##### individual plot parameters ######
transparency = 0.7  # 0=completely transparent 1=completely solid
size = 10
marker_type = 'o'  # 'o' = circles ; 's' = squares; '*'= stars

##### animation parameters #####
fps = 10  # frames in a sec

# time_step from the simulation at which data is presented
data_time_step = 10  # sec

# load probe locations
x,y,z = get_probe_locations()
# load velocity data
velocity_data, time_steps = get_velocity_data(time_between_datapts=data_time_step)

# Initialize plot with first frame
v_z = velocity_data[0, :, Vx_index]  # First time step of respective velocity component
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
ani = animation.FuncAnimation(fig, update, frames=len(time_steps), blit=False)

# Save as GIF
ani.save('3d_animation.gif', writer='pillow', fps=fps)
