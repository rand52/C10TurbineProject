from data_reader import get_probe_locations, get_velocity_data
import math as mt

x, y, z = get_probe_locations()

num_pts_in_z = 47
num_pts_in_y = 76

pt_along_y_left_index = mt.floor((num_pts_in_z - 1) / 2)
pt_along_y_mid_index = mt.floor((num_pts_in_y - 1) / 2)*num_pts_in_z + mt.floor(num_pts_in_z / 2)
pt_along_y_right_index = (num_pts_in_y - 1)*num_pts_in_z + mt.floor(num_pts_in_z / 2)

pt_along_z_top_index = mt.floor((num_pts_in_y - 1) / 2)*num_pts_in_z
pt_along_z_mid_index = mt.floor((num_pts_in_y - 1) / 2)*num_pts_in_z + mt.floor(num_pts_in_z / 2)
pt_along_z_bot_index = mt.floor((num_pts_in_y - 1) / 2)*num_pts_in_z + (num_pts_in_z - 1)

print(x[pt_along_y_left_index],y[pt_along_y_left_index],z[pt_along_y_left_index])
print(x[pt_along_y_mid_index],y[pt_along_y_mid_index],z[pt_along_y_mid_index])
print(x[pt_along_y_right_index],y[pt_along_y_right_index],z[pt_along_y_right_index])
print()
print(x[pt_along_z_top_index],y[pt_along_z_top_index],z[pt_along_z_top_index])
print(x[pt_along_z_mid_index],y[pt_along_z_mid_index],z[pt_along_z_mid_index])
print(x[pt_along_z_bot_index],y[pt_along_z_bot_index],z[pt_along_z_bot_index])