import matplotlib.pyplot as plt

from data_reader import x,y,z,velocity_data,time_steps,Vx_index,Vy_index,Vz_index

# get velocity data for Vx only
v_z = velocity_data[0, :,Vx_index]


# Create a 3d figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(x, y, z, c=v_z, cmap='viridis', marker='o', alpha=0.6)

# Add color bar
cbar = plt.colorbar(sc, ax=ax, shrink=0.5, aspect=10)
cbar.set_label("Value Intensity")

# Labels
ax.set_xlabel('X coord')
ax.set_ylabel('Y coord')
ax.set_zlabel('Z coord')
ax.set_title('3D Cloud Map at time step ')

plt.show()