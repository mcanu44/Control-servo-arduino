# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:15:18 2016

@author: olinero
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.show()
