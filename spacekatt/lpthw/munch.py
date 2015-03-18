numbe = [2, 3, 7]
munch = False
print """\nIf you had to choose a number to describe your lunch...

	What would it be?
"""

while munch == False:
	lunch = []
	try:
		n = int(raw_input("---> "))
	except ValueError:
		n = False
	if n != False:
		print "\nTime to cook!"
		nlist = str(n)
		for a in nlist:
			lunch.append(int(a))
		print "We made: ", lunch
		print "We want to eat: ", numbe
	else:
		print "\nThis isn't an integer... Retry"
	if len(set(numbe) & set(lunch)) > 0:
		munch = True
		print "\nToday's menu: ", list(set(numbe) & set(lunch))
		print "\nNomnomnom... yumz!"
	else:
		print "\nYour lunch cannot be munched"
		print "Pick a new lunch\n"
	
#change so duplicate numbers aren't cut
