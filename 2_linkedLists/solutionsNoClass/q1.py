'''
	1. Remove Dups
			Write code to remove duplicates from an unsorted linked list.
			Follow up:
				How would you solve the probem if a temporary buffer is 
				not allowed?
'''
def removeDups(mList):
	nList = []
	for i in range(0, len(mList)):
		if mList[i] not in nList:
			nList.append(mList[i])
	return nList

def q1():
	assert removeDups([1,1]) == [1]
	assert removeDups([1,2,1]) == [1,2]
	assert removeDups([]) == []
	assert removeDups([12,44,3,22]) == [12,44,3,22]
	print('PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q1()

