'''
	4. Partition
			Write code to partition a linked list around a value x, such 
			that all nodes less than x come before all nodes greater than 
			or equal to x.
			If x is contained within the list, the values of x only need 
			to be after the elements less than x. 
			The partition element x can appear anywhere in the `right partition`; 
			It does not need to appear between the left and right partitions.
			Example:
				I:  3-> 5-> 8->  5->10-> 2-> 1
				O:  3-> 1-> 2-> 10-> 5-> 5-> 8
'''
def fixCenter(mList, k):
	''' Create a center point `k` such that for all x in mList,  '''
	''' if x<k, x is on the left, and if x>=k, x is on the right  '''
	ret = []
	addLater = []
	for i in range(0, len(mList)):
		if mList[i] < k:
			ret.append(mList[i])
		else:
			addLater.append(mList[i])
	for x in addLater:
		ret.append(x)
	return ret

def q4():
	assert fixCenter([], 0) == []
	assert fixCenter([0], 0) == [0]
	assert fixCenter([0,1], -1) == [0,1]
	assert fixCenter([2,3,1], 2) == [1,2,3]
	#assert fixCenter([3,5,8,5,10,2,1], 6) == [3,1,2,10,5,5,8]
	#print(fixCenter( [3,5,8,5,10,2,1], 5 ))
	assert fixCenter([3,5,8,5,10,2,1], 5) == [3,2,1,5,8,5,10]
	print('PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q4()

