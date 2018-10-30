'''
Author:
	Tanner.L.Woody@gmail.com
	20181030

Purpose:
	Given a matrix of int colors, find longest path of similar colors.
'''
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
	v       = {}   #visited
	s       = []   #stack
	longest = []   #array containing nodes in longest path
	ls      = 0    #length of longest
	for c in range(0, len(m)):
		for r in range( 0, len(m[c]) ):
			if (r,c) in v:
				continue                    #if we have been to row, column do not duplicate work
			s        = []
			curSize  = 1
			v[(r,c)] = True
			s.append( (r,c) )              #x,y coordinate pairs
			while curSize > 0:
				print('\t' + str(s))
				if curSize > ls:
					longest  = s.copy()
					ls = curSize
				cur         = s[curSize-1]
				neighbors   = getneighbors(m, cur[0], cur[1]) #Filters out by colors already
				needspopped = True #Nothing more to add; Go back to previous;
				for n in neighbors:
					if n in v:
						continue
					s.append(n)
					curSize += 1
					v[(n[0], n[1])] = True
					needspopped     = False
				if needspopped == True:
					curSize -= 1
					t = s.pop(curSize)
	print(longest)
	return (longest, ls)

if __name__ == "__main__":
	assert getLongestPath( [[]] ) == ([], 0)
	assert getLongestPath( [[1,2,3]] ) == ([(0,0)], 1)
	assert getLongestPath( [[1,2,3],[4,5,6]] ) == ([(0,0)], 1)
	assert getLongestPath( [[1,2,3],[4,5,6],[7,8,9]] ) == ([(0,0)], 1)
	assert getLongestPath( [[1,2,3],[4,5,6],[1,2,3]] ) == ([(0,0)], 1)
	assert getLongestPath( [ [1], [1] ] ) == ( [ (0,0), (0,1) ], 2 )
	assert getLongestPath( [ [1,0], [0,1] ] ) == ( [ (0,0), (1,1) ], 2 )
	assert getLongestPath( [ [1,0], [0,2] ] ) == ( [ (1,0), (0,1) ], 2 )
	assert getLongestPath( [ [1,2,3], [1,2,3], [1,2,3] ] ) == ( [ (0,0), (0,1), (0,2) ], 3 )
	m = [
		[1,2,3],
		[1,1,3],
		[1,2,1]
	]
	assert getLongestPath( m ) ==( [ (0,0), (1,1), (2,2), (0,1), (0,2) ], 3 )



