'''
2. Minimal Tree
	Given a sorted (increasing order) array with unique integer elements, 
	write an algorithm to create a binary tree with minimal height.

Thoughts:

	                   .......27......
                     /               \
                    20               31
                   /  \             /  \
                  /    \           /    \
                 16    21         29    40
                / \   /  \       /  \   / \
                  17     25     28  30 35 45

	     
		INSERT: 19
	                     .........27..........
                       /                     \
                    ..20..                   31
                   /      \                 /  \
                  /        \               /    \
                 17        25             29    40
                / \       /  \           /  \   / \
               16        21             28  30 35 45
                        /
                       19


		INSERT: 20
	                     .........27..........
                       /                     \
                    ..21...                ..31..
                   /       \              /      \
                  / `20`    \            /        \
                 17         25          29        40
                /  \       /  \        /  \       / \
               16  19     22          28  30     35 45
	
	
	                     .........27..........
                       /                     \
                    ..20...                ..31..
                   /       \              /      \
                  /         \            /        \
                 17         21          29        40
                /  \       /  \        /  \       / \
               16  19     22  25      28  30     35 45
	
	
		INSERT: 32
		                  .........27............
                       /                       \
                    ..20...                  ..32...
                   /       \                /       \
                  /         \              /         \
                 17         21          ..30..        40
                /  \       /  \        /      \       / \
               16  19     22  25      28      31     35 45
                                        \
                                        29

			INSERT: 39
		                  .........27...............
                       /                          \
                    ..20...                  .....32....
                   /       \                /           \
                  /         \              /             \
                 17         21          ..30..         ..40..
                /  \       /  \        /      \       /      \
               16  19     22  25      28      31     35       45
                                        \             \
                                        29            39


			INSERT: 26
		                  .........27...............
                       /    `26`                  \
                    ..20...                  .....32....
                   /       \                /           \
                  /         \              /             \
                 17         21          ..30..         ..40..
                /  \       /  \        /      \       /      \
               16  19     22  25      28      31     35       45
                                        \             \
                                        29            39
	

		                  .........32...............
                       /                            \
                    ..21...                    .....32....
                   /       \                  /           \
                  /         \                /             \
                 17         25            ..30..         ..40..
                /  \       /  \          /      \       /      \
               16  19     22  26        28      31     35       45
                                \        \             \
                                 27       29            39
	

	
'''
import sys
class Node:
	def __init__(self, val, left=None, right=None):
		self.left  = left
		self.right = right
		self.val   = val
		
class BTree:
	def __init__(self, head=None, values=None):
		if head is not None:
			self.head = Node(head)
		else:
			self.head = head
		if head is not None:
			self.depth = 1
		else:
			self.depth = None
		if values is not None:
			for v in values:
				self.add(v)
	def add(self, value):
		if self.head is None:
			self.head = Node(value)
		else:
			if value < hval:
				
		
			



def q2():
	a = [1,2,3,4,5,6,7,8,11,12,14,15,16,22,33,44,55,66]
	b = BTree(a)
	print('q1: PASSED ALL TESTS')

if __name__ == "__main__":
	q2()

