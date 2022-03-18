import numpy as np
from sklearn.linear_model import LinearRegression
import bike_data

#print(bike_data.trainset)
train_x = bike_data.trainset.drop(['cnt'],axis=1)

# print(train_x)
train_y = bike_data.trainset['cnt']
# print(train_y.head())

# built training model
lr=LinearRegression()
test=lr.fit(train_x,train_y)
# Another way we choose to use Least Squares instead of LinearRegression package
# alog_temp=train_x.T.dot(train_x)
# alog_temp=np.array(alog_temp)
# alog_temp=alog_temp.astype(float)
# alog=np.linalg.inv(alog_temp).dot(train_x.T).dot(train_y)

test_x = bike_data.testset.drop(['cnt'],axis=1)
#print(test_x.head())
print(bike_data.testset)
test_y = bike_data.testset['cnt']
print(test_y)
test_y=test_y.values.tolist()


#test the testset with model
result=lr.predict(test_x)
# match with the Least Squares to calculate the prediction Y
# result=test_x.dot(alog)
# result=result.values.tolist()
result_arr=np.array(result)
print(result)
# print(result_arr[0])
# print(test_y)
# print(test_y[0])
temp=test_y[0]-result_arr[0]
# print(temp)

#calculate the accuracy
add=0
ad=0
for row in range(146):
    ad=ad+1

    if ((1-(np.abs(test_y[row]-result_arr[row])/test_y[row]))>0.8):
        add=add+1
accuary=add/ad
print("the accuary is:",accuary)
