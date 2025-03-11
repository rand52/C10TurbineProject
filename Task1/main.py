from datasplitting import DataSplit
import numpy as np
import os
import matplotlib.pyplot as plt
File_Names = ['noshear TIC_veer0.2','noshear TIC_veer0.4','noshear_TIA_veer0.2','noshear_TIA_veer0.4','noshear_TIA_veer0.05','noshear_TIC_veer0.05','noTI_shear0.2_veer0.2','noTI_shear0.2_veer0.4','noTI_shear0.2_veer0.05','noTI_shear0.12_veer0.2','noTI_shear0.12_veer0.4','noTI_shear0.12_veer0.05','noveer_shear0.2_TIA','noveer_shear0.2_TIC','noveer_shear0.12_TIA','noveer_shear0.12_TIC','shear0.2','shear0.12','TIA','TIC','Uniform_noshear_noveer_noTI','veer0.2','veer0.4','veer0.05']
names = ['Extracted_Uref3.csv','Extracted_Uref4.csv','Extracted_Uref5.csv','Extracted_Uref6.csv','Extracted_Uref7.csv','Extracted_Uref8.csv','Extracted_Uref9.csv','Extracted_Uref10.csv','Extracted_Uref10.59.csv','Extracted_Uref11.csv','Extracted_Uref12.csv','Extracted_Uref13.csv','Extracted_Uref14.csv','Extracted_Uref15.csv','Extracted_Uref16.csv','Extracted_Uref17.csv','Extracted_Uref18.csv','Extracted_Uref19.csv','Extracted_Uref20.csv']

wind = [0, 1, 2]
power = [0, 0, 0]

for i in range(len(names)):
    file_path = os.path.join('Task1/Data/Uniform_noshear_noveer_noTI',names[i])
    Times, Wind1VelXs, Wind1VelYs, Wind1VelZs, GenPwrs = DataSplit(file_path)
    print("Average power produced:", np.mean(GenPwrs))
    print("Average wind speed:", np.mean(Wind1VelXs))
    # print(DataSplit("Task1/Data/noshear TIC_veer0.2/Extracted_Uref3.csv"))
    
    wind.append(np.mean(Wind1VelXs))
    power.append(np.mean(GenPwrs))



print(wind)
print(power)
# Create the plot
plt.plot(wind, power, marker='o', linestyle='-')

# Labels and title
plt.xlabel('Wind')
plt.ylabel('Power')
plt.title('Simple Plot')

# Show the plot
plt.show()


