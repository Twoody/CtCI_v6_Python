'''
	Q1.8: Zero Matrix
		Write an algorithm such that if an element in an MxN matrix
		is 0, its entrie row and column are set to zero.

	Thoughts:
		This is a tricky one.
		If we take the time to look for all of the zeros, first, we can easily 
		duplicate our run time, which is allready at m*n.
		If we build our matrix as we go, we risk also duplicating the run time
		by going back and switching all of the entries at the end.
		
		The best thoguht I have it to implement this such that we have a holding
		stage, where the items set to be switched to zero sit, and we fill in
		the rest of the items from there.
		Otherwise, we can create a situation where the zero's compound on one 
		another.

		CtCI seems to agree with me, and using two arrays and flags.
'''
def nullifyRow(matrix, row):
	for i in range(0, len(matrix[row])):
		matrix[row][i] = 0
	return matrix
def nullifyCol(matrix, col):
	for i in range(0, len(matrix)):
		matrix[i][col] = 0
	return matrix

def nullifyMatrix(matrix):
	'''If cell is zero, set all cells in adjacent col and row to zero'''
	m = len(matrix)
	n = len(matrix[0])
	rows = []
	cols = []
	for i in range(0, m):
		for j in range(0, n):
			if matrix[i][j] == 0:
				rows.append(i)
				cols.append(j)
	for row in rows:
		matrix = nullifyRow(matrix, row)
	for col in cols:
		matrix = nullifyCol(matrix, col)
	return matrix


def q8():
	foo  = [ [1,2,3], [3,4,0], [4,0,1] ]
	nFoo = [ [1,0,0], [0,0,0], [0,0,0] ]
	assert nullifyMatrix(foo) == nFoo
	print('Q8: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q8()
