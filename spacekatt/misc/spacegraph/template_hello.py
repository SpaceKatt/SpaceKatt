from sys import argv

script, output = argv

a = 'import matplotlib as mpl\n'
b = "mpl.use('agg')\n"
c = 'import matplotlib.pyplot as plt\n'
d = 'from mpl_toolkits.mplot3d import Axes3D\n'
f = 'import numpy as np\n'
e = 'from itertools import product, combinations\n'
g = 'import pylab\n'

list = []

for n in (a, b, c, d, e, f, g):
	list.append(n)

with open(output, 'w') as h:
	for n in list:
		h.write(n)
