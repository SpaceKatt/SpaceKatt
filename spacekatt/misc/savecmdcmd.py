from sys import argv

script, fileIO, cmd = argv

"""This bit-let stores commands I find neeto.

To use this lil'tidder to save instructions on how to use this lil'tidder:
    >python sav* cmd* 'python sav* cmd* ["cmd"]'

If the use wants a list of neeto commands:
    Use list in place of ["cmd"]
"""

sfile = str(fileIO)

cmdlist = []

with open(sfile, 'r') as o:
    for line in o:
        if line == '\n':
	    break
	else:
            result = line.strip()
            result = result[1:-1]
            cmdlist.append(result)

def read_file(file):
    with open(str(file), 'r') as r: 
	print r.read()

def saviour(cmd):
    cmdlist.append(cmd)
    with open(sfile, 'w') as z:
        z.truncate()
        for m in range(len(cmdlist)):
	    z.write("'{0}'{1}".format(str(cmdlist[m]), '\n'))
    read_file(fileIO)		

if cmd == 'list':
    for r in range(len(cmdlist)):
	print cmdlist[r]
elif cmd in cmdlist:
    print '\n', 'ERROR: Command already exists :3'
else:
    saviour(cmd)
