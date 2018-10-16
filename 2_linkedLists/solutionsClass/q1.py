'''
	1. Remove Dups
			Write code to remove duplicates from an unsorted linked list.
			Follow up:
				How would you solve the probem if a temporary buffer is 
				not allowed?

	Thoughts:
		If we want to remove duplicates, my first thought is to make a temp
		and to append to the temp any item that is already not in the temp.
		This will take O(1 + 2 + ... + n) which is Gauss Summation.
		Gauss Summation gives us ~O(n-n^2)

		Our other choice is to search for a duplicate before we add the item.
		This will take O(n-1 + n-2 + ... + n-n+1 + n-n)
		, which is O( n(1-1/n + 1-2/n + ... + 1-1+1/n + 0) )
		, which is O( n(1 + 1 + ... + 0 + 0) )
		, which is O(n^2)
		This approach is sligtly faster, and only has space complexity of O(1).

		However, if we are allowed more advanced data structures, like a hash table,
		this becomes a O(n) time, as we will not have to traverse multiple times.
'''
import sys
sys.path.append('/Users/tannerleewoody/Workspace/google/CtCI/2_linkedLists/')
from LinkedList import LinkedList

def __removeDups(ll):
	''' Slower, O(1) space complexity option; NO BUFFER'''
	''' We have to look into the prev, not next to keep one original '''
	current = ll.head
	while current:
		isunique	= True
		if current.prev:
			runner = current.prev
			while runner:
				if runner.value == current.value:
					isunique = False
					break
				runner = runner.prev
		if isunique == False:
			''' We need to update the prev node to skip the current node by changing its next'''
			#skipNextNode(current.prev)
			current.prev.skipNextNode()
			''' We also need to update the next node to have new prev node'''
			if current.next:
				current.next.skipPrevNode()
				#skipPrevNode(current.next)
		current = current.next
	return ll

def removeDups(ll):
	''' Faster, hashtable option  '''
	nll		= LinkedList()
	ht			= {}
	current	= ll.head
	while current:
		v = current.value
		if v not in ht:
			ht[v] = True
			nll.append(v)
		current	= current.next
	return nll

def q1():
	assert removeDups(LinkedList([])) == LinkedList([])
	assert removeDups(LinkedList([1])) == LinkedList([1])
	assert removeDups(LinkedList([1,2])) == LinkedList([1,2])
	assert removeDups(LinkedList([1,2,2])) == LinkedList([1,2])
	assert removeDups(LinkedList([2,2])) == LinkedList([2])
	assert removeDups(LinkedList([2,2,1])) == LinkedList([2,1])
	assert removeDups(LinkedList([2,1,2])) == LinkedList([2,1])
	assert removeDups(LinkedList([1,2,2])) == LinkedList([1,2])
	assert removeDups(LinkedList([1,1,1])) == LinkedList([1])
	
	assert __removeDups(LinkedList([])) == LinkedList([])
	assert __removeDups(LinkedList([1])) == LinkedList([1])
	assert __removeDups(LinkedList([1,2])) == LinkedList([1,2])
	assert __removeDups(LinkedList([1,2,2])) == LinkedList([1,2])
	assert __removeDups(LinkedList([2,2])) == LinkedList([2])
	assert __removeDups(LinkedList([2,2,1])) == LinkedList([2,1])
	assert __removeDups(LinkedList([2,1,2])) == LinkedList([2,1])
	assert __removeDups(LinkedList([1,2,2])) == LinkedList([1,2])
	assert __removeDups(LinkedList([1,1,1])) == LinkedList([1])
	print('q1.py: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q1()

