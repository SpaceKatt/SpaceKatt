from sys import exit

def dead(why):
	print "\n", why, "you failed!"
	exit(0)

def intro(start):
	if start == 0:
		print "Welcome!"
	else:
		print "%sWelcome back..." % "\n"
	print "\n", "You are trapped inside this computer."
	print """Nothing before...

	...has ever...
			...escaped."""
	print 'The only option is to go forward.\n'
	action = raw_input("What do you do? ")
	list = ["go forward", "kill self"]
	if "forward" in action:
		antechamber()
	elif "kill" in action or "self" in action:
		dead('Because of your penchant for auto-darwinism,')
	else:
		what(list, intro)
	
def what(options, room, *args):
	if len(args) == 0:
		print "\nI have no idea what you meant, try: \n"
	else:
		print "I have no idea what you meant, next time try: \n"
	a = 0
	for o in options:
		a += 1
		print "%i: %s" % (a, o) 
	if room == intro or room == final:
		room(1)
	else:
		room()

def antechamber():
	opt1 = ['look around', 'give up']
	opt = ['north', 'south']
	print "\nThis hallway seems to be going on forever...\n"
	action = raw_input('What next? ')
	if 'look' in action:
		print '\nYou see people flying around.'
		print 'Wings begin to sprout on your back.'
		print 'Do you fly north or south for the winter?\n'
		dir = raw_input("---> ")
		if "north" in dir:
			tundra()
		elif 'south' in dir:
			skyway()
		else:
			print "\nYou start yelling in confusion and land..."
			print "Also,", what(opt, antechamber, 1)
	elif action == 'give' or action == 'up' or action == 'give up':
		dead("Your lack of motivation is disturbing,")
	else:
		what(opt1, antechamber)

def tundra():
	print "\nYou have chosen to fly into the tundra during winter..."
	dead("You freeze to death,")

def skyway():
	print "\nHmmm..."
	print "You are confused as to how you're flying inside a computer."
	a = raw_input("\nDo you continue flying? (y/n) --> ")
	if "y" in a or "Y" in a:
		b = "As you begin to ascend to the heavens,\n"
		c = '	you fly too close to the sun.\n'
		d = 'The wax on your wings melts off,\n'
		e = '	and you begin to fall,'
		f = b + c + d + e
		dead(f)
	elif "n" in a or 'N' in a:
		final(0)		
	else:
		hmm = ['n -or- N', 'y -or- Y']
		what(hmm, skyway)

def judgement(a, b):
	z = str(a)
	n = str(b)
	c = list(set(z) & set(n))
	return len(c)

def final(x):
	if x == 0:
		print """\nYou land safely. Without the need for another step,
	a guru steps out of his shack and gives you a strange offer:"""
		guru_happy = False
	elif x != "not winning" and x != 0:
		guru_happy = True
		print "\nYou are wise beyond your words..."	
	else:
		print "\nYoung one, this is no joke... Do you know what a number is?"
		guru_happy = False
	numbe = [2, 3, 5, 6]
	while guru_happy == False:
		print "\nTell me your favorite number so I can judge your soul."
		try:
			a = int(raw_input("\n->>->> "))
		except ValueError:
			final("not winning")
		lista = judgement(a, numbe)
		if lista > 0:
			final(a)
		else:
			print "\nThink long and hard about what you soul means to you..."
	win(x)

def win(a):
	print "\nWinning text"
	print "Your score: %d" % (a%4)
	exit(0)

intro(0)
