'''
	6. Palindrome
			Implement a function to check if a linked list is a palindrome.
			Hints:
				5, 13, 29, 61, 101
	
	Thoughts:
		To check the linked list, we can just check the first half,
		and then check that half to the next half, but backwards.
		Our Linked List is smart enough though, that we could just
		check the tail and tail.prev to head and head.next...

'''
import sys
sys.path.append('/Users/tannerleewoody/Workspace/google/CtCI/linkedLists/')
from LinkedList import LinkedList

def isPalindrome(ll):
	if ll.head is None or ll.tail is None:
		#Nothing implies palindrome
		return True
	head = ll.head
	tail = ll.tail
	l = len(ll)
	i = 0
	while head and tail and i < l//2:
		if head is tail:
			return True
		elif head == tail:
			head = head.next
			tail = tail.prev
			i += 1
			continue
		else:
			return False
	return True

def q6():
	assert isPalindrome( LinkedList( [] ) ) == True
	assert isPalindrome( LinkedList( [1] ) ) == True
	assert isPalindrome( LinkedList( [1,2] ) ) == False
	assert isPalindrome( LinkedList( [2,2] ) ) == True
	assert isPalindrome( LinkedList( [1,2,1] ) ) == True
	assert isPalindrome( LinkedList( [1,2,2,1] ) ) == True
	assert isPalindrome( LinkedList( [1,3,2,1] ) ) == False
	assert isPalindrome( LinkedList( [1,2,2,3] ) ) == False
	print('q6.py: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q6()

