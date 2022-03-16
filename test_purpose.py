import bike_data
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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

#Get the correlation coefficient to determine which factors have high correlation and which factors have low correlation
# correlation = bike_data.train_1.corr()
# mask = np.array(correlation)
# mask[np.tril_indices_from(mask)] = False
# fig,ax = plt.subplots()
# fig.set_size_inches(20,10)
# sns.heatmap(correlation,mask=mask,vmax=0.8,square=True,annot=True)
# plt.show()
