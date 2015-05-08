from __future__ import  division
from math import *
from sympy import *

x = symbols('x')

def factz(n):
	if n != 0:
		z = 1
		facts = [z]
		for m in range(1, n+1):
			z = z * m
			facts.append(z)
		return facts
	else:
		return 1

def ndiff(fx, n):
	terms = [fx]
	if n != 0:
		for z in range(n):
			fx = diff(fx, x)
			terms.append(fx)
		return terms
	else:
		return terms

#gblogs = {'x': 0}

#def whaha(fx, n):
#	for z in range(n):
#		macl = eval('ndiff(fx, n)', gblogs)
#		return macl


def funn():
	return 2

def evalu(fx, input):
	x = input
	a = eval(fx)
	return a

def taylorcn(eq, terms, a):
	cnof = []
	listfx = ndiff(eq, terms)
	factori = factz(terms)
	for z in range(0, len(listfx)):
		cn = evalu(str(listfx[z]), a)
		thing = '{0} / {1}'.format(cn, factori[z])
		cnof.append(thing)
	return cnof

def simplify(list):
	simple = []
	a = 0
	for n in range(0, len(list)):
		m = eval(list[n + a])
		if m == 0:
			list.pop(n + a)
			a -= 1
		if m != 0:
			continue
	return list

def xterm(terms, a):
	xtermz = []
	for i in range(0, terms):
		thing = '((x - {0}) ** {1})'.format(a, i)
		xtermz.append(thing)
	return xtermz

m = funn()

eq = x ** 4
print ndiff(eq, 4)

#print whaha(sin(x), 2)

ser = taylorcn(eq, 4, 1)
print simplify(ser)
print xterm(4, 1)
