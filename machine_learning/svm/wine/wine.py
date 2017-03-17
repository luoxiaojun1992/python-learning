#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mlpy

wine = np.loadtxt('./wine.data', delimiter=',')
x, y = wine[:, :13], wine[:, 13]

svm = mlpy.LibSvm()
svm.learn(np.array(x), np.array(y))
print svm.pred(x[0])
print svm.pred(x[len(x) - 1])
