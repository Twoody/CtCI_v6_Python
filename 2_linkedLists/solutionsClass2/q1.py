'''
	1. Remove Dups
			Write code to remove duplicates from an unsorted linked list.
			Follow up:
				How would you solve the probem if a temporary buffer is 
				not allowed?
'''
from LinkedList import LinkedList

def removeDups(ll):
	if ll.head is None:
		return 0
	c = h = ll.head
	c = c.next
	i = 1
	l = len(ll)
	removals = 0
	while c and i < l:
		p = c.prev
		j = i
		while p and j>=0:
			#Compare to elements we alrady saw in the list
			j -= 1
			if c == p:
				ll.remove(j)
				removals += 1
			p = p.prev
		i +=1
		c = c.next
	return removals

def q1():
	assert removeDups( LinkedList( [] ) ) == 0
	assert removeDups( LinkedList( [1] ) ) == 0
	assert removeDups( LinkedList( [1,2] ) ) == 0
	assert removeDups( LinkedList( [1,2,2] ) ) == 1

	foo = LinkedList( [1,2,2] )
	removeDups(foo)
	assert foo == LinkedList( [1,2] )
	print('PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q1()

