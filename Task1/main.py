from datasplitting import DataSplit
import numpy as np
name2 = [Extracted_Uref3.csv, Extracted_Uref4.csv, Extracted_Uref5.csv, Extracted_Uref6.csv, Extracted_Uref7.csv, Extracted_Uref8.csv, Extracted_Uref9.csv, Extracted_Uref10.csv, Extracted_Uref10.59.csv, Extracted_Uref11.csv, Extracted_Uref12.csv, Extracted_Uref13.csv, Extracted_Uref14.csv, Extracted_Uref15.csv, Extracted_Uref16.csv, Extracted_Uref17.csv, Extracted_Uref18.csv, Extracted_Uref19.csv, Extracted_Uref20.csv]
Times, Wind1VelXs, Wind1VelYs, Wind1VelZs, GenPwrs = DataSplit("Task1/Data/noshear TIC_veer0.2/Extracted_Uref3.csv")
print(Times)
print("Average power produced:", np.mean(GenPwrs))
# print(DataSplit("Task1/Data/noshear TIC_veer0.2/Extracted_Uref3.csv"))

wind = []
power = []

wind.np.mean(Wind1VelXs)
power.np.mean(GenPwrs)



import matplotlib.pyplot as plt

# Create the plot
plt.plot(Times, GenPwrs, marker='o', linestyle='-')

# Labels and title
plt.xlabel('Time')
plt.ylabel('Power')
plt.title('Simple Plot')

# Show the plot
plt.show()
