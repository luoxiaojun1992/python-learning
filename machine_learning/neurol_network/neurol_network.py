#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import neurolab as nl

#Input Sample
input = np.array([[4, 11], [7, 340], [10, 95], [3, 29], [7, 43], [5, 128]])
#Output Sample
target = np.array([[1], [0], [1], [0], [1], [0]])
#Building Network
net = nl.net.newff([[3, 10], [11, 400]], [5, 1])
#Training Network
err = net.train(input, target, show=1, goal=0.000000001)
#Testing Network
print 'Prediction result: ', net.sim([[3, 10]])
#Print Error Line
plt.plot(err)
plt.show()

