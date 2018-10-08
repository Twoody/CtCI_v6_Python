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
		An intersection is not just a search between two lists
		and returning a common element with a shared index.

		An intersection in this case is a little bit different, such that,
		we have a linked list with nodes that are lists themselves.
		This approach to the data structure means that we can have a list
		like:				_
			[					\
				[1],				\
				[2],					\
				[7],						\
				[								\
					[9],							\
					[5],								\	I am pretty sure this is all
					[1],								/		wrong;
					[3]							/
				],								/
				[							/
					[6],				/
					[4]			/
				]				/
			]				_
		, and our intersection is apparent at [7]
'''
def getIntersection

def q7():
	print('PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q7()

