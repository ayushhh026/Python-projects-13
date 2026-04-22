import pandas as pd
from sklearn.linear_model import LogisticRegression

iris_data=pd.read_csv('iris.csv')
# print(iris_data.head())

X = iris_data.drop(columns=['variety'])
Y = iris_data['variety']
# print(X.head())

model = LogisticRegression()

model.fit(X.values, Y)

predictions = model.predict([[6.1,2.9,4.7,1.4]])
print(predictions)