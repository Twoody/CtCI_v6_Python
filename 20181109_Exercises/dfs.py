'''
DFS Initialization on a knights tour

Begining Time:
	10:03
Failure Time:
	10:36

Purpose:
	Construct a completed knights tour for a provided board
'''

def getBestTour(board, startPos):
	v    = [] #visited
	ws   = {} #hashtable of walks
	cw   = [] #current walk
	cwl  = 0  #current walk length
	bw   = [] #best walk
	bwl  = 0  #best walk length
	s    = [] #stack of walks to visit
	ss   = 0  #stack size
	akms = getAKMs(board)

	s.append(startPos)
	v.append(startPos)
	cw.append(startPos)
	cwl += 1
	ws[cw.copy] = True

	while s != []:
		cn				= s[ss-1] #current node
		v[curnode]  = True
		didAddMove	= False
		for nextMove in akms[cn]:
			if nextMove in visited:
				continue
			s.append(nextMove)
			ss += 1
			visited.
			didAddMove = True
			break
		if ss > bwl:
			bw = s.copy()
		if didAddMove == False:
			ws[str(s)] == True
			s.pop(ss-1)
			ss -=1
			v.remove(cn)





if __name__ == "__main__":
	board = [	[1 ,2, 3],
					[4 ,5, 6],
					[7 ,8, 9],
					['',0,'']
				]
	akm = getAKMs(board)
	assert isinstance(akm, dict)
	assert akm['0'] == [4,6]
	assert akm['5'] == []

	startPos = 1
	bestTour = getBestTour(board, startPos)
