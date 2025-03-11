from datasplitting import DataSplit
import numpy as np
Times, Wind1VelXs, Wind1VelYs, Wind1VelZs, GenPwrs = DataSplit("Task1/Data/noshear TIC_veer0.2/Extracted_Uref3.csv")
print(Times)
print("Average power produced:", np.mean(GenPwrs))
# print(DataSplit("Task1/Data/noshear TIC_veer0.2/Extracted_Uref3.csv"))

FileNames = ['noshear TIC_veer0.2','noshear TIC_veer0.4','noshear_TIA_veer0.2','noshear_TIA_veer0.4','noshear_TIA_veer0.05','noshear_TIC_veer0.05','noTI_shear0.2_veer0.2','noTI_shear0.2_veer0.4','noTI_shear0.2_veer0.05','noTI_shear0.12_veer0.2','noTI_shear0.12_veer0.4','noTI_shear0.12_veer0.05','noveer_shear0.2_TIA','noveer_shear0.2_TIC','noveer_shear0.12_TIA','noveer_shear0.12_TIC','shear0.2','shear0.12','TIA','TIC','Uniform_noshear_noveer_noTI','veer0.2','veer0.4','veer0.05']