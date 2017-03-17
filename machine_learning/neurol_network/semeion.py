#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import neurolab as nl
import os

iris = np.loadtxt('./semeion.data', delimiter=' ', dtype='str')
x, y = iris[:, :256].astype(np.float), iris[:, 256:-1].astype(np.int)

#Input Sample
input = np.array(x)
#Output Sample
target = np.array(y)

#Building Network
if os.path.exists('./semeion.net'):
    net = nl.load('./semeion.net')
else:
    net = nl.net.newff([[0, 1]]*256, [10, 10])

##Training Network
err = net.train(input, target, show=1, epochs=1000)

net.save('./semeion.net')

#Testing Network
print 'Prediction result: ', net.sim([x[0]])
#Print Error Line
plt.plot(err)
plt.show()

