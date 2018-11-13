'''
	Tanner Woody
	20181112

Purpose:
	heapsort.py is meant to show that a heap is a complete binary tree.
	heapsort.py is meant to display Heap usage to sort an array

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
	def details(self):
		ret = str(self.value) +':\n'
		ret += '\tparent:\t'    + str(self.parent) +'\n'
		ret += '\tleft:\t'      + str(self.left) +'\n'
		ret += '\tright:\t'     + str(self.right) +'\n'
		return ret
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
		#O(shiftTail) + O(heapify) + O(c) --> O(3 * binLog(n))
		if isinstance(value, list):
			for v in value:
				self.add(v)
			return self.tail
		self.size += 1
		if self.head is None:
			self.head = Node(value)
			self.tail = self.head
			return self.tail
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
		#O( binLog(n) )
		#Traverse up `n` heapifying along the way
		cur = n.parent
		while cur is not None:
			if n.value > cur.value:
				#swap nodes and do not lose track of n.value
				self.swap(n, cur)
				n = cur
			cur = cur.parent
		return n
	def swap(self, n1, n2):
		#Swap node1 and node2
		t = n1.value
		n1.value = n2.value
		n2.value = t
		return True
	def shiftTail(self):
		#O(2 * binLog(n))
		ns       = self.size+1  #(n)ext (s)size
		c        = self.head    #cur node
		r        = []				#Route to traverse from head
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

def merge(a1, a2):
	if a1 == []:
		return a2
	if a2 == []:
		return a1
	n = len(a1)
	m = len(a2)
	for i in range(0, n):
		if a1[i] > a2[0]:
			t     = a1[i]
			a1[i] = a2[0]
			a2[0] = t
			for j in range(0, m-1):
				if a2[j] > a2[j+1]:
					t       = a2[j]
					a2[j]   = a2[j+1]
					a2[j+1] = t
				else:
					break
	return a1 + a2
def mergesort(arr):
	if len(arr) <= 1:
		return arr
	mp = len(arr) //2
	r  = arr[mp:]
	l  = arr[:mp]
	return merge( mergesort(l), mergesort(r) )


if __name__ == "__main__":
	from random import randint
	unsorted = []
	srtd     = []
	size     = 9999
	for i in range(0, size):
		unsorted.append( randint(0, size) )
	while unsorted != []:
		h        = Heap(unsorted)
		unsorted = h.toArr()
		srtd.insert(0, unsorted[0])
		unsorted.pop(0)
	print(srtd)
	'''
	srtd = mergesort(unsorted)
	print(srtd)
	'''
	'''
	per 9999 items and 0,999 random integers:
		MergeSort:
			real	0m8.628s
			user	0m8.575s
			sys	0m0.026s
		Heapsort:
			real	0m3.018s
			user	0m2.976s
			sys	0m0.028s
	
	'''

