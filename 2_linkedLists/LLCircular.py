from LinkedList import LinkedList

class LLCircular(LinkedList):
	def append(self, value=None):
		super(LLCircular, self).append(value)
		self.tail.next = self.head
		self.head.prev = self.tail
	def push(self, values=None):
		super(LLCircular, self).push(values)
		self.tail.next = self.head
		self.head.prev = self.tail
	def remove(self, k):
		super(LLCircular, self).remove(k)
		self.tail.next = self.head
		self.head.prev = self.tail

def tests():
	foo = LinkedList([1,2,3])
	bar = LinkedList([1,2,3])
	foo.tail.next = foo.head		#LL is now CircularLL
	assert foo.isCircular() == True
	assert bar.isCircular() == False

	foo.append(99)
	assert foo.isCircular() == False

	foo = LLCircular([1,2,3])
	assert foo.isCircular() == True
	assert str(foo) == "1 -> 2 -> 3 -> ..."
	foo.append(99)
	assert foo.isCircular() == True
	assert str(foo) == "1 -> 2 -> 3 -> 99 -> ..."
	bar = foo.get(0)
	assert bar is foo.head
	bar = foo.get(56) 		#56%4 == 0
	assert bar is foo.head
	bar = foo.get(55) 		#55%4 == 3
	assert bar is foo.tail
	foo.remove(0)
	assert foo.isCircular() == True
	assert str(foo) == "2 -> 3 -> 99 -> ..."

	print('LLCircular.py: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	tests()

