#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import neurolab as nl

input = []
target = []

iris_data_file = open("./iris.data")

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
net = nl.net.newff([[0, 8], [0, 5], [0, 7], [0, 3]], [100, 1])
#Training Network
err = net.train(input, target, show=1, goal=0.0001, epochs=10000)
#Testing Network
print 'Prediction result: ', net.sim([['4.9', '3.0', '1.4', '0.2']])
#Print Error Line
plt.plot(err)
plt.show()

