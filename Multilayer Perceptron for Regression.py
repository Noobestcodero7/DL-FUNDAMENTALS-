#Multilayer Perceptron for Regression
#import the libraries
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

#load dataset
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url,sep=r"\s+",skiprows=22, header=None )
data = np.hstack([raw_df.values[::2,:],raw_df.values[1::2,:2]])
target = raw_df.values[1::2,2].reshape(-1,1)

#Create X and y
X = pd.DataFrame(data)
y = target.ravel()

#Split data into training and test set
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42)

#Standardize the features
scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

#Initialize and fit the MLP regression model
mlp_rg = MLPRegressor(max_iter=500, random_state=42)
mlp_rg.fit(X_train,y_train)

#Make Prediction by MLP
y_pred_train = mlp_rg.predict(X_train)
y_pred_test = mlp_rg.predict(X_test)

#Print MLP performance
print("Multilayer Perceptron Performance")
print("---------------------------------")
print("Train R2:",f'{mlp_rg.score(X_train,y_train):.3f}')
print("Test R2:",f'{mlp_rg.score(X_test,y_test):.3f}')
print("---------------------------------")
print("Train MSE:",f'{mean_squared_error(y_train,y_pred_train):.3f}')
print("Test MSE:",f'{mean_squared_error(y_test,y_pred_test):.3f}')

