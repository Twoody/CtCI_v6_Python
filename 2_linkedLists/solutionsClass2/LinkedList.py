class Node:
	def __init__(self, __value=None, __next=None, __prev=None):
		self.value = __value
		self.next  = __next
		self.prev  = __prev
	def __eq__(self, other):
		return self.value == other.value
	def __len__(self):
		cnt = 0
		c = self.value
		if isinstance(c, str):
			x = list(c)
			print(x)
			for x in list(c):
				cnt +=1
		elif isinstance(c, list) or isinstance(c, dict):
			for x in c:
				cnt +=1
		else:
			#some kind of float/number
			#just return 1
			cnt = 1
		return cnt
	def __str__(self):
		return str(self.value)

class LinkedList:
	def __init__(self,values=None):
		self.head = None
		self.tail = None
		if values is not None:
			self.append(values)
	def __eq__(self, other):
		if self is other:
			#Covers same list
			return True
		sVals = [x.value for x in self]
		oVals = [y.value for y in other]
		return sVals == oVals
	def __iter__(self):
		c = self.head
		while c:
			yield c
			c = c.next
	def __len__(self):
		cnt = 0
		c = self.head
		while c:
			cnt +=1
			c = c.next
		return cnt
	def __str__(self):
		values = [str(x.value) for x in self]
		if self.isCircular():
			values.append('...') #Represent infinity
		return (' -> ').join(values)
	def append(self, values=None):
		if values is None:
			raise ValueError("ERROR: append(): PARAMETER 0 UNDEFINED")
		if isinstance(values, list):
			for i in values:
				self.append(i)
			return
		if self.head is None:
			self.head = Node(values)
			self.tail = self.head
		else:
			self.tail.next = Node(values, None, self.tail)
			self.tail = self.tail.next
		return self.tail
	def get(self, index):
		''' Return item at index '''
		''' Else, LookUpError() '''
		if self.head is None:
			raise LookupError('ERROR: LinkedList.py: get(): LINKED LIST IS NONE')
		i = 0
		c = self.head
		while c:
			if i == index:
				return c
			i +=1
			c = c.next
		raise LookupError('ERROR: LinkedLisjt.py: get(): INDEX OUT OF RANGE')
	def isCircular(self):
		if self.head is None:
			return False
		if self.tail.next and self.tail.next is self.head:
			#A straight forward circular linkedlist
			return True
		if self.head.next is None or self.head.next.next is None:
			#Not enough nodes to be circular
			return False
		#fast and slow runner
		f = self.head
		s = self.head
		s = s.next
		f = f.next.next
		while f and f.next:
			if s is f:
				return True
			s = s.next
			f = f.next.next
		return False
	def remove(self, index):
		if self.head is None:
			raise LookupError('ERROR: LinkedList.py: remove(): LINKED LIST IS NONE')
		i = 0
		c = self.head
		while c:
			if i == index:
				#Remove this Node
				if c is self.head:
					self.head = self.head.next
					self.head.prev = None
				elif c is self.tail:
					self.tail = self.tail.prev
					if self.isCircular():
						self.tail.next = self.head
					else:
						self.tail.next = None
				else:
					c.prev.next = c.next
					c.next.prev = c.prev
				return c
			i +=1
			c = c.next
		raise LookupError('ERROR: LinkedList.py:remove(): INDEX OUT OF RANGE')
