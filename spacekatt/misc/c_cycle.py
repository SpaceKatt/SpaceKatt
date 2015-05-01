from __future__ import division
from math import sin, cos, pi

def cycloid(bar, i):
	x = bar * (i - sin(i))
	y = bar * (1 - cos(i))
	return y

for f in range(4):
	for a in range(1, 65):
		r = cycloid(4/2, a/(pi * 8))
		print 'Note start: %f' % (r + f * 4)
