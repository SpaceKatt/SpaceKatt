from __future__ import division

droph = [(1, 5.47-2.21), (5, 4.17-2.05), (1, 5.75-11.47),
		(15, 4.26-11.68), (35, 5.05 - 2.96), (15, 5.14 -11.50),
		(2, 2.42), (1, 4.43 - 9.45), (10, 9.36 - 0.87), (15, 9.29 - 12.08)]

def mals(drops, pH):
	drpmL = 1 /20
	mL_L = 1 / 1000
	L = drops * drpmL * mL_L
	moles = L * 6
	return moles

def process_data(list):
	data = []
	for n in range(0, len(list)):
		thing = '{0}: {1:2.1e} moles, delta-pH = {c:2.3}'
		x = list[n][1]
		z = thing.format(int(n+1), mals(*list[n]), c=x)
		data.append(z)
	return data

#print process_data(droph)

def specify(list, which):
	specific = []
	m = process_data(list)
	for n in which:
		specific.append(m[n - 1])
	return specific

def printl(list, ra):
	listb = specify(list, ra)
	for n in range(0, len(listb)):
		print listb[n]

def num(a, b):
	return range(a, b+1)

#print specify(process_data(droph), range(7, 9)) 

printl(droph, num(7, 8))
