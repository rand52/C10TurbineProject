from datasplitting import DataSplit
import numpy as np
import os

names = ['Extracted_Uref3.csv','Extracted_Uref4.csv','Extracted_Uref5.csv','Extracted_Uref6.csv','Extracted_Uref7.csv','Extracted_Uref8.csv','Extracted_Uref9.csv','Extracted_Uref10.csv','Extracted_Uref10.59.csv','Extracted_Uref11.csv','Extracted_Uref12.csv','Extracted_Uref13.csv','Extracted_Uref14.csv','Extracted_Uref15.csv','Extracted_Uref16.csv','Extracted_Uref17.csv','Extracted_Uref18.csv','Extracted_Uref19.csv','Extracted_Uref20.csv','Extracted_Uref21.csv']

def turbulence(folder_path):
    meanwind = []
    defwind = []

    for name in names:
        file_path = os.path.join(folder_path, name)
        if not os.path.exists(file_path):
            #print(f"File not found: {file_path}, skipping...")
            continue
        Times, Wind1VelXs, Wind1VelYs, Wind1VelZs, GenPwrs = DataSplit(file_path)
        meanwind.append(np.mean(Wind1VelXs)) 
        defwind.append(np.std(Wind1VelXs))

    turbulence = []
    for i in range(len(meanwind)):
        turbulence.append(defwind[i]/meanwind[i])
    return turbulence

print(np.mean(turbulence("Task1/Data/TIA")))
print(np.mean(turbulence("Task1/Data/TIC")))
print(np.mean(turbulence("Task1/Data/Uniform_noshear_noveer_noTI")))