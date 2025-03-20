from datasplitting import DataSplit
from window import select_datasets
import numpy as np
import os
from numpy.typing import NDArray
from rich.progress import Progress
import tkinter as tk
from tkinter import simpledialog, ttk

File_Names = ['noshear TIC_veer0.2','noshear TIC_veer0.4','noshear_TIA_veer0.2','noshear_TIA_veer0.4','noshear_TIA_veer0.05','noshear_TIC_veer0.05','noTI_shear0.2_veer0.2','noTI_shear0.2_veer0.4','noTI_shear0.2_veer0.05','noTI_shear0.12_veer0.2','noTI_shear0.12_veer0.4','noTI_shear0.12_veer0.05','noveer_shear0.2_TIA','noveer_shear0.2_TIC','noveer_shear0.12_TIA','noveer_shear0.12_TIC','shear0.2','shear0.12','TIA','TIC','Uniform_noshear_noveer_noTI','veer0.2','veer0.4','veer0.05']
names = ['Extracted_Uref3.csv','Extracted_Uref4.csv','Extracted_Uref5.csv','Extracted_Uref6.csv','Extracted_Uref7.csv','Extracted_Uref8.csv','Extracted_Uref9.csv','Extracted_Uref10.csv','Extracted_Uref10.59.csv','Extracted_Uref11.csv','Extracted_Uref12.csv','Extracted_Uref13.csv','Extracted_Uref14.csv','Extracted_Uref15.csv','Extracted_Uref16.csv','Extracted_Uref17.csv','Extracted_Uref18.csv','Extracted_Uref19.csv','Extracted_Uref20.csv','Extracted_Uref21.csv']

DataSet:dict = {} 

with Progress() as progress:
  task = progress.add_task("[cyan]Processing...", total=len(File_Names))

  for filename in File_Names:
    folder_path = f"Task1/Data/{filename}"
    files = os.listdir(folder_path)  # Get all files and folders in the directory
    file_count = len([f for f in files if os.path.isfile(os.path.join(folder_path, f))])
    windspeed = [0,1,2]
    power = [0,1,2]
    for i in range(file_count):
      file_path = f"Task1/Data/{filename}/{names[i]}"
      if not os.path.exists(file_path):
          print(f"File not found: {file_path}, skipping...")
          continue
      Times, Wind1VelXs, Wind1VelYs, Wind1VelZs, GenPwrs = DataSplit(file_path)

      windspeed.append(np.mean(Wind1VelXs))
      power.append(np.mean(GenPwrs))
    Data:NDArray = np.column_stack((windspeed, power))
    if filename not in DataSet:
      DataSet[filename] = Data
    progress.update(task, advance=1)

# Main loop for selecting datasets and plotting
testing = True
while testing:
    select_datasets(DataSet)

    # After the plot is done and the window is closed, ask if they want to plot more data
    retry = simpledialog.askstring("Plot More?", "Plot more data? (y/n):")
    if retry and retry.lower() == "n":
        testing = False

# testing = True
# while testing:
#   number = input("Number of data to be plotted: ")
#   data_list = []
#   labels = []
#   for i in range(int(number)):
#     Call_dataset = input(f"Folder name of desired data{i}: ")
#     data_list.append(DataSet[Call_dataset])
#     labels.append(Call_dataset)
#   plot_data(*data_list,labels=labels)
#   if input("Plot more data? (y/n): ") == "n":
#     testing = False