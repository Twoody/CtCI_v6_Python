def getLargestUniqueSub(arr):
	''' return largest possible arr of unique elements '''
	''' sub-array elements must be in order found in parent array '''
	hm       = {}
	longest  = []
	longestS = 0 #Avoid calculating len(longest) mult times;
	curr     = []
	currS    = 0
	for i in range(0, len(arr):
		for j in range(i, len(arr)):
			item = arr[j]
			if item in hm:
				break
			hm[item] = True
			curr.append(item)
		if currS > longestS:
			longest  = curr
			longestS = currS
		currS = 0
		curr  = []
	return longest

if __name__ == "__main__":
	assert getLargestUniqueSub( [] ) == []
	assert getLargestUniqueSub( [0] ) == [0]
	assert getLargestUniqueSub( [1,2] ) == [1,2]
	assert getLargestUniqueSub( [1,2,1] ) == [1,2]
	assert getLargestUniqueSub( [1,2,1,2,3] ) == [1,2,3]
	assert getLargestUniqueSub( [1,2,3,1,2] ) == [1,2,3]
	assert getLargestUniqueSub( [1,2,3,1,2,4] ) == [1,2,3]
	assert getLargestUniqueSub( [2,0,2,1,4,3,1,0] ) == [0,2,1,4,3]
