class Node:
	''' Node exists for stack only '''
	''' Stack is LIFO, so no `next` needed '''
	''' `tag` is our pointer '''
	def __init__(self, value, prev=None, tag=None):
		self.value = value
		self.prev  = prev
		self.tag   = 0
		if tag is None and prev is not None:
			self.tag = prev.tag +1
	def __str__(self):
		return str(self.value)
	def __eq__(self, other):
		return self.value == other.value
	def __len__(self):
		v   = self.value
		cnt = 0
		if isinstance(v, str):
			v = list(v)
		if isinstance(v, list) or isinstance(v, dict):
			cnt = 0
			while x in v:
				cnt += 1
		elif v is None:
			cnt = 0
		else:
			cnt = 1 #Probably an int or float
		return cnt

class MultiStack:
	''' Array of three stacks '''
	''' When one stack is full, move to next stack '''
	''' Use self.tail as pointer '''
	def __init__(self,value=None, stacksize=10):
		self.numberOfStacks = 3
		self.array          = [None] * self.numberOfStacks
		self.stacksize      = stacksize
		self.tail           = None
		self.maxtag         = self.numberOfStacks * stacksize -1
		for i in range(0, self.numberOfStacks):
			self.array[i] = [None] * stacksize
		if value:
			self.append(value)
	def __eq__(self, other):
		sValues = []
		oValues = []
		if self.numberOfStacks != other.numberOfStacks:
			return False
		for s in self.array:
			for e in s:
				sValues.append(e)
		for s in other.array:
			for e in s:
				oValues.append(e)
		return sValues == oValues
	def __iter__(self):
		c = self.tail
		while c:
			yield c
			c = c.tail.prev
	def __str__(self):
		s = ''
		#t = self.tail
		values = [str(t.value) for t in self]
		'''
		values = []
		while t:
			values.insert(0, str(t.value))
			t = t.prev
		'''
		return ' -> '.join(values)
	def append(self, value):
		if value is None:
			raise ValueError('ERROR: NO ARGUMENT PASSED FOR `append()`')
		if isinstance(value, list):
			for x in value:
				self.append(x)
		else:
			if self.tail is None:
				self.tail = Node(value)
			elif self.tail.tag == maxtag:
				self.tail = Node(value, self.tail, 0)
			else:
				self.tail = Node(value, self.tail, self.tail.tag+1)
		curstack = self.getCurStack()
		curtag   = self.tail.tag
		self.array[curstack][curtag] = self.tail
		return self.tail
	def getCurStack(self):
		return self.tail.tag // self.stacksize
	def isempty(self, stacknum):
		a = self.array[stacknum]
		for e in a:
			if e is not None:
				return False
		return True
	def isfull(self,stacknum):
		a = self.array[stacknum]
		for e in a:
			if e is None:
				return False
		return True
	def peek(self, stacknum):
		return str(self.array[stacknum][0])
	def pop(self, args={}):
		returnnode = False
		if args:
			if args['returnnode']:
				returnnode = True
		n = self.tail
		self.tail = self.tail.prev
		self.tail
		if returnnode:
			return n
		else:
			return n.value
	
