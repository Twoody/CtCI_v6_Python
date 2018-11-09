def mergeTwo(arr1, arr2, args=None):
	returntuple = False
	if args is None:
		args = {}
	if 'returntuple' in args and args['returntuple'] == True:
		returntuple = True
	''' Assuming arr1 and arr2 are sorted at this point '''
	if arr1 is None:
		if arr2 is None:
			return []
		return arr2
	if arr2 is None:
		return arr1
	n = len(arr1)
	m = len(arr2)
	for i in range(0, n):
		if arr1[i] > arr2[0]:
			#Swap current arr1 node and head of arr2
			tmp = arr1[i]
			arr1[i] = arr2[0]
			arr2[0] = tmp
			for j in range(0, m-1):
				#Allocate the new head within arr2
				if arr2[j] > arr2[j+1]:
					tmp = arr2[j]
					arr2[j] = arr2[j+1]
					arr2[j+1] = tmp
				else:
					break
	if returntuple == True:
		return (arr1, arr2)
	return arr1 + arr2
def mergesort(arr):
	if len(arr) <= 1:
		return arr
	midpoint = len(arr) // 2
	lArr     = arr[:midpoint]
	rArr     = arr[midpoint:]
	return mergeTwo(mergesort(lArr), mergesort(rArr))

if __name__ == "__main__":
	a = [33,22,12,55, 2, 3,11, 1]
	c = [44,23,55,66,12, 1, 2, 3,4,5]
	b = mergesort(a)
	d = mergesort(c)
	ret = mergeTwo(b,d, {'returntuple':True})
	print(ret[0])
	print(ret[1])
