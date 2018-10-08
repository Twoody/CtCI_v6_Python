'''
2. Reurn Kth to Last
			Implement an algorithm to find the kth to last element of a 
			singly linked list.
			Hint:
				#8, #25, #41, #67, #126

	Thoughts:
		We should add these functions to our LinkedList.py class
		We should also init ValueError testing.

		getFromIndices can also change the current LinkedList via node arrangment
		and simply changeing ll.head to the kth position
			--> We would also need to set the kth node.prev to None
			--> Also make sure we set `last` node's tail and tail.prev/tail.next
			--> This is best to be implemented in a ll.strip() as we do not want to 
					lose our current list if we do need two of them...

'''
import sys
sys.path.append('/Users/tannerleewoody/Workspace/google/CtCI/linkedLists/')
from LinkedList import LinkedList

def getFromIndices(ll, k, last=-1):
	ret = LinkedList()
	cnt = 0
	current = ll.head
	while current:
		if k <= cnt:
			if last >=cnt or last==-1:
				ret.append(current.value)
		current = current.next
		cnt +=1
	if ret.head is None:
		raise ValueError("ERROR:getFromIndices():INDEXING LinkedList() OUT OF BOUNDS AT `"+str(k)+"`")
	return ret

def getFromIndex(ll, k, last=-1):
	''' Return Node of kth position '''
	''' Defaults to list of nodes if `last`'''
	current = ll.head
	cnt = 0
	if last!=-1:
		return getFromIndices(ll, k, last)
	while current:
		if k == cnt:
			return current
		current = current.next
		cnt += 1
	raise ValueError("ERROR: INDEXING LinkedList() OUT OF BOUNDS AT `"+str(k)+"`")


def q2():
	assert getFromIndex( LinkedList([1]), 0 ).value 	== 1
	assert getFromIndex( LinkedList([1,2]), 0 ).value	== 1
	assert getFromIndex( LinkedList([1,2]), 1 ).value	== 2

	assert getFromIndex( LinkedList([1,2]), 1, 1 ) 	== LinkedList([2])
	assert getFromIndex( LinkedList([1,2]), 0, 1 ) 	== LinkedList([1,2])
	assert getFromIndex( LinkedList([1]), 0 ,0 ) 	== LinkedList([1])
	assert getFromIndex( LinkedList([1,2]), 0, 0 ) 	== LinkedList([1])
	assert getFromIndex( LinkedList([1,2]), 1, 1 ) 	== LinkedList([2])
	print('q2.py: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q2()

