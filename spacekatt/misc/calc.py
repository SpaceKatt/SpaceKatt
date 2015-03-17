from __future__ import division
from math import *
from sympy import Rational

def y(t):
	a = (-1) * (e ** t) * (t ** 2 - 3 * t + 3)
	return a

print e
print y(0)
b = y(0) - y(1)
print b, "\n"
print 3 - e
