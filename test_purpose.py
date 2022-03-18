import bike_data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import bike_data
import main
sns.set()
#Used to test the relationship between each factor and the target value, draw a scatter plot
# plt.scatter(bike_data.train_1["dteday"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["weathersit"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["weekday"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["holiday"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["hum"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["season"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["yr"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["mnth"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["workingday"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["temp"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["atemp"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["windspeed"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["casual"],bike_data.train_1["cnt"])
# plt.scatter(bike_data.train_1["registered"],bike_data.train_1["cnt"])

# Obtain the correlation coefficient to determine which factors have high correlation and which factors have low correlation
correlation = bike_data.train_1.corr()
find_co = np.array(correlation)
find_co[np.tril_indices_from(find_co)] = False
fig,ax = plt.subplots()
fig.set_size_inches(20,10)
sns.heatmap(correlation,mask=find_co,vmax=0.8,square=True,annot=True)
plt.show()

#Create a data to predict future,Convert manually to one-hot format
forfun=pd.DataFrame({"dteday":['3-17-2022','3-18-2022','3-19-2022','3-20-2022','3-21-2022','3-22-2022','3-23-2022'],
                     "season_1":[1,1,1,1,0,0,0],
                     "season_2":[0,0,0,0,1,1,1],
                     "season_3":[0,0,0,0,0,0,0],
                     "season_4":[0,0,0,0,0,0,0],
                     "mnth_1":[0,0,0,0,0,0,0],
                     "mnth_2":[0,0,0,0,0,0,0],
                     "mnth_3":[1,1,1,1,1,1,1],
                     "mnth_4":[0,0,0,0,0,0,0],
                     "mnth_5":[0,0,0,0,0,0,0],
                     "mnth_6":[0,0,0,0,0,0,0],
                     "mnth_7":[0,0,0,0,0,0,0],
                     "mnth_8":[0,0,0,0,0,0,0],
                     "mnth_9":[0,0,0,0,0,0,0],
                     "mnth_10":[0,0,0,0,0,0,0],
                     "mnth_11":[0,0,0,0,0,0,0],
                     "mnth_12":[0,0,0,0,0,0,0],
                     "weathersit_1":[0,0,0,0,0,1,1],
                     "weathersit_2":[0,1,0,0,0,0,0],
                     "weathersit_3":[1,0,1,1,1,0,0],
                     "weekday_0":[0,0,0,1,0,0,0],
                     "weekday_1":[0,0,0,0,1,0,0],
                     "weekday_2":[0,0,0,0,0,1,0],
                     "weekday_3":[0,0,0,0,0,0,1],
                     "weekday_4":[1,0,0,0,0,0,0],
                     "weekday_5":[0,1,0,0,0,0,0],
                     "weekday_6":[0,0,1,0,0,0,0],
                     "temp": [0.38, 0.38, 0.32, 0.29, 0.34, 0.46, 0.47],
                     "atemp": [0.39, 0.39, 0.35, 0.34, 0.37, 0.45, 0.45],
                     "holiday":[0,0,0,0,0,0,0],
                     "workingday":[1,1,0,0,1,1,1],
                     "yr":[11,11,11,11,11,11,11]})
print(forfun.head())
forfun_prediction=forfun.drop(['dteday'],axis=1)
print(forfun_prediction.head())
result=main.lr.predict(forfun_prediction)
print(result)
x=result[0]
result=np.array(result)
result=result.tolist()
for i in result:
    if i<x:
        x=i
index=result.index(min(result))
print("The most suitable day for travel is:",forfun['dteday'][index])
