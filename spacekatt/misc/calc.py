from __future__ import division
from math import *
from sympy import Rational


def y(a):
	b = 0
	for i in range(1, 8 + 1):
		s = i / (1 + sqrt(i))
		b += s
		print b

y(5000)
