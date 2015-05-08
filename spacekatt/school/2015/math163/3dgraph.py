import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import numpy as np
import pylab

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax2 = fig.gca(projection='3d')
ax.set_aspect("equal")

mpl.rcParams['legend.fontsize'] = 10

theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()

pylab.savefig('test1.png')
