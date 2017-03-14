#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mlpy
import sklearn.preprocessing

iris = np.loadtxt('./heart-disease.data', delimiter=',', dtype='str')
x, y = iris[:, :13], iris[:, 13].astype(np.int)

x_data = []
for item in x:
    

svm = mlpy.LibSvm()
svm.learn(np.array(x_data), np.array(y))
print svm.pred(x_data[0])
print svm.pred(x_data[len(x_data) - 1])
print svm.pred(x_data[len(x_data) - 3])
print svm.pred(x_data[len(x_data) - 10])
