from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
x.append([0,0,1])
x.append([0,0,-1])

for i in range(1,4):
    for j in range(0,8):
        x.append([np.sin(i*np.pi/4)*np.cos(j*np.pi/4),np.sin(i*np.pi/4)*np.sin(j*np.pi/4),np.cos(i*np.pi/4)])

xs = 10*np.array(x)

ax.scatter(xs[:,0],xs[:,1],xs[:,2])
plt.show()
