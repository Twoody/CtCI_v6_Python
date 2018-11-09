'''

'''
def sortByLowestNeighbor(akms):
	''' Need to visit corners and borders first '''
	''' Will INSERTION SORT by a custom `weight` of moves available neighbors '''
	''' '''
	for cur in akms:
		moves = akms[cur]
		nmoves = []
		for move in moves:
			weight = len(akms[move])
			if weight == 8 or nmoves == []:
				nmoves.append(move)
			else:
				lNmoves = len(nmoves)
				for j in range(0, lNmoves):
					nmove = nmoves[j]
					nweight = len(akms[nmove])
					if weight <= nweight:
						nmoves.insert(j, move)
						break
					elif j == lNmoves-1:
						nmoves.append(move)
		akms[cur] = nmoves
	return akms
def isLegalKM(b, x, y):
	if x < 0 or y < 0 :
		return False
	elif y >= len(b):
		return False
	elif x >= len(b[y]):
		return False
	elif b[y][x] == '':
		return False
	return True
def getAKMs(b):
	akms = {}
	for y in range(0, len(b)):
		for x in range(0, len(b[y])):
			xs1 = [x+1, x-1]
			ys1 = [y+2, y-2]
			xs2 = [x+2, x-2]
			ys2 = [y+1, y-1]
			akms[b[y][x]] = []
			for i in range(0, len(xs1)):
				for j in range(0, len(ys1)):
					if isLegalKM(b, xs1[i], ys1[j]) == True:
						akms[b[y][x]].append(b[ys1[j]][xs1[i]])
			for i in range(0, len(xs2)):
				for j in range(0, len(ys2)):
					if isLegalKM(b, xs2[i], ys2[j]) == True:
						if b[ys2[j]][xs2[i]] not in akms[ b[y][x] ]:
							akms[b[y][x]].append(b[ys2[j]][xs2[i]])
	akms = sortByLowestNeighbor(akms)
	return akms
def getLongestKnightsTour(b, startx, starty):
	start   = b[starty][startx]
	akm     = getAKMs(b)         #Get available knight moves
	s       = []                 #Stack
	l       = []                 #longest walk
	v       = {}                 #Visited
	ws      = {}                 #Walks
	ls      = 0                  #Size of longest walk
	cursize = 0                  #Keep track of size
	bs      = len(b) * len(b[0]) #Board size
	s.append(start)
	cursize += 1
	while s != []:
		curnode     = s[cursize-1]
		needspopped = True         #Needs popped if no new moves added;
		v[curnode]  = True
		for move in akm[curnode]:
			if move in v and v[move] == True:
				continue
			s.append(move)
			if str(s) in ws:
				s.pop(-1)
				continue
			needspopped = False
			cursize += 1
			ws[str(s)] = True
			break          #Found legal move; Only can make one move out of sequence
		if cursize == bs:
			return (s, cursize)
		if cursize > ls:
			l = s.copy()
			ls = cursize
		if needspopped == True:
			v[curnode] = False
			s.pop(-1)
			cursize -= 1
	return (l, ls)
def merge(tour):
	if len(tour) <=1:
		return tour
	midpoint = len(tour)//2
	lTour = tour[:midpoint]
	rTour = tour[midpoint:]
	return mergesort(merge(lTour), merge(rTour))

def mergesort(lTour, rTour):
	''' quick merge sort implementation to show we visited all nodes '''
	if len(lTour) == 0:
		return rTour
	elif len(rTour) == 0:
		return lTour
	iLeft     = 0
	iRight    = 0
	merged    = []
	targetLen = len(lTour) + len(rTour)
	while len(merged) < targetLen:
		if lTour[iLeft] <= rTour[iRight]:
			merged.append(lTour[iLeft])
			iLeft += 1
		else:
			merged.append(rTour[iRight])
			iRight += 1
		if iRight == len(rTour):
			merged += lTour[iLeft:]
			break
		elif iLeft == len(lTour):
			merged += rTour[iRight:]
			break
	return merged
if __name__ == "__main__":
	b = [
			[1, 2, 3, 4, 5, 6, 7, 8],
			[9,10,11,12,13,14,15,16],
			[17,18,19,20,21,22,23,24],
			[25,26,27,28,29,30,31,32],
			[33,34,35,36,37,38,39,40],
			[41,42,43,44,45,46,47,48],
			[49,50,51,52,53,54,55,56],
			[57,58,59,60,61,62,63,64]
	]
	#akms = getAKMs(b)
	#for spot in akms:
	#	print('\t' + str(spot) + ':\t' + str(akms[spot]))
	knightstour   = getLongestKnightsTour(b, 0, 0)
	proposedSeq   = knightstour[1]
	tour          = knightstour[0]
	print(proposedSeq)
	print(tour)
	print(merge(tour))
	print()
	knightstour   = getLongestKnightsTour(b, 0, 3)
	proposedSeq   = knightstour[1]
	tour          = knightstour[0]
	print(proposedSeq)
	print(tour)
	print(merge(tour))
	print()
	
	''' TEST WITH PHONE PAD '''
	''' TODO: '''
	b = [
		[1,2,3],
		[4,5,6],
		[7,8,9],
		['',0,'']
	]
	knightstour   = getLongestKnightsTour(b, 0, 0)
	proposedSeq   = knightstour[1]
	tour          = knightstour[0]
	print(proposedSeq)
	print(tour)
	print(merge(tour))
	print()
