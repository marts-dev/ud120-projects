#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
data_dict.pop("TOTAL")
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below

# plot data
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter(salary, bonus, color="blue")

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()

#target, features = targetFeatureSplit(data)

# Split data set
#salary_train, salary_test, bonus_train, bonus_test = train_test_split(features, options)


