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
import sys
sys.path.append('/Users/tannerleewoody/Workspace/google/CtCI/2_linkedLists/')
from LinkedList import LinkedList

def deleteMiddleNode(ll):
	''' Just going to delete floor and ceiling of middle for evens '''
	length = len(ll)
	if length == 0:
		return True #No middle in nothing
	ll.remove( (length//2) )
	if length%2 == 0:
		ll.remove( (length//2)-1 )			#The true middle if odd and covers even second middle
	return True

def q3():
	llc1 = LinkedList()			#Linked List Compare
	llc2 = LinkedList([1,3])	#Linked List Compare
	llc3 = LinkedList([1,4])	#Linked List Compare
	ll1 = LinkedList()
	ll2 = LinkedList([0])
	ll3 = LinkedList([0,1])
	ll4 = LinkedList([1,2,3])
	ll5 = LinkedList([1,2,3,4])
	assert deleteMiddleNode(ll1) 	== True
	assert deleteMiddleNode(ll2)	== True
	assert deleteMiddleNode(ll3)	== True
	assert deleteMiddleNode(ll4)	== True
	assert deleteMiddleNode(ll5)	== True
	assert ll1 == llc1
	assert ll2 == llc1
	assert ll3 == llc1
	assert ll4 == llc2
	assert ll5 == llc3

	print('q3.py: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q3()

