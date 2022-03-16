# This file is to pre-process the origional data set
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

np.set_printoptions(threshold=np.inf)

# Read the data from the CSV file
train_1 = pd.read_csv("day.csv")
train = pd.read_csv("day.csv")
train=train.drop(['dteday','hum','windspeed','casual','registered'],axis=1)
print(train.head())
#print("train : " + str(train.shape))

# For categorical features, observe the value range and histogram
categorical_features = ['season', 'mnth', 'weathersit', 'weekday']


# Convert the data type to object for easy handling by get_dummies
for col in categorical_features:
    train[col] = train[col].astype('object')

# convert data into one_hot form
X_train_cat = train[categorical_features]
X_train_cat = pd.get_dummies(X_train_cat)
print('The result of one_hot')
print(X_train_cat)

mn_X = MinMaxScaler()
numerical_features = ['temp', 'atemp']
temp = mn_X.fit_transform(train[numerical_features])
X_train_num = pd.DataFrame(data=temp, columns=numerical_features, index=train.index)
print('Result of Data normalization processing ')
print(X_train_num.head())

# Concat the related data column 
X_train = pd.concat([X_train_cat, X_train_num, train['holiday'], train['workingday']], axis=1, ignore_index=False)
print('X_train.head(): ')
print(X_train.head())

# Concat the data
FE_train = pd.concat([train['instant'], X_train, train['yr'], train['cnt']], axis=1)
FE_train = FE_train.drop('instant',axis=1)

# Save file 
FE_train.to_csv('FE_day.csv', index=False)  


print('FE_train.head():')
print(FE_train.head())
print(FE_train.info())
trainset = FE_train[:585]
testset=FE_train[585:]
print(trainset)
print(testset)

