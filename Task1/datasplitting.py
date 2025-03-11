import pandas as pd
import numpy as np
def DataSplit(filename:str):
  Times = []
  Wind1VelXs = []
  Wind1VelYs = []
  Wind1VelZs = []
  GenPwrs = []
  with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()  # Read all lines into a list
  total_lines = len(lines)
  start_index = (total_lines // 2)  # Find middle point

  for line in lines[start_index:]:
    Time, Wind1VelX, Wind1VelY, Wind1VelZ, GenPwr = line.strip().replace(" ", "").split(",")
    Times.append(float(Time))
    Wind1VelXs.append(float(Wind1VelX))
    Wind1VelYs.append(float(Wind1VelY))
    Wind1VelZs.append(float(Wind1VelZ))
    GenPwrs.append(float(GenPwr))
  return Times, Wind1VelXs, Wind1VelYs, Wind1VelZs, GenPwrs

# if __name__ == __a
