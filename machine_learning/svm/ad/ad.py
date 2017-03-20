#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mlpy
import sklearn.preprocessing
import pickle
import os

iris = np.loadtxt('./ad.data', delimiter=',', dtype='str')
x, y = iris[:, :1558], iris[:, 1558]

le = sklearn.preprocessing.LabelEncoder()

x_data = []
for item in x:
   le.fit(item)
   new_item = le.transform(item)
   x_data.append(new_item)

le.fit(y)
y = le.transform(y)

if os.path.exists('./ad.mdl'):
  svm_file = open('./ad.mdl')
  svm = pickle.load(svm_file)
  svm_file.close()
else:
  svm = mlpy.LibSvm()

svm.learn(np.array(x_data), np.array(y))

svm_file = open('./ad.mdl', 'wb')
pickle.dump(svm, svm_file, -1)
svm_file.close()

print svm.pred(x_data[len(x_data) - 1])
print svm.pred(x_data[0])
