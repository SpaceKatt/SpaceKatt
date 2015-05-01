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
	for n in range(0, len(list)):
		thing = '{0}: {1:2.2e} moles,'
		z = thing.format(int(n+1), mals(*list[n]))
		x = list[n][1]
		print z, 'pH = %.2f' % x

process_data(droph)
