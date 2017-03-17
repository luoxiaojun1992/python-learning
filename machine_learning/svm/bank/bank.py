#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mlpy
import sklearn.preprocessing

iris = np.loadtxt('./bank-full.csv', delimiter=';', skiprows=1, dtype=np.str)
x, y = iris[:, :16], iris[:, 16]

le = sklearn.preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

x_data = []
for item in x:
    le.fit(item)
    item = le.transform(item)
    x_data.append(item)

svm = mlpy.LibSvm()
svm.learn(np.array(x_data), np.array(y))
print svm.pred(x_data[0])
print svm.pred(x_data[len(x_data) - 1])
print svm.pred(x_data[len(x_data) - 3])
print svm.pred(x_data[len(x_data) - 10])
