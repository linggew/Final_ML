import bike_data
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()
#用来测试各个因素与目标值得关系，画出散点图
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

#求得相关系数，判别哪些因素相关性高，哪些因素相关性低
# correlation = bike_data.W.corr()
# mask = np.array(correlation)
# mask[np.tril_indices_from(mask)] = False
# fig,ax = plt.subplots()
# fig.set_size_inches(20,10)
# sns.heatmap(correlation,mask=mask,vmax=0.8,square=True,annot=True)
# plt.show()
