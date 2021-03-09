

#  importing file 

cars <- read.csv(file.choose())

attach(cars)

#1st moment of business decision 
#measure  of central tendency
mean(speed)   #15.4
median(speed) #15

mean(dist)   #42.98
median(dist)   #36

#2nd moment of business decision
#measure of dispersion

#variance
var(speed)  #27.95
var(dist)  # 664.06
#standard deviation 
sd(speed)   #5.28
sd(dist)    #25.76
#Range 
range_sp = max(speed) - min(speed) 
range_sp

range_dist = max(dist)-min(dist)
range_dist


library(moments)

#3rd moment of business decision #skewness

skewness(speed) #  -0.11
skewness(dist)   # 0.78

#4th moment of business decision #kurtosis peakness of dataset 


kurtosis(speed)  #2.42
kurtosis(dist)    #3.24



#Q2

sp_wt=read.csv(file.choose())


attach(sp_wt)


#1st  moment of business decision measure of central tendency

mean(SP)   #121.54
median(SP) #118

mean(WT)   #32.41
median(WT)   #32.73


#2nd moment of business decision 
#measure of dispersion

#variance
var(SP) #201.11
var(WT)    #  56.14

#standard deviation

sd(SP)   #14.18
sd(WT)    #7.49


#range
ran_sp=max(SP) - min(SP)
ran_sp

ran_wt=max(WT) - min(WT)
ran_wt

library(moments)
#3rd moment of business decision skewness

skewness(SP)
skewness(WT)

#4th moment of business decision kurtosis

kurtosis(SP)
kurtosis(WT)


