import matplotlib.pyplot as pt
import pandas as pd
train=pd.read_csv("day.csv")
pt.scatter(train["holiday"],train["cnt"])
pt.show()
