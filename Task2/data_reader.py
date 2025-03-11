import numpy as np

# File path
file_path = "Data/U_withAGW"
# time offset of start of data gathering since simulation start
time_start_point = 21600
# Num. lines with probes
num_probes = 3572
# space between position data and velocity data
skip_lines = 2
# Num. time steps
num_time_steps = 3600

# Load tha data
with open(file_path, "r") as file:
    lines = file.readlines()

# probe positions arrays
x, y, z = np.empty(num_probes), np.empty(num_probes), np.empty(num_probes)

for i in range(num_probes):
    # split by first bracket, take second half, remove the second bracket and new line
    line_data = lines[i].split("(")[-1].strip(")\n")
    # from each data line split the entries
    data = line_data.split()
    # save
    x[i] = float(data[0])
    y[i] = float(data[1])
    z[i] = float(data[2])

# time step array
time_steps = np.empty(num_time_steps)

# 3d with first index being the time step
# 0 index: time step index
# 1 index: datapoint index
# 2 index: 0->x  1->y  2->z velocity component
velocity_data = np.empty((num_time_steps + 1, num_probes, 3))

# Constant indices for velocity components:
Vx_index = 0
Vy_index = 1
Vz_index = 2

for t, line in enumerate(lines[num_probes + skip_lines::]):  # Work after all the probe locations are read
    # read of the time
    line = line.strip("\n")  # removes the new line at the end of the line
    line_parts = line.split("(")  # split on first brackets
    time_steps[t] = float(line_parts[0]) - time_start_point
    # process the rest of the datapoints on the line into the velocity components
    for i, datpt in enumerate(line_parts[1::]):
        # trip and split data from (vx,vy,vz) to arr[vx,vy,vz]
        stripped_data = datpt.strip(') ')  # remove second bracket and spaces if they are present
        data = stripped_data.split()
        data = np.array(data).astype(float)
        # save datapoint
        velocity_data[t, i] = data

    print(f"Reading line {t}/{num_time_steps}")

