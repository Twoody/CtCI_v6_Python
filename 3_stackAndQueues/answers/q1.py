'''
1. Three in One
	Describe how you could use a single array to implement three stacks.
	Hints:
		2, 12, 38, 58

Thoughts:
	A single stack requires a LIFO principal and pointer.
	We can adjust the data from the three stacks to be on a modular cycle.
	This approach would allocate appending and popping based off of mod
	groups 0, 1, and 2 being in the modular group 3.

	The other approach is to have an `isStackFull` flag.
	If stack0.isStackFull -> if stack1.isStackFull -> if stack2.isStackFull
		push to appropriate stack
		We might cycle back through to stack0 if stack2 is full, too.
	
	To implement the stack, we will want to make a circular LinkedList.
	Furthermore, we can have a circular Linked List of those circular
	Linked list.
	That is:
		[
			[], [], ..., []
		],
		[
			[], [], ..., []
		],
		[
			[], [], ..., []
		]

	Does our CLL need to be circular in and out?
	Can we utilize the built in python `list` class?
'''
import sys
class Node:
	def __init__(self, value, prev=None, _next=None, tag=0):
		self.value = value
		self.prev = prev
		self.next = _next
		self.tag  = tag
	def __str__(self):
		return str(self.value)
	def __eq__(self, other):
		return self.value == other.value

class Stack:
	def __init__(self, values=[], stacksize=10):
		self.curdex = -1
		self.head   = None
		self.tail   = None
		self.stacksize = stacksize
		cnt = 0
		if values != []:
			self.append(values)
	def __eq__(self, other):
		sValues = [str(i) for i in self]
		oValues = [str(j) for j in other]
		return sValues == oValues
	def __iter__(self):
		''' Start from curdex+1, and work way back to curdex '''
		c = self.head
		i = self.curdex
		if c and c.prev is not None:
			#we are circular
			while c.tag != self.curdex:
				c = c.next
			c = c.next
			while c.tag != self.curdex:
				yield c
				c = c.next
		elif c:
			#Not circular
			while c:
				yield c
				c = c.next
	def __str__(self):
		c = self.head
		values = []
		if c and c.prev is not None:
			#we are circular
			while c.tag != self.curdex:
				c = c.next
			c = c.next
			while c.tag != self.curdex:
				values.append(str(c.value))
				c = c.next
			values.append(str(c.value))
		elif c:
			while c:
				values.append(str(c.value))
				c = c.next
		return ' -> '.join(values)
	def append(self, value):
		self.curdex += 1
		if self.curdex == self.stacksize:
			self.curdex -= self.stacksize
		if isinstance(value, list):
			for i in value:
				self.append(i)
		elif isinstance(value, dict):
			for i in value:
				self.append(value[i])
		elif isinstance(value, tuple):
			for i in value:
				self.append(i)
		else:
			if self.head is None:
				self.head = self.tail = Node(value, None, None, self.curdex)
			elif self.curdex == 0:
				self.head.prev = self.tail
				self.tail.next = self.head
				self.insert(value, self.curdex)
			elif self.head.prev is None:
				#Not circular yet
				self.tail.next = Node(value, self.tail, None, self.curdex)
				self.tail = self.tail.next
			else:
				#Circular, rewrite curdex with new node
				print('MEAT')
				self.insert(value, self.curdex)
		return self.tail
	def insert(self, value, index):
		c = self.head
		while c:
			print(c)
			if c.tag == index:
				c.value = value
				return c
			c = c.next
		return None 

def q1():
	foo = Stack()
	assert foo == Stack([])
	assert str(foo) == ""
	for i in range(0, 10):
		foo.append(i)
	print(foo)
	assert str(foo) == '0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9'
	foo.append(99)
	foo.append(99)
	print(foo)
	#assert str(foo) ==  '99 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9'
	#print( Stack( [1,2,3] ).curdex )
	#print( Stack( [1,2,3] ) )

	print('q1.py: PASSED ALL TESTS')
	print('\tBUT GRADE IS A `C`!!!')
	return True
if __name__ == "__main__":
	q1()

