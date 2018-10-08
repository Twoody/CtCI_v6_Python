'''
for n>0 and n<1000, solve all instances of: 
	a^3 + b^3 = c^3 + d^3
	a**3 + b**3 = c**3 + d**3

Brute force would look like for i, for j, for k, for l... which would
	run as 1000**4 iterations about.
	NOT OPTIMAL

A better solution is to make a set of all of the cubed numbers first.
'''

def getcubes(n=0):
	mList = []
	for i in range(0,n):
		iCubed = i**3
		mList.append(iCubed)
	return mList

def equation(a,b,c,d):
	if (a+b-c-d == 0):
		return True
	else:
		return False

def brute1(intSetMax=0, intSetMin=0):
	cubes = getcubes(intSetMax)
	successes = []
	for i in range(intSetMin, len(cubes)):
		a = cubes[i]
		for j in range(i+1, len(cubes)):
			b = cubes[j]
			for k in range(j+1, len(cubes)):
				c = cubes[k]
				for l in range(k+1, len(cubes)):
					d = cubes[l]
					if(equation(a,b,c,d) == True):
						successes.append([a,b,c,d])
	return successes

def getCDList():
	'''mdic key is based off of sum of mdic value pairs'''
	mdic = {}
	for i in range(1,1000):
		c = i**3
		for j in range(1,1000):
			d = j**3
			mdic[str(c+d)] = (c,d)
	return mdic


def brute2(resDic):
	# d = a**3 + b**3 - c**3
	successes = []
	for i in range(1, 1000):
		a = i**3
		for j in range(1, 1000):
			b = j**3
			if (resDic[str(a+b)]):
				CDpair = resDic[str(a+b)]
				c = CDpair[0]
				d = CDpair[1]
				successes.append([a,b,c,d])
	return successes

def main():
	intSetMax = 100
	#cubes = getcubes(intSetMax)

	#x = brute1(intSetMax)
	#for j in x:
	#	print(j)

	mdic  = getCDList()
	mList = brute2(mdic)
	for arr in mList:
		print(arr)

if __name__ == "__main__":
	main()
