#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mlpy
import sklearn.preprocessing

iris = np.loadtxt('./heart-disease.data', delimiter=',', dtype='str')
x, y = iris[:, :13], iris[:, 13].astype(np.int)

le = sklearn.preprocessing.LabelEncoder()

x_data = []
for item in x:
   le.fit(item)
   new_item = le.transform(item)
   x_data.append(new_item)

svm = mlpy.LibSvm()
svm.learn(np.array(x_data), np.array(y))
print svm.pred(x_data[len(x_data) - 3])
