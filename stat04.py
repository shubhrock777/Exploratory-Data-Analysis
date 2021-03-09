
#Q1


import pandas as pd 


cars=pd.read_csv("D:\\BLR10AM\\Assi\\04.statistical data visulization plot\\Statistical Datasets\\Statistical Datasets\\Q1_a.csv")

cars.info()

cars.describe()


#1st moment of business decision 
#measure  of central tendency
#mean
cars.speed.mean()
cars.dist.mean()

#median
cars.speed.median()
cars.dist.median()

#2nd moment of business decision
#measure of dispersion

#variance
cars.speed.var()
cars.dist.var()
#standard deviation 
cars.speed.std()
cars.dist.std()
#Range 
range_sp = max(cars.speed) - min(cars.speed) 
range_sp

range_dist = max(cars.dist)-min(cars.dist)
range_dist


#3rd moment of business decision #skewness

cars.speed.skew()
cars.dist.skew()

#4th moment of business decision #kurtosis peakness of dataset 

cars.speed.kurt()
cars.dist.kurt()

import matplotlib.pyplot as plt

plt.hist(cars.speed)
plt.hist(cars.dist)

plt.boxplot(cars.speed)
plt.boxplot(cars.dist)


#Q2

sp_wt=pd.read_csv("D:/practice/Statistical 04/DataSets/Q2_b.csv")

sp_wt.info()

sp_wt.describe()


#from scipy.stats import stats

#1st  moment of business decision measure of central tendency
#mean
sp_wt.SP.mean()
sp_wt.WT.mean()

#median
sp_wt.SP.median()
sp_wt.WT.median()

#2nd moment of business decision 
#measure of dispersion

#variance
sp_wt.SP.var()
sp_wt.WT.var()

#standard deviation

sp_wt.SP.std()
sp_wt.WT.std()


#range
ran_sp=max(sp_wt.SP) - min(sp_wt.SP)
ran_sp

ran_wt=max(sp_wt.WT) - min(sp_wt.WT)
ran_wt


#3rd moment of business decision skewness

sp_wt.SP.skew()
sp_wt.WT.skew()

#4th moment of business decision kurtosis

sp_wt.SP.kurt()
sp_wt.WT.kurt()



















