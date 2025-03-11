import pandas as pd
import numpy as np
def DataSplit(filename:str):
  Times = []
  Wind1VelXs = []
  Wind1VelYs = []
  Wind1VelZs = []
  GenPwrs = []
  with open(filename, mode="r", encoding="utf-8") as file:
    for line in file:
      Time, Wind1VelX, Wind1VelY, Wind1VelZ, GenPwr = line.strip().split(",")
      Times.append(float(Time))
      Wind1VelXs.append(float(Wind1VelX))
      Wind1VelYs.append(float(Wind1VelY))
      Wind1VelZs.append(float(Wind1VelZ))
      GenPwrs.append(float(GenPwr))
  return Times, Wind1VelXs, Wind1VelYs, Wind1VelZs, GenPwrs