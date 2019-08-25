# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)

data['Gender'].replace('-','Agender',inplace=True)

gender_count = data.Gender.value_counts()

gender_count.plot(kind='bar',legend='best')

#Code starts here 




# --------------
#Code starts here


alignment = data['Alignment'].value_counts()
alignment.plot(kind='pie',legend='best')


# --------------
#Code starts here

sc_df = data[['Strength','Combat']]
#sc_df.head()

sc_covariance = sc_df.cov().iloc[0,1]

sc_strength = round(sc_df.Strength.std(),2)

sc_combat = round(sc_df.Combat.std(),2)

sc_pearson = round(sc_covariance / (sc_strength * sc_combat),2)
print(sc_strength)
print(sc_combat)
print(sc_pearson)

ic_df = data[['Intelligence','Combat']]
#ic_df.head()

ic_covariance = ic_df.cov().iloc[0,1]

ic_intelligence = round(ic_df.Intelligence.std(),2)

ic_combat = round(ic_df.Combat.std(),2)

ic_pearson = round(ic_covariance / (ic_intelligence * ic_combat),2)
print(ic_intelligence)
print(ic_combat)
print(ic_pearson)




# --------------
#Code starts here

total_high =  data['Total'].quantile(q=0.99)

print(total_high)

super_best = data[data['Total']>total_high]

#print(super_best.head())

super_best_names = list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here
fig1 = plt.figure(figsize=[10,5])
ax_1 = fig1.add_subplot(111)
ax_2 = fig1.add_subplot(121)
ax_3 = fig1.add_subplot(131)
#fig1 , axes = plt.subplots(nrows=1,ncols=3)
#fig1.add_axes()
ax_1.boxplot(data.Intelligence)
ax_2.boxplot(data.Speed)
ax_3.boxplot(data.Power)



