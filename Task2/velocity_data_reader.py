import numpy as np
import os

# File path MAC and Windows
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
file_path = os.path.join(current_dir, 'Data', 'U_withAGW')

# time offset of start of data gathering since simulation start
time_start_point = 21600
# time step used in the simulation
global_simulation_time_step = 0.5  # sec

# Num. lines with probes
num_probes = 3572
# space between position data and velocity data
skip_lines = 2
# Num. time steps
num_time_steps_tot = 3600

# 3d with first index being the time step
# 0 index: time step index
# 1 index: datapoint index
# 2 index: 0->x  1->y  2->z velocity component
Vx_index = 0
Vy_index = 1
Vz_index = 2


def get_probe_locations():
    print("Reading probe locations")

    # Load tha data
    with open(file_path, "r") as file:
        lines = file.readlines()
        file.close()

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

    return x, y, z


def get_velocity_data(time_between_datapts=10):
    # Load tha data
    with open(file_path, "r") as file:
        lines = file.readlines()
        file.close()

    # number lines between datapoints to be read
    splitter = round(time_between_datapts / global_simulation_time_step)
    # selecting the lines to be read
    lines = lines[num_probes + skip_lines::splitter]
    # number of datapoints to be read
    num_datpts = len(lines)
    # time step array
    time_steps = np.empty(num_datpts)

    # 3d with first index being the time step
    # 0 index: time step index
    # 1 index: datapoint index
    # 2 index: 0->x  1->y  2->z velocity component
    velocity_data = np.empty((num_datpts, num_probes, 3))

    for t, line in enumerate(lines):  # Work after all the probe locations are read
        # read of the time
        line = line.strip("\n")  # removes the new line at the end of the line
        line_parts = line.split("(")  # split on first brackets
        time_steps[t] = float(line_parts[0]) - time_start_point
        # process the rest of the datapoints on the line into the velocity components
        for i, datpt in enumerate(line_parts[1::]):
            # strip and split data from (vx,vy,vz) to arr[vx,vy,vz]
            stripped_data = datpt.strip(') ')  # remove second bracket and spaces if they are present
            data = stripped_data.split()
            data = np.array(data).astype(float)
            # save datapoint
            velocity_data[t, i] = data

        print(f"Reading line {t}/{num_datpts}")

    return velocity_data,time_steps
