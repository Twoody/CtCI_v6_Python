'''
	Tanner Woody
	20181112

Purpose:
	heapify.py is meant to show that a heap is a complete binary tree.
	heapify.py is meant to teach what a heap is, and lead to a heap sort.

Core Principals on Heaps:
	1. Heap must be Complete Binary Tree (CBT)
	2. Heap weight must be greater than weight of any child
'''
class Node:
	def __init__(self, value, parent=None, right=None, left=None):
		self.value  = value
		self.parent = parent
		self.right  = right
		self.left   = left
	def __str__(self):
		return str(self.value)
class Heap:
	def __init__(self, values=None):
		self.head = None
		self.tail = None
		self.size = 0
		if values is not None:
			self.add(values)
	def __str__(self):
		l   = self.toArr()
		seq = self.getSequence()
		i   = 0
		ret = ''
		for n in l:
			if i in seq and i != 0:
				#New level, print newline
				ret += '\n'
			ret += str(n) + ' '
			i += 1
		return ret
	def getSequence(self):
		cur = 0
		i   = 0
		a   = []
		while cur <= self.size:
			a.append(cur)
			cur += pow(2,i)
			i += 1
		return a
	def toArr(self):
		#BFS to convert heap to array
		a = []
		c = self.head
		s = [c] #stack to visit
		while s != []:
			c = s.pop(0)
			a.append(c.value)
			if c.left:
				s.append(c.left)
			if c.right:
				s.append(c.right)
		return a
	def add(self, value):
		if isinstance(value, list):
			for v in value:
				self.add(v)
			return self.tail
		self.size += 1
		if self.head is None:
			self.head = Node(value)
			self.tail = self.head
			return self.tail
		print(self.toArr())
		t = self.tail
		n = Node(value, self.tail)
		if t.left is None:
			#Keep the tail the same
			t.left = n
		elif t.right is not None:
			raise TypeError('ERROR: HEAP IS NOT A COMPLETE BINARY TREE AND NEEDS BALANCED: ')
		else:
			#Will need to shift tail
			t.right = n
			t = self.shiftTail()
		#Lastly, we need to see if we need to heapify the array...
		#This is only necessary in heapsort, and could be omitted if building a heap from scratch...
		suc = self.heapify(n)
		return self.tail
	def heapify(self, n):
		#Traverse up `n` heapifying along the way
		cur = n.parent
		while cur is not None:
			print(cur)
			if n.value > cur.value:
				#swap nodes
				self.swap(n, cur)
			cur = cur.parent
		return n
	def swap(self, n1, n2):
		#Swap node1 and node2
		t = n1
		if self.head is n1:
			self.head = n2
		n1.parent = n2.parent
		n1.right  = n2.right
		n1.left   = n2.left
		n1.value  = n2.value
		n2.parent = t.parent
		n2.right  = t.right
		n2.left   = t.left
		n2.value  = t.value
		return True
	def shiftTail(self):
		#Build route to tail via current size
		#If size is odd, it is right child
		#If size is even, it is left child
		ns       = self.size+1  #(n)ext (s)size
		c        = self.head    #cur node
		r        = []
		didFirst = False        #Flag for skipping bottom layer
		while ns > 1:
			if ns%2 == 0:
				ns = ns/2
				if didFirst == True: 
					r.insert(0, 'l')
				else:
					didFirst = True
			else:
				ns = (ns-1)/2
				if didFirst == True: 
					r.insert(0, 'r')
				else:
					didFirst = True
		for d in r:
			if d == 'r':
				c = c.right
			elif d == 'l':
				c = c.left
			else:
				raise OSError('NEVER SHOULD HAPPEN')
		self.tail = c
		return self.tail

if __name__ == "__main__":
	h  = Heap([33])
	assert h.size == 1
	assert str(h) == '33 '

	h = Heap([33, 22])
	assert h.size == 2
	assert str(h) == '33 \n22 '

	h = Heap([33, 22,11])
	assert h.size == 3
	assert str(h) == '33 \n22 11 '

	h = Heap([33, 22,11,10])
	assert h.size == 4
	assert str(h) == '33 \n22 11 \n10 '

	h = Heap([33, 22,11,10,9,8,7,6,5,4])
	assert h.size == 10
	assert str(h) == '33 \n22 11 \n10 9 8 7 \n6 5 4 '

	h = Heap([33, 22,11,10,9,8,7,6,5,4,3,2])
	assert h.size == 12
	assert str(h) == '33 \n22 11 \n10 9 8 7 \n6 5 4 3 2 '

	h = Heap([33, 22,11,10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3])
	assert h.size == 17
	assert str(h) == '33 \n22 11 \n10 9 8 7 \n6 5 4 3 2 1 0 -1 \n-2 -3 '
	h = Heap([1,2])
	print(h)

	h = Heap([1,2,3,4,5,6,7,8])
	print(h)
