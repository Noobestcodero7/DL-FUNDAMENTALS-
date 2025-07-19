#Multilayer perceptron for classification
#import libraries
# import libraries
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


#load the dataset
from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()

#Create X and Y
X=pd.DataFrame(breast_cancer.data)
y=breast_cancer.target

#Split the data into training and test set
X_train,X_test,y_train,y_test=train_test_split(breast_cancer.data,breast_cancer.target)

#Standardize the features
scaler =StandardScaler()
scaler.fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

#Initiate and fit the model
mlp_clf = MLPClassifier(max_iter=1000)
mlp_clf.fit(X_train,y_train)

#Show accuracy score
print("Training Accuracy",mlp_clf.score(X_train,y_train))
print("Test Accuracy",mlp_clf.score(X_test,y_test))
