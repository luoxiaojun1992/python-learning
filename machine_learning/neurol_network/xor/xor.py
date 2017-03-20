#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import neurolab as nl
import sys

input = []
target = []

iris_data_file = open('./xor.data')

while True:
    lines = iris_data_file.readlines(100000)
    if not lines:
        break
    for line in lines:
        line = line.replace('\n', '')
        if line != '':
            line_data = line.split(',')
            data_len = len(line_data)
            target.append([line_data[data_len - 1]])
            del(line_data[data_len - 1])
            input.append(line_data)

iris_data_file.close()

#Input Sample
input = np.array(input)
#Output Sample
target = np.array(target)
#Building Network
net = nl.net.newff([[0, 1]]*2, [5, 1])
#Training Network
err = net.train(input, target, show=1, goal=0.000000001)
#Testing Network
print 'Prediction result: ', net.sim([[1,1], [1,0], [0,1], [0,0]])
#Print Error Line
plt.plot(err)
plt.show()

