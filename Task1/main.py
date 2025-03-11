from datasplitting import DataSplit
import numpy as np
Times, Wind1VelXs, Wind1VelYs, Wind1VelZs, GenPwrs = DataSplit("Task1/Data/noshear TIC_veer0.2/Extracted_Uref3.csv")
print(Times)
print("Average power produced:", np.mean(GenPwrs))
# print(DataSplit("Task1/Data/noshear TIC_veer0.2/Extracted_Uref3.csv"))