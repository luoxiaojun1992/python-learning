#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mlpy

iris = np.loadtxt('./iris.data', delimiter=',')
x, y = iris[:, :4], iris[:, 4].astype(np.int)

svm = mlpy.LibSvm()
svm.learn(np.array(x), np.array(y))
print svm.pred(x[0])
print svm.pred(x[len(x) - 1])
