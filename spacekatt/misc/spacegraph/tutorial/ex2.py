import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import numpy as np
import pylab

plt.plot([1,2,3,4], [1,4,9,16], '-b')
plt.axis([0, 6, 0, 20])
plt.savefig('pic2.png')
