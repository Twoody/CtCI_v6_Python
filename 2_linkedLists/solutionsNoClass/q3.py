'''
	3. Delete Middle Node
			Implement an algorithm to delete a node in the middle of a
			singly linked list, given only access to that node.
			The middle is any node but the first and last node, not 
			necessarily the exact middle. 
			Example:
				I: the node c from the linked list:
					a -> b -> c -> d -> e -> f
				O: Nothing is retured. The new linked list looks like:
					a -> b -> d -> e -> f

			not allowed?
'''
def deleteK(mList, k):
	''' Delete kth item from list  '''
	length = len(mList)
	if k >= length:
		return mList
	if k <0:
		return mList
	ret = []
	for i in range(0, length):
		if i != k:
			ret.append(mList[i])
	return ret

def q3():
	assert deleteK( [], 0) 				== []
	assert deleteK( [], -1) 			== []
	assert deleteK( [], 99) 			== []
	assert deleteK( [1,2], 0)  		== [2]
	assert deleteK( [1,2], 1)  		== [1]
	assert deleteK( [1,2], -1)  		== [1,2]
	assert deleteK( [1,2,3,4], 1)  	== [1,3,4]
	print('PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q3()

