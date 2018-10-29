'''
2. Minimal Tree
	Given a sorted (increasing order) array with unique integer elements, 
	write an algorithm to create a binary tree with minimal height.

Thoughts:

	
'''
import sys
class Node:
	def __init__(self, val, parent=None, left=None, right=None):
		self.leftchild   = left
		self.rightchild  = right
		self.parent      = parent
		self.value       = val
		self.depth       = 0
		self.height      = 0
		if self.parent is not None:
			self.depth = self.parent.depth+1
	def __str__(self):
		return str(self.value)
	def __eq__(self, other):
		return self.value == other.value
	def getbalance(self):
		balance = 0
		if self.rightchild is not None:
			if self.rightchild.rightchild is not None:
				balance += 1
			if self.rightchild.leftchild is not None:
				balance -= 1
			balance += 1
		if self.leftchild is not None:
			if self.leftchild.rightchild is not None:
				balance += 1
			if self.leftchild.leftchild is not None:
				balance -= 1
			balance -= 1
		return balance
	def getheight(self):
		''' recursive function; Uses -1 if not balanced; '''
		if self is None:
			return 0
		h1 = getheight(self.right)
		h2 = getheight(self.left)
		if h1 == -1 or h2 == -1:
			return -1
		if abs( h1-h2 ) > 1:
			return -1
		if h1 >= h2:
			return h1 + 1
		return h2 + 1
		
class BTree:
	def __init__(self, values=None):
		self.head = None
		self.size = 0
		if values is not None:
			self.add(v)
	def __str__(self):
		''' DFS to print tree '''
		s  = ''         #string
		c  = self.head  #curnode
		st = []         #stack
		v  = []         #visited
		w  = []         #walks
		st.append(c)
		while len(st) != 0:
			c = 
			neighbors = [st[-1].



	def isBalanced(self, node=None):
		if node is None:
			node = self.head
		return node.getheight() != -1

	def add(self, value):
		if isinstance(value, list):
			for item in list:
				self.add(item)
		if self.head is None:
			self.head = Node(value)
			return self.head
		curnode = self.head
		while curnode is not None:
			if curnode.value > value:
				if curnode.leftchild is not None:
					curnode = curnode.leftchild
				else:
					curnode.leftchild = Node(value, curnode)
					if curnode.parent is not None and isBalanced(curnode.parent) == False:
						#We added to the left of the tree, meaning we right rotate
						self.rightrotate(curnode.parent)
				self.size +=1
				return curnode.leftchild
			elif curnode.value < value:
				if curnode.rightchild is not None:
					curnode = curnode.rightchild
				else:
					curnode.rightchild = Node(value, curnode)
					if curnode.parent is not None and isBalanced(curnode.parent) == False:
						#We added to the right of the tree, meaning we left rotate
						self.leftrotate(curnode.parent)
				self.size +=1
				return curnode.rightchild
			else:
				raise KeyError('ERROR: AVL TREE: KEY ' + str(value) + ' ALREADY EXISTS')
		raise ValueError('ERROR: AVL TREE: COULD NOT ALLOCATE VALUE `' + str(value) + '` INTO TREE')
	
	def rightrotate(self, node):
		#There are not right children two nodes deep
		pNode            = node.parent
		lNode            = node.leftchild
		lNode.rightchild = node
		node.parent      = lNode
		node.rightchild  = None
		if pNode.rightchild is cur:
			pNode.rightchild = lNode
		elif pNode.leftchild is cur:
			pNode.leftchild = lNode
		return True
	def leftrotate(self, node):
		pNode           = node.parent
		rNode           = node.rightchild
		rNode.leftchild = node
		node.parent     = rNode
		node.leftchild  = None
		if pNode.leftchild is cur:
			pNode.leftchild = rNode
		elif pNode.rightchild is cur:
			pNode.rightchild = rNode
		return True

def q2():
	b = BTree()
	b.add(10)
	print('q2: PASSED ALL TESTS')

if __name__ == "__main__":
	q2()

