import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('C:\\Users\\user\\OneDrive\\Desktop\\Data.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_test)



plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience(training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience(test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
