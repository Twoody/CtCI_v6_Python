'''
	Q1.7: Rotate Matrix
		Given an image represented by an NxN matrix, where each
		pixel in the image is 4 bytes, write a method to rotate the
		image by 90 degrees. Can you do this in place?
	
	Thoughts:
		 _              _             _              _ 
		|                |   90deg   |                |
		| a0  a1  ... an |  _____|\  | n0  ...  b0 a0 |
		| b0  b1  ... bn |  _____  / | n1  ...  b1 a1 |
		| ...            |       |/  | ...     ... ...|
		| n0  n1  ... nn |           | nn  ...  bn an |
		|_              _|           |_              _|


		  90deg   |                |
		 _____|\  | nn  ... n1  n0 |
		 _____  / | ...    ... ... |
		      |/  | bn  ... b1  b0 |
		          | an  ... a1  a0 |
		          |_              _|


		From college, I know there is an easy transpose to do on the matrix.
		However, what if I do not remember it (which I truthfully do not
		at this point in time of writing and reviewing this question)?!

		What I should first ask:
			How is the matrix stored?
			Is it a list of lists?
			Is it some sort of nasty looking tree?
			Is it a list of tuples?
			Is it a dict of lists?
			Is it a dict of dicts?

		The most structured approach is a list of lists.
		If we use a hashtable, it might have some issues when looking up
		the associated list value during a:
			for key in mDic:
				mList = mDic[key]
		How do we know that the mList is going to be the first in the matrix?

		Thus, let us work with list of lists.
			mImage = [ [a0, a1, ..., an], ..., [n0, n1, ..., nn] ]
		
		If we make a new list and move each component, we would have to
		look at each first item of each inner list, and append to a new list:
			nList0 = [a0, ..., n0]

		We then append this to our new image list:
			nImage = []
			nImage.append(nList0)

		If we do this for each item, we will have O(n0 + n1 + ... + nn).
		That will evaluate to O(n * n), or O(n^2).

		But do we have to look at each item?
		Are we not assuming that each item is getting rotated, when in fact,
		some items may keep their current place.

		For example:
			Take a 4x4 matrix of:
				mImage = [ [1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4] ]
			Rotating this, we get:
				nImage = [ [1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4] ]

			For visual reference:
				 1 2 3 4		1 1 1 1
				 1 2 3 4		2 2 2 2 
				 1 2 3 4		3 3 3 3
				 1 2 3 4		4 4 4 4 

		Exmample2:
			Take a 4x4 matrix of:
				mImage = [ [1,2,3,4], [5,6,7,8], [9,a,b,c], [d,e,f,g] ]
			Rotating this, we get:
				nImage = [ [d,9,5,1], [e,a,6,2], [f,b,7,3], [g,c,8,4] ]

			For visual reference:
             1 2 3 4    d 9 5 1
             5 6 7 8    e a 6 2
             9 a b c    f b 7 3
             d e f g    g c 8 4
			
			
'''

def rotateMatrix(_matrix):
	nMatrix = []
	for i in range(0, len(_matrix)):
		nLayer = []
		for j in range(0, len(_matrix)):
			nLayer.append(_matrix[j][i])
		nMatrix.append(nLayer)
	return nMatrix

def printMatrix(matrix):
	out = "\t\t"
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[i])):
			out += str(matrix[i][j]) + ' '
		if (i != len(matrix)-1):
			out += "\n\t\t"
	print(out)
	return True

def q7():
	mImage = [ [1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4] ]
	nImage = rotateMatrix(mImage)
	#printMatrix(mImage)
	#print()
	#printMatrix(nImage)
	assert nImage == [ [1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4] ]
	print('Q7: PASSED ALL TESTS')
	return True
	
if __name__ == "__main__":
	q7()
