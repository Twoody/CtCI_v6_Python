'''
	5. Sum Lists
			Given two numbers represented by a linked list, where each
			node contains a single digig, write a function that adds the
			two numbers and returns the sum as a linked list.
			The digits are stored in reverse order, such that the 1's
			digit is at the head of the list.
			Example:
				Input: (7-> 1 -> 6) + (5 -> 9 -> 2).
					That is, 617 + 295.
				Output: 2 -> 1 -> 9.
					That is, 912.
			FOLLOW UP:
				Suppose the digits are stored in forward order. 
				Repeat the above problem.
				EXAMPLE
					Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).
						That is,617 + 295. 
					Output: 9 -> 1 -> 2.
						That is, 912.
			Hints: 
				#7, #30, #71, #95, #109
	
	Thoughts:
		We just make a while loop with the shorter length.
		If we have a carriage, append that as such.
		This will run in O(n) time, where n is the length of the larger LL.
		I am calling length, which will increase the run time.
		Our actual end method runs in O(2n + 2m), specifically.
		We could speed this up with a while loop, and storing in memory
			the `bigger` LL and `smaller` LL.
		The drawback of this is readability.

		For the follow up, we can just implement a `pop()` method for LinkedList.py
		We then run through a while loop for ll1.pop() and ll2.pop(), until ll1 is None
			and ll2 is None.
		We would still have a carriage.
		We would `push()` our results instead of `append()`.
'''
import sys
sys.path.append('/Users/tannerleewoody/Workspace/google/CtCI/2_linkedLists/')
from LinkedList import LinkedList

def LLSum(ll1, ll2):
	''' Add values of ll1 and ll2 to return new linked list '''
	l1 = len(ll1) #Length 1
	l2 = len(ll2) #Length 2
	if l1 > l2:
		#We want to have an order to which one is bigger and which is smaller
		return LLSum(ll2, ll1)
	if l1 == 0:
		return ll2
	ret   = LinkedList()
	cur1  = ll1.head
	cur2  = ll2.head
	carry = 0
	for i in range(0, l1):
		app = cur1.value + cur2.value
		if app > 9:
			app = app - 10 + carry
			carry = 1
		else:
			app += carry
			carry = 0
		ret.append(app)
		cur1 = cur1.next
		cur2 = cur2.next
	for i in range(l1,l2):
		ret.append(cur2.value + carry)
		carry = 0
		cur2 = cur2.next
	if carry == 1:
		ret.append(carry)
		carry = 0
	return ret

def q5():
	assert LLSum( LinkedList( [] ),  LinkedList( [] ) ) == LinkedList( [] )
	assert LLSum( LinkedList( [] ),  LinkedList( [0] ) ) == LinkedList( [0] )
	assert LLSum( LinkedList( [0] ),  LinkedList( [0] ) ) == LinkedList( [0] )
	assert LLSum( LinkedList( [9] ),  LinkedList( [9] ) ) == LinkedList( [8,1] )
	assert LLSum( LinkedList( [0,0,1] ),  LinkedList( [9] ) ) == LinkedList( [9,0,1] )
	assert LLSum( LinkedList( [0,0,1] ),  LinkedList( [0,0,9] ) ) == LinkedList( [0,0,0,1] )
	assert LLSum( LinkedList( [7,1,6] ),  LinkedList( [5,9,2] ) ) == LinkedList( [2,1,9] )
	print('q5.py: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q5()

