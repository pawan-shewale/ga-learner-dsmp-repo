# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here

df =  pd.read_csv(path)
print(df.columns)
p_a = len(df[df['fico']>700])/len(df)
print(p_a)

p_b = len(df[df['purpose'] == 'debt_consolidation'])/len(df)
print(p_b)

df1 = df[df['purpose'] == 'debt_consolidation']

p_a_b = p_b*(len(df1[df1['purpose'] == 'debt_consolidation'])/len(df[df['fico']>700]))/p_a

print(p_a_b)
result = False;
if(p_a_b == p_a):
    result = True
print(result)
# code ends here


# --------------
# code starts here

prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df)
print(prob_lp)
prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df)
print(prob_cs)

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)

bayes = prob_pd_cs * prob_lp / prob_cs

print(bayes)
# code ends here


# --------------
# code starts here

df.purpose.value_counts().plot(kind='bar')

df1 = df[df['paid.back.loan'] == 'No']

df1.purpose.value_counts().plot(kind='bar')
# code ends here


# --------------
# code starts here

inst_median = df['installment'].median()
print(inst_median)
inst_mean = df['installment'].mean()
print(inst_mean)
plt.hist(df['installment'])


plt.hist(df['log.annual.inc'])


# code ends here


