'''
	7. Intersection
			Given two singly linked lists, determine if the two lists 
			intersect.
			Return the intersecting node.
			Note that the intersection is defined based on reference, not
			value.
			That is, if the kth node of the first ilnked list is the exact
			same node (by reference) as the jth node of the second linked
			list, then they are intersecting

	Thoughts:
		I didn't even know that we could do this.
		I am going to run tests in the shell...
'''
import sys
sys.path.append('/Users/tannerleewoody/Workspace/google/CtCI/linkedLists/')
from LinkedList import LinkedList
from LinkedList import LinkedListNode

def getIntersection(ll1, ll2):
	''' Return first intersecting node  '''
	''' Else return None '''
	t1 = ll1.tail		#Tail One
	t2 = ll2.tail		#Tail Two
	if t1 is not t2 or t1 is None:
		return None
	if ll1 is ll2:
		#Same exact list...
		return ll1.head
	l1 = len(ll1)
	l2 = len(ll2)
	if l2<l1:
		return getIntersection(ll2, ll1)
	'''************ End Sanity Checks ************'''
	'''*************** Begin  Work ****************'''
	p1 = ll1.head		#Pointer for First Linked List
	p2 = ll2.head		#Pointer for Second Linked List
	for i in range(0, l2-l1):
		p2 = p2.next
	#Both pointers are at the same level
	#We can find the intersecting point now
	while p1 and p2:
		if p1 is p2:
			return p1
		p1 = p1.next
		p2 = p2.next
	return None

def q7():
	foo = LinkedList( [1,2,3] )
	bar = LinkedList( [3,3,3] )
	baz = LinkedListNode(44, None, foo.tail)

	foo.tail.next = baz
	bar.tail.next = baz
	foo.tail      = foo.tail.next
	bar.tail      = bar.tail.next
	assert bar.tail is baz

	foo.append(99)							#This should add 99 to bar, too
	baz = foo.tail
	bar.tail.next = baz					#But it will not update bar, like it will foo
	bar.tail      = bar.tail.next		#So, update bar's tail manually
	assert foo == LinkedList([1,2,3,44,99])			#This is `foo`
	assert bar == LinkedList([3,3,3,44,99])			#This is `bar`
	assert getIntersection(foo, bar) == foo.get(3)	#They share `44` first

	foo = LinkedList([1,2])
	baz = bar.get(4)
	foo.tail.next = baz
	foo.tail      = foo.tail.next
	assert getIntersection(foo, bar) == baz							#Different length
	assert getIntersection(bar,foo) == baz								#Longer first
	assert getIntersection(foo, foo) == foo.head						#Same LinkedList
	assert getIntersection(LinkedList(), LinkedList()) is None	#Same None LL
	assert getIntersection(LinkedList(), foo) is None				#No Intersection w/ None LL
	
	bar = LinkedList([1,2,3])
	assert getIntersection(bar,foo) == None							#No Intersection w/ filled LL

	print('q7.py: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q7()

