'''
TODO:
	Sanity check if list enfolds on self.
		If a node is a reference back to a prior node in the list,
		we will have endless loops

'''

class LinkedListNode:
	def __init__(self, value, nextNode=None, prevNode=None):
		self.value	= value
		self.next 	= nextNode
		self.prev	= prevNode
	def __eq__(self, other):
		return self.value == other.value
	def __str__(self):
		return str(self.value)
	def skipNextNode(self):
		#Used in q1
		if self.next:
			self.next = self.next.next
	def skipPrevNode(self):
		#Used in q1
		if self.prev:
			self.prev = self.prev.prev

class LinkedList:
	def __init__(self, values=None):
		self.head	= None
		self.tail	= None
		if values is not None:
			self.append(values)
	def __eq__(self, other):
		if self:
			sValues = [x for x in self]
		else:
			sValues = None
		if other:
			oValues = [y for y in other]
		else:
			oValues = None
		return sValues == oValues
	def __iter__(self):
		current = self.head
		while current:
			yield current
			current = current.next
	def __len__(self):
		res = 0
		node = self.head
		while node:
			res += 1
			node = node.next
		return res
	def __str__(self):
		values = []
		if not self.head:
			return ''
		h = self.head
		c = h.next
		values.append(str(h))
		while c and c is not h:
			values.append(str(c))
			c = c.next
		if self.isCircular():
			values.append('...') #Represent infinite
		return ' -> '.join(values)
	def append(self, value=None):
		if value is None:
			raise ValueError('ERROR: LinkedList.py: append() `value` PARAMETER MISSING')
		if isinstance(value, list):
			for v in value:
				self.append(v)
			return
		elif self.head is None:
			self.head	= LinkedListNode(value)
			self.tail	= self.head
		else:
			''' We have existing nodes  '''
			''' Head.next is same '''
			''' Tail is new node '''
			self.tail.next	= LinkedListNode(value, None, self.tail)
			self.tail		= self.tail.next
			if self.head.next is None:
				self.head.next = self.tail.prev
		return self.tail
	def get(self, k, last=-1):
		#q2.py
		current = self.head
		cnt = 0
		if last != -1:
			return self.getFromIndices(k, last)
		while current:
			if k == cnt:
				return current 
			current = current.next
			cnt += 1
		raise ValueError("ERROR: INDEXING LinkedList() OUT OF BOUNDS AT `"+str(k)+"`")
	def getFromIndices(self, k, last=-1):
		#q2.py
		ret = LinkedList()
		cnt = 0
		current = self.head
		while current:
			if k <= cnt:
				if last >=cnt or last==-1:
					ret.append(current.value)
			current = current.next
			cnt += 1
		if ret.head is None:
			raise ValueError("ERROR:getFromIndices():INDEXING LinkedList() OUT OF BOUNDS AT `"+str(k)+"`")
		return ret
	def isCircular(self):
		if self.head is None:
			return True #Nothing is circular, right?
		elif self.head.next is None:
			return False
		if self.tail.next and self.tail.next is self.head:
			return True
		fast = slow = self.head
		fast = fast.next.next
		slow = slow.next
		while fast and fast.next:
			if fast is slow:
				return True
			fast = fast.next.next
			slow = slow.next
		return False
	def push(self, value=None):
		'''Push new node with `value` to LinkedList head '''
		if value is None:
			raise ValueError('ERROR: LinkedList.py: push() `value` PARAMETER MISSING')
		if isinstance(value, list):
			for v in value:
				self.push(v)
			return
		if self.head is None:
			self.tail = LinkedListNode(value)
			self.head = self.tail
		else:
			''' We have existing nodes  '''
			''' Head.prev is new node '''
			''' Tail is same '''
			self.head.prev = LinkedListNode(value, self.head, None)
			self.head = self.head.prev
			if self.tail.prev is None:
				self.tail.prev = self.head.next
		return self.head

	def remove(self, k):
		''' Remove node at k index '''
		cur = self.head
		cnt = 0
		while cur:
			if cnt == k:
				#Found our node, going to remove reference to it
				if cur == self.head:
					self.head = self.head.next
					if self.head and self.head.prev:
						self.head.prev	= None
				elif cur == self.tail:
					self.tail = self.tail.prev
					if self.tail and self.tail.next:
						self.tail.next	= None
				else:
					cur.prev.next = cur.next
					cur.next.prev = cur.prev
				return cur
			cur = cur.next
			cnt +=1
		raise ValueError("ERROR: LinkedList() OUT OF BOUNDS AT remove(" + str(k) + ")")
