
def mergesort(arr1, arr2):
	''' return tuple of same length arr1 and arr2 but sorted between the two '''
	n = len(arr1)
	m = len(arr2)
	for i in range(0, n):
		if arr1[i] > arr2[0]:
			tmp = arr1[i]
			arr1[i] = arr2[0]
			arr2[0] = tmp
			
			for j in range(0, m-1):
				if arr2[j+1] < arr2[j]:
					tmp       = arr2[j+1]
					arr2[j+1] = arr2[j]
					arr2[j]   = tmp
				else:
					continue
	print(arr1)
	print(arr2)
	return (arr1, arr2)


if __name__ == "__main__":
	arr1 = [1,2]
	arr2 = [3,4]
	tup = mergesort(arr1, arr2)
	arr1 = tup[0]
	arr2 = tup[1]
	assert arr1 == [1,2]
	assert arr2 == [3,4]
	
	arr1 = [1,3]
	arr2 = [2,4]
	tup = mergesort(arr1, arr2)
	arr1 = tup[0]
	arr2 = tup[1]
	assert arr1 == [1,2]
	assert arr2 == [3,4]
	
	arr1 = [22,33,44]
	arr2 = [12,23,56]
	tup = mergesort(arr1, arr2)
	arr1 = tup[0]
	arr2 = tup[1]
	assert arr1 == [12,22,23]
	assert arr2 == [33,44,56]
