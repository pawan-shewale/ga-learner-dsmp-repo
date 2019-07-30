# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

bank = pd.read_csv(path)
#bank = pd.Dataframe(data)
print(bank.info())
#print(bank.head())
#print(bank.shape)


# code starts here
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)



# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],axis=1)
#print(banks.head)
print(banks.isnull().sum())
#print(null_values)
bank_mode = banks.mode().iloc[0]
print(bank_mode)
#print(bank_mode)
banks.fillna(bank_mode,inplace=True)
#print(banks)
#print(banks.head)
null_values = banks.isnull().sum() 
print(null_values)
#code ends here


# --------------
# Code starts here




avg_loan_amount = pd.pivot_table(banks,index=('Gender','Married','Self_Employed'),values='LoanAmount')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here
print(banks.columns)



loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].index.value_counts().sum()
print(loan_approved_se)
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].index.value_counts().sum()
print(loan_approved_nse)
percentage_se = (loan_approved_se/614)*100
percentage_nse = (loan_approved_nse/614)*100
print(percentage_se,percentage_nse)
# code ends here


# --------------
# code starts here




loan_term = banks.Loan_Amount_Term.apply(lambda x:x/12 if x != 0 else x)
#print(long_term)
big_loan_term = banks[banks['Loan_Amount_Term'] >= 300 ].index.value_counts().sum()

print(big_loan_term)
# code ends here


# --------------
# code starts here

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])
print(loan_groupby)
loan_groupby=loan_groupby[columns_to_show]
print(loan_groupby)
# Check the mean value 
mean_values=loan_groupby.agg([np.mean])

print(mean_values)

# code ends here


