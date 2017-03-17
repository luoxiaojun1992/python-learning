#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mlpy

iris = np.loadtxt('./semeion.data', delimiter=' ', dtype='str')
x, y = iris[:, :256].astype(np.float), iris[:, 257:-1].astype(np.int)

svm = mlpy.LibSvm()
svm.learn(np.array(x), np.array(y))
print svm.pred(x[0])
print svm.pred(x[len(x) - 1])
