from __future__ import division
import numpy as np

L = 100 #number of grid points in each dimension

Ng = 0

for i in range(L):
    for j in range(L):
        for k in range(L):
            if (i-L/2)**2+(j-L/2)**2+(k-L/2)**2 < (L/2)**2:
                Ng += 1
                print i,j,k
