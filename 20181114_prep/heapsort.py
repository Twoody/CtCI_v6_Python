class MaxHeap:
	def __init__(self, items=[]):
		super().__init__()
		self.heap = []
		self.size = 0
		for item in items:
			self.append(item)
	def append(self, item):
		if isinstance(item, list):
			for i in items:
				ret = self.append(item)
			return ret
		self.heap.append(item)
		self.size += 1
		self.__bubbleUp(self.size-1)
		return item
	def getParentIndex(self, i):
		#From i, get the index of it's parent in a heap
		pIndex = i
		if i == 0:
			return None
		if i%2 == 1:
			pIndex -= 1 #right child
		return  pIndex//2
	def getChildrenIndices(self, i):
		l = i*2
		r = l +1
		c = []
		if l < self.size:
			c.append(l)
		if r < self.size:
			c.append(r)
		return c
	def pop(self):
		#Remove and return head; Re-Heapify after removed;
		m = self.heap[0]
		self.__swap(0, self.size-1)
		self.heap.pop()
		self.size -= 1
		if self.size > 1:
			self.__bubbleDown(0)
		return m
	def getSequence(self):
		#Get summation(2**i) arr for newline placement
		cur  = 0
		i    = 1
		a    = []
		while cur <= self.size:
			a.append(cur)
			cur += pow(2,i)
			i += 1
		return a
	def prettyprint(self):
		seq = self.getSequence()
		s   = ''
		for i in range(0, self.size):
			el = self.heap[i]
			s += str(el) + ' '
			if i in seq:
				s+= '\n'
		print(s+'\n')
	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
		return True
	def __bubbleUp(self, index):
		pIndex = self.getParentIndex(index)
		if index < 1:
			return True
		elif self.heap[pIndex] < self.heap[index]:
			self.__swap(index, pIndex)
			return self.__bubbleUp(pIndex)
		else:
			return True
	def __bubbleDown(self, index):
		cIndices = self.getChildrenIndices(index)
		for cIndex in cIndices:
			if self.heap[index] < self.heap[cIndex]:
				self.__swap(index, cIndex)
				self.__bubbleDown(cIndex)
		return True

def heapsort(arr):
	h   = MaxHeap(arr)
	ret = []
	while h.size > 0:
		ret.append(h.pop())
	return ret

def merge(arr1, arr2):
	if arr1 == []:
		return arr2
	if arr2 == []:
		return arr1
	n = len(arr1)
	m = len(arr2)
	for i in range(0, n):
		if arr1[i] < arr2[0]:
			arr2[0], arr1[i] = arr1[i], arr2[0] 				#swap
			for j in range(0, m-1):             				#Reorder arr2, now
				if arr2[j] < arr2[j+1]:
					arr2[j], arr2[j+1] = arr2[j+1], arr2[j] 	#Swap
				else:
					break
	return arr1+arr2
def mergesort(arr):
	#O(n logn); Stable
	if len(arr) <2:
		return arr
	mp = len(arr) //2 #floor
	l = arr[mp:]
	r = arr[:mp]
	return merge( mergesort(l), mergesort(r) )

def quicksort(arr):
	#O(n logn); Not stable
	n = len(arr)
	if n<2:
		return arr
	pivot   = arr[n//2]
	less    = [i for i in arr[1:] if i<=pivot]
	greater = [i for i in arr[1:] if i>pivot]
	return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
	from random import randint

	doHeap   = False
	doMerge  = False
	doQuick  = True

	unsorted = []
	size     = 9999
	for i in range(0, size):
		unsorted.append( randint(0, 10) )

	if doHeap == True:
		srtd = heapsort(unsorted)
	elif doMerge==True:
		srtd = mergesort(unsorted)
	elif doQuick == True:
		srtd = quicksort(unsorted)
	print(srtd)
	'''
	Heap Sort for 9999 size of 0,10 range -->
		real	0m0.578s
		user	0m0.555s
		sys	0m0.014s
	Merge Sort for 9999 size of 0,10 range -->
		real	0m6.889s
		user	0m6.840s
		sys	0m0.024s
	'''


