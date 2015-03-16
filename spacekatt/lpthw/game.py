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
	
def what(options, room):
	print "\nI have no idea what you mean, try: \n"
	a = 0
	for o in options:
		a += 1
		print "%i: %s" % (a, o) 
	if room == intro:
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
			what(opt, antechamber)
	elif action == 'give' or action == 'up' or action == 'give up':
		dead("Your lack of motivation is disturbing,")
	else:
		what(opt1, antechamber)

def tundra():
	print "\nYou have chosen to fly into the tundra during winter..."
	dead("You freeze to death,")

def skyway():
	print "\nHmmm..."
	print "You are confused as to how you're flying in a computer."

intro(0)
