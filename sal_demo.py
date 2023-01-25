import pandas
dataset = pandas.read_csv('SalaryData.csv')
dataset
print("Here are some past data : " )
print("------------------------")
print (dataset)
y = dataset['Salary']
x = dataset['YearsExperience']
X = x.values.reshape(-1,1)

print("------------------------")


from sklearn.linear_model import LinearRegression

model = LinearRegression()

 
model.fit(X , y)

import sys
exp = sys.argv[1]

p = model.predict([[exp]])
print("Your salary for", exp , "yr experience will  be around :" ,  p)


