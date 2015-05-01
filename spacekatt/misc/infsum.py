from __future__ import  division
from math import *
from sympy import *

x = symbols('x')

def ndiff(fx, n):
	terms = [fx]
	if n != 0:
		for z in range(n):
			fx = diff(fx, x)
			terms.append(fx)
		return terms
	else:
		return terms

gblogs = {'x': 0}

def whaha(fx, n):
	for z in range(n):
		macl = eval('ndiff(fx, n)', gblogs)
		return macl


def funn():
	return 2


m = funn()

eq = x ** 4
print ndiff(eq, 4)
#print whaha(sin(x), 2)
