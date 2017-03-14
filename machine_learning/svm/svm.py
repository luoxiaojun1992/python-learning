#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mlpy

x = [[1, 8], [3, 20], [1, 15], [3, 35], [5, 35], [4, 40], [7, 80], [6, 49]]
y = [1, 1, 0, 0, 1, 0, 0, 1]
svm = mlpy.LibSvm()
svm.learn(np.array(x), np.array(y))
print svm.pred([1, 8])
