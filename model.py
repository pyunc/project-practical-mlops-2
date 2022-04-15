# Simple Linear Regression

'''
This model predicts the salary of the employ based on experience using simple linear regression model.
'''

import json
import logging
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)



logging.info('Data loading, preprocessing and splitting')

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


logging.info('Model training')
# Fitting Simple Linear Regression to the Training set

## linear model

regressor = LinearRegression()

## random forest model
#from sklearn.ensemble import RandomForestRegressor
#regressor = RandomForestRegressor(n_estimators=20, random_state=0)

regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

logging.info('Model error evaluation')

print(mean_squared_error(y_pred, y_test))

logging.info('Model dumping')

# Saving model using pickle
pickle.dump(regressor, open('model.pkl','wb'))

logging.info('Model quick evaluation')

# Loading model to compare the results
model = pickle.load( open('model.pkl','rb'))
print(model.predict([[1.8]]))
