import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

iris_data=pd.read_csv('iris.csv')

X = iris_data.drop(columns=['variety'])
y = iris_data['variety']

X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

scaler = StandardScaler()
X_train_scaled= scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()

model.fit(X_train_scaled,y_train)

#Evaluate model on testing set
y_pred = model.predict(X_test_scaled)
accuracy= accuracy_score(y_test, y_pred)
print("Accuracy:",accuracy)

new_data = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [6.3, 2.6, 5.7, 1.9]
])
new_data_scaled = scaler.transform(new_data)
predictions= model.predict(new_data_scaled)
print(predictions)

