#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import neurolab as nl

input = []
target = []

wine_data_file = open("./wine.data")

while True:
    lines = wine_data_file.readlines(100000)
    if not lines:
        break
    for line in lines:
        line = line.replace('\n', '')
        if line != '':
            line_data = line.split(',')
            data_len = len(line_data)
            target.append([(float)(line_data[data_len - 1])])
            del(line_data[data_len - 1])
            processed_line_data = []
            for item in line_data:
                processed_line_data.append((float)(item))
            input.append(processed_line_data)

wine_data_file.close()

print input,target

#Input Sample
input = np.array(input)
#Output Sample
target = np.array(target)
#Building Network
net = nl.net.newff([[0, 170]] * 13, [5, 1])
#Training Network
err = net.train(input, target, show=1, goal=0.0001)
#Testing Network
print 'Prediction result: ', net.sim([[2,12,.92,2,19,86,2.42,2.26,.3,1.43,2.5,1.38,3.12]])
#Print Error Line
plt.plot(err)
plt.show()

