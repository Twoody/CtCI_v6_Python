'''

Author:
	Tanner Woody
	20181029

Purpose:
	Given a list of values either 0 or 1, sort the list.
	List should be sorted s.t. all zeros, then all 1's.
'''

def sortBinElements(l):
	zL = []
	oL = []
	for i in l:
		if i ==0:
			zL.append(0)
		elif i ==1:
			oL.append(1)
		else:
			raise ValueError('ERROR: sortBinElements: LIST HAS INCORRECT VALUE `'+str(I)+'`')
	return zL+oL


if __name__ == "__main__":
	assert sortBinElements([1,0,0,0,1,1]) == [0,0,0,1,1,1]
	assert sortBinElements([]) == []
	assert sortBinElements([0]) == [0]
	assert sortBinElements([1]) == [1]
	assert sortBinElements([0,1]) == [0,1]
	assert sortBinElements([1,0]) == [0,1]
