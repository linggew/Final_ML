import pandas as pd


# read the dataset
train_1 = pd.read_csv("day.csv")

#delete the attributes with have low correlation
train = train_1.drop(['dteday','hum','windspeed','casual','registered'],axis=1)
print(train.head())
print("train : " + str(train.shape))

#The feature should do one-hot transfer since the limitation value range of them
feature = ['season', 'mnth', 'weathersit', 'weekday']
for col in feature:
    # transfor the data type to object which can be handled by get_dummies
    train[col] = train[col].astype('object')
train_feature = train[feature]
train_feature = pd.get_dummies(train_feature)
print('the result of one-hot')
print(train_feature)

# combine data
X_train = pd.concat([train_feature, train['temp'],train['atemp'], train['holiday'], train['workingday']], axis=1, ignore_index=False)
print('X_train.head(): ')
print(X_train.head())
final_train = pd.concat([train['instant'], X_train, train['yr'],train['cnt']], axis=1)
final_train = final_train.drop('instant',axis=1)

# final_train.to_csv('fianl.csv', index=False)  # creat final dataset file
print('final_train.head():')
print(final_train.head())
print(final_train.info())

#separate the train and test set 8:2
trainset = final_train[:585]
testset=final_train[585:]
print(trainset)
print(testset)

