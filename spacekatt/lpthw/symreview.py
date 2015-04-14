from __future__ import division

#print True and False, ', oh so false\n'

class firetoy:

	wick = 'Kevlar'
	artform = 'Flow'
	tricks = []
	disc = []

	def __init__(self, name):
		self.type = name
		print 'Intint', name

	def add_dscrpt(self, what):
		self.disc.append(what)
		return self.disc

	def add_trick(self, trick):
		self.tricks.append(trick)
		print self.tricks

	def full(self):
		print "Type of firetoy: ", self.type
		print "Tricks known: ", self.tricks
		print "Description: ", self.disc
		return 'Not none\n'

#d = firetoy('Staff')
#e = 'Dart'
#f = 'dart attached to a rope of varying length'
#d.add_dscrpt('rod of varying length moved around the body')
#d.add_trick('smack-yourself-in-face')

#print firetoy('Staff').wick, d.disc, '\n'

#print d.full()

class something:

	def __init__(self):
		print 'Initializing...'
		#If return, TypeError: __init__() should return None

	def __enter__(self):
		print 'Entering...'
		return 'Something'

	def __exit__(self, type, value, traceback):
		print 'Exiting...'
		return "Nothing"

#with something() as nothing:
#	print nothing

class Cls:
	x =3
#inst = Cls()
#inst.x = inst.x + 1 #4
#inst2 = Cls()
#inst2.x = inst.x + 2 #6
#print inst2.x

def wittyname():
	#assert could test for variable types
	less7 = raw_input('Enter a digit less than 7: ')
	assert 0 < int(less7) < 7
	return 'Universal truth'

#wittyname()

def typetest():
	roar = raw_input('Enter an integer: ')
	assert int(roar)
	return 'Local truth'

#typetest()

def breaks():
	well = 10
	while well > 0:
		print "Current: ", well
		well -= 1
		if well in range(3, 8):
#			break
			continue
		print 'Future!'
	for a in range(7):
		print 'Old: ', a
		if a == 3:
			break
	
#breaks()

def deldict():
	dict = {'banana': 'Yellow', 'orange': 'orange', 'pen': 15.00}
	#The sig.figs. on 15.00 is cut to 15.0, look up formatting later
	print  dict['banana']
	a = dict['pen']
	del dict['banana']
	print str(dict)
	del dict
	print a, 'This appears after del, must be a seperate variable'
	bonkers = 10
	while True:
		try:
			len(dict) > 0
		except UnboundLocalError:
			print 'Deleted!'
			break
		print 'It survived!'
		bonkers -= 1
		if bonkers == 3:
			return False #Stops while loop after 7 iterations

#deldict()

def fib(par, ter):
	#print par
	b = par - par
	term = [b, par]
	for a in range(ter):
		term.append(par)
		par =+ term[len(term) - 2] + term[len(term) - 1]
		#print par
	term.append(par)
	return term
		


#print fib(1, 1000)

def fibber(x):
	a = fib(1, 13)
	if x in a:
		print 'Illuminati confirmed'
	elif (x + 1) in a:
		print 'Illuminati suspected'
	else:
		print 'Conspiracy theories are myths'

#for b in range(5, 8):
#	fibber(b)

def divzero():
	try:
		return 1 / 0
	except ZeroDivisionError:
		return 'This fails.'

#print divzero()

#exec('print("Hmmm...")')

def rascalsong(x):
	try:
		int(x)
		assert x > 2
	except ValueError:
		print "This isn't a number."
	except AssertionError:
		print 'Nice try.'
	else:
		print 'When is this triggered?'
	finally:
		print 'Is this always triggered?'

#for a in (2, 4, 'Failure'):
#	rascalsong(a)

#print 9/4

x = 27

def globalexample():
	#x defined with-in function is said to be a 'shadow' of the
	#global variable, purely local
	#global statement imports global variable locally 
	global x
	print 'Non-local:', x
	x += 1
	return 'end function'

#print globalexample()
#print 'Global x value:', x
