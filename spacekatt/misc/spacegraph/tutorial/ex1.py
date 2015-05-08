import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import numpy as np
import pylab

#from time 0 to time 5, 0.2 increments
t = np.arange(0., 5., 0.2)

#red dashed, blue squares, green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.savefig('pic1.png')
