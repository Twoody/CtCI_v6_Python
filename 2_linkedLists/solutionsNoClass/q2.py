'''
2. Reurn Kth to Last
			Implement an algorithm to find the kth to last element of a 
			singly linked list.
			Hint:
				#8, #25, #41, #67, #126


'''
def segmentList(mList, k):
	''' return list from k to end of list'''
	length = len(mList)
	ret    = []
	if k >= length:
		return ret
	if k<= 0:
		return mList
	for i in range(k, length):
		ret.append(mList[i])
	return ret

def q2():
	assert segmentList([], 0) == []
	assert segmentList([], 99) == []
	assert segmentList([], -1) == []
	assert segmentList([1,2], 3) == []
	assert segmentList([1,2], -1) == [1,2]
	assert segmentList([1,2,3,4,5,6], 4) == [5,6]
	assert segmentList([1,2,3,4,5,6], 5) == [6]
	print('PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q2()

