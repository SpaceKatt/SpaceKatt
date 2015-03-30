print True and False, ', oh so false\n'

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

d = firetoy('Staff')
e = 'Dart'
f = 'dart attached to a rope of varying length'
d.add_dscrpt('rod of varying length moved around the body')
d.add_trick('smack-yourself-in-face')

print firetoy('Staff').wick, d.disc, '\n'

print d.full()

class something:

	def __init__(self):
		print 'Initializing...'

	def __enter__(self):
		print 'Entering...'

	def __exit__(self, type, value, traceback):
		print 'Exiting...'
		return "Nothing"

with something() as nothing:
	print nothing
