'''
Author:
	Tanner.L.Woody@gmail.com
	20181030

Purpose:
	Given a matrix of int colors, find longest path of similar colors.
'''
from random import randint
from math import ceil

def getneighbors(m, row, col):
	color = m[col][row]
	right = row-1
	left  = row+1
	top   = col-1
	bot   = col+1
	h     = len(m)     #height of matrix
	w     = len(m[0])  #width of matrix
	neighbors = []
	if right >= 0 and right < w:
		if bot >=0 and bot < h and m[bot][right] == color:          #Diagonals
			neighbors.append( (right,bot) )
		if top >=0 and top < h and m[top][right] == color:          #Diagonals
			neighbors.append( (right,top) )
		if m[col][right] == color:                                  #Right one
			neighbors.append( (right,col) )
	if left >= 0 and left < w:
		if bot >=0 and bot < h and m[bot][left] == color:           #Bot-Left Diagonal
			neighbors.append( (left, bot) )
		if top >=0 and top < h and m[top][left] == color:           #Diagonals
			neighbors.append( (left,top) )
		if m[col][left] == color:                                   #Left one
			neighbors.append( (left,col) )
	if top >=0 and top < h and m[top][row] == color:               #Top one
		neighbors.append( (row,top) )
	if bot >=0 and bot < h and m[bot][row] == color:               #Bottom one
		neighbors.append( (row,bot) )
	return neighbors

def getLongestPath(m):
	v       = {}                         #visited
	s       = []                         #stack
	longest = []                         #array containing nodes in longest path
	ls      = 0                          #length of longest
	half    = ceil(len(m[0])*len(m)/2)   #EZ escape if longest >= half
	iters   = 0                          #Validate test process covered each node
	for c in range(0, len(m)):           #c is col
		for r in range( 0, len(m[c]) ):   #r is row
			if (r,c) in v:
				continue                    #if we have been to row, column do not duplicate work
			s           = []
			needsworked = []
			curSize     = 1
			v[(r,c)]    = True
			s.append( (r,c) )              #x,y coordinate pairs
			needsworked.append( (r,c) )
			while len(needsworked) > 0:
				cur       = needsworked.pop(-1)
				neighbors = getneighbors(m, cur[0], cur[1]) #getneightbors() filters out by colors already
				for n in neighbors:
					if n in v:
						continue
					s.append(n)
					needsworked.append(n)
					curSize += 1
					v[(n[0], n[1])] = True                   #Only visit each node once
			if curSize >= half:
				return (s, curSize)
			if curSize > ls:
				longest = s.copy()
				ls      = curSize
			iters += curSize
	if iters != len(m) * len(m[0]):
		print('WARNING: ITERATIONS OFF: ' + str(iters) )
	return (longest, ls)

if __name__ == "__main__":
	import timeit
	#Empty Checks
	assert getLongestPath( [ [] ] ) == ([], 0)
	assert getLongestPath( [ [1,2,3] ] ) == ([(0,0)], 1)
	assert getLongestPath( [ [1,2,3],[4,5,6] ] ) == ([(0,0)], 1)
	assert getLongestPath( [ [1,2,3],[4,5,6],[7,8,9] ] ) == ([(0,0)], 1)
	assert getLongestPath( [ [1,2,3],[4,5,6],[1,2,3] ] ) == ([(0,0)], 1)

	#Full matches
	assert getLongestPath( [ [1], [1] ] ) == ( [ (0,0), (0,1) ], 2 )
	assert getLongestPath( [ [1,0], [0,1] ] ) == ( [ (0,0), (1,1) ], 2 )
	assert getLongestPath( [ [1,0], [0,2] ] ) == ( [ (1,0), (0,1) ], 2 )
	assert getLongestPath( [ [1,2,3], [1,2,3], [1,2,3] ] ) == ( [ (0,0), (0,1), (0,2) ], 3 )
	m = [
		[1,2,3],
		[1,1,3],
		[1,2,1]
	]
	assert getLongestPath( m ) ==( [ (0,0), (1,1), (0,1), (0,2), (2,2) ], 5 )
	m = [
		[1,0,0,2,2],
		[1,1,0,1,2],
		[1,0,1,2,2],
		[2,2,2,0,0],
		[4,1,1,1,1]
	]
	foo     = getLongestPath(m)
	xy_pair = foo[0][0]
	x       = xy_pair[0]
	y       = xy_pair[1]
	assert m[y][x] == 2
	
	bigArr = []
	size   = 2222
	for i in range(0, size):
		row = []
		for j in range(0, size):
			row.append( randint(0,1) )
		bigArr.append( row )
	tic = timeit.default_timer()
	print('starting main benchmark')
	print('\t' + str(size*size) + ' NODES TO ITTERATE')
	print('\tHALF POINT: ' + str(ceil(size*size/2)))
	t = getLongestPath( bigArr )
	toc = timeit.default_timer()
	print('\tLONGEST WALK: ' + str(t[1]) + ' NODES')
	print('\tTIME: ' + str(toc-tic))
	print('END BENCHMARK\n')
