def getSequence(h):
	cur  = 0
	i    = 0
	a    = []
	size = len(h)
	while cur <= size:
		a.append(cur)
		cur += pow(2,i)
		i += 1
	return a
def prettyprint(h):
	seq = getSequence(h)
	s   = ''
	for i in range(0, len(h)):
		el = h[i]
		s += str(el) + ' '
		if i in seq:
			s+= '\n'
	print(s)

def getParentIndex(i):
	#From i, get the index of it's parent in a heap
	pIndex = i
	if i == 0:
		return None
	if i%2 == 1:
		pIndex -= 1 #right child
	return  pIndex//2

def swap(a, i, j):
	a[i], a[j] = a[j], a[i]
	return a

def getHeap(a):
	i = len(a)-1
	while i > 0:
		pIndex = getParentIndex(i)
		if pIndex is None:
			continue
		curIndex = i
		while a[pIndex] < a[curIndex]:
			prettyprint(a)
			print('\tChild:  ' + str(a[curIndex]))
			print('\tParent: '+ str(a[pIndex]))
			print()
			a        = swap(a, curIndex, pIndex)
			curIndex = pIndex
			pIndex   = getParentIndex(pIndex)
			if pIndex is None:
				break
		i-=1
	print('DONE\n')
	return a

if __name__ == "__main__":
	#heap sort an array via indice logic
	#Try to treat the array as the heap instead of a new DataStruc.
	a  = [1,4,5,2,213,4,2,1234,4,4,3,2223,21]
	h  = getHeap(a)
	prettyprint(h)

