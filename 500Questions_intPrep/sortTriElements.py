'''

Author:
	Tanner Woody
	20181029

Purpose:
	Given a list of values either 0, 1, or 2, sort the list.
	List should be sorted s.t. all zeros, then all 1's, then all 2's.
'''

def sortTriElements(l):
	''' Create a pivot around middle point, 1 '''
	ret = []
	pivot = 0 #count where 0 ends and 1 begins;
	for i in range(0, len(l)):
		item = l[i]
		if item == 2:
			ret.append(2)
		elif item == 1:
			ret.insert(pivot, 1)
		elif item == 0:
			ret.insert(0, 0)
			pivot += 1
		else:
			raise ValueError('ERROR: sortTriElements: LIST HAS INCORRECT VALUE `'+str(I)+'`')
	return ret


if __name__ == "__main__":
	assert sortTriElements([]) == []
	assert sortTriElements([0]) == [0]
	assert sortTriElements([1]) == [1]
	assert sortTriElements([0,1]) == [0,1]
	assert sortTriElements([1,0]) == [0,1]
	assert sortTriElements([0,2]) == [0,2]
	assert sortTriElements([2,0]) == [0,2]
	assert sortTriElements([2,1]) == [1,2]
	assert sortTriElements([2,1,0]) == [0,1,2]
	assert sortTriElements([1,2,0]) == [0,1,2]
	assert sortTriElements([0,1,2]) == [0,1,2]
	assert sortTriElements([1,0,0,0,1,1]) == [0,0,0,1,1,1]
	assert sortTriElements([1,0,2,2,0,0,2,2,1,1]) == [0,0,0,1,1,1,2,2,2,2]
