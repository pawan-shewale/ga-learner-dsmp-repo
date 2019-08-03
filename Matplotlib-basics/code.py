# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)
print(data.columns)
loan_status = data['Loan_Status'].value_counts()
print(loan_status)

plt.plot(loan_status.index,loan_status)


#Code starts here


# --------------
#Code starts here




property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()

property_and_loan.plot.bar(stacked=False)


plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.title('Property Area vs Loan Status')




# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()


education_and_loan.plot.bar(stacked=True)

plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.title('Education vs Loan Status')

plt.xticks(rotation=45)


# --------------
#Code starts here

graduate  = data[data['Education'] == 'Graduate']
not_graduate  = data[data['Education'] == 'Not Graduate']

plt.plot()

graduate['LoanAmount'].plot(kind='density',label='Graduate',color='red')



not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate',color='green')






#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
#fig = plt.figure(figsize =[15,10])
fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1)

ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
#ax_1.title('Applicant Income')
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
#ax_2.title('Coapplicant Income')

data['TotalIncome']  = data['ApplicantIncome']+data['CoapplicantIncome']

ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
#ax_3.title('Total Income')
#fig.add_axes(ax_1,ax_2,ax_3)




