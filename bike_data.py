import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.inf)

# 读入数据
train = pd.read_csv("day.csv")
train=train.drop(['dteday','hum','windspeed','casual','registered'],axis=1)
print(train.head())
#print("train : " + str(train.shape))
    # 对类别型特征，观察其取值范围及直方图
categorical_features = ['season', 'mnth', 'weathersit', 'weekday']

    # 数据类型变为object，才能被get_dummies处理
for col in categorical_features:
    train[col] = train[col].astype('object')

X_train_cat = train[categorical_features]
X_train_cat = pd.get_dummies(X_train_cat)
print('独热编码结果')
print(X_train_cat)

from sklearn.preprocessing import MinMaxScaler
mn_X = MinMaxScaler()
numerical_features = ['temp', 'atemp']
temp = mn_X.fit_transform(train[numerical_features])
X_train_num = pd.DataFrame(data=temp, columns=numerical_features, index=train.index)
print('数据归一化处理结果')
print(X_train_num.head())
# 合并数据
X_train = pd.concat([X_train_cat, X_train_num, train['holiday'], train['workingday']], axis=1, ignore_index=False)
print('X_train.head(): ')
print(X_train.head())

    # 合并数据
FE_train = pd.concat([train['instant'], X_train, train['yr'], train['cnt']], axis=1)
FE_train = FE_train.drop('instant',axis=1)
FE_train.to_csv('FE_day.csv', index=False)  # 保存数据
print('FE_train.head():')
print(FE_train.head())
print(FE_train.info())
trainset = FE_train[:585]
testset=FE_train[585:]
print(trainset)
print(testset)

