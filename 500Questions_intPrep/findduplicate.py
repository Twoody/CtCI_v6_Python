def finddup(arr):
	''' Find first duplicate match in arr; If dup DNE, return None '''
	hm = {} #hashmap
	for i in arr:
		if i in hm:
			return i
		hm[i] = True
	return None

if __name__ == "__main__":
	assert finddup( [] ) is None
	assert finddup( [1] ) is None
	assert finddup( [1,1] ) == 1
	assert finddup( [1,2,3] ) is None
	assert finddup( [1,2,3,1] ) == 1
	assert finddup( [1,2,3,4,4] ) == 4
