


def init(filename, header):
	fstring = ""
	for val in header:
		fstring = fstring + str(val) + ", "
	fstring = fstring[:-2] + "\n"
	f = open("Data/" + filename, 'w')
	f.write(fstring)
	f.close()

def write(filename, dArray):
	fstring = ""
	for val in dArray:
		fstring = fstring + str(val) + ', '
	fstring = fstring[:-2] + '\n'
	f = open("Data/" + filename, 'a')
	f.write(fstring)
	f.close()

def format(bigData):
	


def deconstruct(dString):

