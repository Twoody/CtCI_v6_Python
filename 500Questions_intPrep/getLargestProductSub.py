def getMaximumProductSubarray_V2(arr):
	minIndex = 1
	maxIndex = 1
	maxSoFar = 1
	for i in arr:
		temp     = maxIndex
		maxIndex = max(i, max(i*maxIndex, i*minIndex))
		minIndex = min(i, min(i*temp, i*minIndex))
		maxSoFar = max(maxIndex, minIndex)
	return maxSoFar

def getMaximumProductSubarray_V1(arr):
	#O(n^2) time
	#There should be a faster way...
	curcProduct = 1
	currArr     = []
	largestArr  = []
	largestProd = 0
	for i in range(0, len(arr)):
		currProduct = arr[i]
		currArr = [arr[i]]
		for j in range(i+1, len(arr)):
			currProduct = currProduct * arr[j]
			currArr.append(arr[j])
			if currProduct > largestProd:
				largestArr = currArr.copy()
				largestProd = currProduct
	return (largestArr, largestProd)


if __name__ == "__main__":
	arr = [1,2,3,4,5,0,9,9]
	maxProd = getMaximumProductSubarray_V1(arr)
	print(maxProd[0])
	maxProd = getMaximumProductSubarray_V2(arr)
	print(maxProd)

