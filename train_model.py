import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn import datasets
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import joblib

#Load the dataset
house_df = pd.read_csv("Housing.csv")
house_df['renovated'] = (house_df['yr_renovated'] > 0).astype(int)

#Set y to be the target column (price)
y = house_df['price']

#Pick columns that will be the predictors (view, condition, and grade will be sliders)
predictors = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'yr_built', 'lat', 'long', 'sqft_basement', 'waterfront', 'renovated', 'view', 'condition', 'grade']
X = house_df[predictors]

#Set a random state and split the data (80-20) into train and test sets
random = 50
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state =random, test_size=0.2)

#Train the regression model and fit it with the training sets
regr_house = linear_model.LinearRegression()
regr_house.fit(X_train, y_train)

y_pred = regr_house.predict(X_test)
print(mean_absolute_error(y_test, y_pred))
print(r2_score(y_test, y_pred))

mae_percent = mean_absolute_error(y_test, y_pred) / y.mean() * 100
print(mae_percent)

joblib.dump(regr_house, "house_price_model.pkl")
joblib.dump(predictors, "predictors.pkl")