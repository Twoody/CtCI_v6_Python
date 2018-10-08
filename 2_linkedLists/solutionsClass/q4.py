'''
	4. Partition
			Write code to partition a linked list around a value x, such 
			that all nodes less than x come before all nodes greater than 
			or equal to x. IF x is contained within the list, the values 
			of x only need to be after the elements less than x. The 
			partition element x can appear anywhere in the `right partition`; 
			It does not need to appear between the left and right partitions.
			Example:
				I:  3-> 5-> 8-> 5 ->10-> 2-> 1
				O:  3-> 1-> 2-> 10-> 5-> 5-> 8

	Thoughts:
		We can just bump all of the items that are greater than k to the tail.
		This will take us just the time to traverse the list.


'''
import sys
sys.path.append('/Users/tannerleewoody/Workspace/google/CtCI/linkedLists/')
from LinkedList import LinkedList

def partitionLL(ll, k):
	''' Partition linkedlist around value k '''
	cur = ll.head
	cnt = 0
	i   = 0
	l   = len(ll)
	while i<l:
		nextnode = cur.next
		ll.remove(cnt)
		if cur.value < k:
			ll.push(cur.value)
			cnt +=1
		else:
			ll.append(cur.value)
		cur = nextnode
		i +=1
	return ll

def q4():
	assert partitionLL( LinkedList( [] ) ,0 )					== LinkedList( [] )
	assert partitionLL( LinkedList( [1] ) ,1 )				== LinkedList( [1] )
	assert partitionLL( LinkedList( [1] ) ,0 )				== LinkedList( [1] )
	assert partitionLL( LinkedList( [1] ) ,2 )				== LinkedList( [1] )
	assert partitionLL( LinkedList( [3,1] ) ,2 )				== LinkedList( [1,3] )
	assert partitionLL(LinkedList( [3,5,8,5,10,2,1] ),4)	== LinkedList([1,2,3,5,8,5,10])
	
	print('q4.py: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q4()

