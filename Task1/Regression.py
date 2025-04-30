from datasplitting import DataSplit
import numpy as np
import os
from rich.progress import Progress
from tkinter import simpledialog
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from window_regression import get_four_values

File_Names = ['noshear TIC_veer0.2','noshear TIC_veer0.4','noshear_TIA_veer0.2','noshear_TIA_veer0.4','noshear_TIA_veer0.05','noshear_TIC_veer0.05','noTI_shear0.2_veer0.2','noTI_shear0.2_veer0.4','noTI_shear0.2_veer0.05','noTI_shear0.12_veer0.2','noTI_shear0.12_veer0.4','noTI_shear0.12_veer0.05','noveer_shear0.2_TIA','noveer_shear0.2_TIC','noveer_shear0.12_TIA','noveer_shear0.12_TIC','shear0.2','shear0.12','TIA','TIC','Uniform_noshear_noveer_noTI','veer0.2','veer0.4','veer0.05']
names = ['Extracted_Uref3.csv','Extracted_Uref4.csv','Extracted_Uref5.csv','Extracted_Uref6.csv','Extracted_Uref7.csv','Extracted_Uref8.csv','Extracted_Uref9.csv','Extracted_Uref10.csv','Extracted_Uref10.59.csv','Extracted_Uref11.csv','Extracted_Uref12.csv','Extracted_Uref13.csv','Extracted_Uref14.csv','Extracted_Uref15.csv','Extracted_Uref16.csv','Extracted_Uref17.csv','Extracted_Uref18.csv','Extracted_Uref19.csv','Extracted_Uref20.csv','Extracted_Uref21.csv']
file_parameters = {
    'noshear TIC_veer0.2':          {'Veer': 0.2,  'Shear': 0.0,   'TI': 0.12},
    'noshear TIC_veer0.4':          {'Veer': 0.4,  'Shear': 0.0,   'TI': 0.12},
    'noshear_TIA_veer0.2':          {'Veer': 0.2,  'Shear': 0.0,   'TI': 0.16},
    'noshear_TIA_veer0.4':          {'Veer': 0.4,  'Shear': 0.0,   'TI': 0.16},
    'noshear_TIA_veer0.05':         {'Veer': 0.05, 'Shear': 0.0,   'TI': 0.16},
    'noshear_TIC_veer0.05':         {'Veer': 0.05, 'Shear': 0.0,   'TI': 0.12},

    'noTI_shear0.2_veer0.2':        {'Veer': 0.2,  'Shear': 0.2,   'TI': 0.0},
    'noTI_shear0.2_veer0.4':        {'Veer': 0.4,  'Shear': 0.2,   'TI': 0.0},
    'noTI_shear0.2_veer0.05':       {'Veer': 0.05, 'Shear': 0.2,   'TI': 0.0},
    'noTI_shear0.12_veer0.2':       {'Veer': 0.2,  'Shear': 0.12,  'TI': 0.0},
    'noTI_shear0.12_veer0.4':       {'Veer': 0.4,  'Shear': 0.12,  'TI': 0.0},
    'noTI_shear0.12_veer0.05':      {'Veer': 0.05, 'Shear': 0.12,  'TI': 0.0},

    'noveer_shear0.2_TIA':          {'Veer': 0.0,  'Shear': 0.2,   'TI': 0.16},
    'noveer_shear0.2_TIC':          {'Veer': 0.0,  'Shear': 0.2,   'TI': 0.12},
    'noveer_shear0.12_TIA':         {'Veer': 0.0,  'Shear': 0.12,  'TI': 0.16},
    'noveer_shear0.12_TIC':         {'Veer': 0.0,  'Shear': 0.12,  'TI': 0.12},

    'shear0.2':                     {'Veer': 0.0,  'Shear': 0.2,   'TI': 0.0},
    'shear0.12':                    {'Veer': 0.0,  'Shear': 0.12,  'TI': 0.0},
    'TIA':                          {'Veer': 0.0,  'Shear': 0.0,   'TI': 0.16},
    'TIC':                          {'Veer': 0.0,  'Shear': 0.0,   'TI': 0.12},

    'Uniform_noshear_noveer_noTI': {'Veer': 0.0,  'Shear': 0.0,   'TI': 0.0},

    'veer0.2':                      {'Veer': 0.2,  'Shear': 0.0,   'TI': 0.0},
    'veer0.4':                      {'Veer': 0.4,  'Shear': 0.0,   'TI': 0.0},
    'veer0.05':                     {'Veer': 0.05, 'Shear': 0.0,   'TI': 0.0},
}

with Progress() as progress:
  task = progress.add_task("[cyan]Processing...", total=len(File_Names))
  power_wind = {}
  for filename in File_Names:
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    folder_path = os.path.join(current_dir, 'Data', filename)
    files = os.listdir(folder_path)  # Get all files and folders in the directory
    file_count = len([f for f in files if os.path.isfile(os.path.join(folder_path, f))])
    power = {}
    
    for i in range(file_count):
        file_path = os.path.join(current_dir, 'Data', filename, names[i])
        if not os.path.exists(file_path):
            #print(f"File not found: {file_path}, skipping...")
            continue
        Times, Wind1VelXs, Wind1VelYs, Wind1VelZs, GenPwrs = DataSplit(file_path)
        power[f"name_{names[i]}"] = np.mean(Wind1VelXs), np.mean(GenPwrs)
    power_wind[f"name_{filename}"] = power

    progress.update(task, advance=1)

#print(power_wind)


# main loop for createing the matrix
matrix = []

for outer_key, inner_dict in power_wind.items():
    clean_name = outer_key.replace("name_", "")

    if clean_name in file_parameters:
        for _, (wind, gen_power) in inner_dict.items():
            row = [
                gen_power,
                wind,
                file_parameters[clean_name]["TI"],
                file_parameters[clean_name]["Shear"],
                file_parameters[clean_name]["Veer"]
            ]
            matrix.append(row)
    else:
        print(f"Warning: {clean_name} not found in file_parameters")

# Convert to NumPy array (optional)
matrix_np = np.array(matrix)
#print(matrix_np)

# # Assuming matrix_np is already defined
y = matrix_np[:, 0]
X = matrix_np[:, 1:]

# Create polynomial features (degree=2 for quadratic)
poly = PolynomialFeatures(degree=10, include_bias=False)
X_poly = poly.fit_transform(X)

# Fit the model
model = LinearRegression()
model.fit(X_poly, y)

# Make a prediction
running = True
while running:
    values = get_four_values()
    prediction_x = np.array([values])  # Same number of features as original X
    prediction_x_poly = poly.transform(prediction_x)
    prediction = model.predict(prediction_x_poly)

    print(prediction)
    
    retry = simpledialog.askstring("Predict More?", "Predict more data? (y/n):")
    if retry and retry.lower() == "n":
        running = False
