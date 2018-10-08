Questions:
	1. Remove Dups
			Write code to remove duplicates from an unsorted linked list.
			Follow up:
				How would you solve the probem if a temporary buffer is 
				not allowed?

	2. Reurn Kth to Last
			Implement an algorithm to find the kth to last element of a 
			singly linked list.
			Hint:
				#8, #25, #41, #67, #126

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

	6. Palindrome
			Implement a function to check if a linked list is a palindrome.
			Hints:
				5, 13, 29, 61, 101

	7. Intersection
			Given two singly linked lists, determine if the two lists 
			intersect.
			Return the intersecting node.
			Note that the intersection is defined based on reference, not
			value.
			That is, if the kth node of the first ilnked list is the exact
			same node (by reference) as the jth node of the second linked
			list, then they are intersecting

	8. Loop Detections:
			Given a circular libked list, implement an algorithm that returns
			the node at the `beginning` of the loop.
			Definitions:
				Circular linked list is a "corrupt" linked list in which
				a nodes next pointer points to an earlier node, so as to make
				a loop in the linked list.
			Example:
				I: A->B->C->D->E->C (The same as C earlier)
				O: C
			Hints:
				50, 69, 83, 90

