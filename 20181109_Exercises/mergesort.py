'''
Start Time:
	9:26
Init End Time:
	9:45
Follow-Up:
	The two arrays below are no longer sorted
Follow-Up End Time:
	9:55
Total compilation errors:
	One
Type of compilation errors:
	Greater than instead of less than being used.

Purpose:
	Given two sorted arrays, merge them in place such that arr1 and arr2
	still have the same size, but are now in order as if they were the 
	same array.

Example:
	arr1 = [1,2,3,4,5,6,7]
	arr2 = [1,2,2,2,3,3,4]

	arrTuple = mergeInPlace(arr1. arr2)
	arr1 = arrTuple[0]
	arr2 = arrTuple[1]
	
	asssert arr1 == [1,1,2,2,2,]
	asssert arr1 == []
'''
from math import floor

def mergeInPlace(arr1, arr2, args=None):
	joinArrays = False
	if args is None:
		args = {}
	if 'joinArrays' in args and args['joinArrays'] == True:
		joinArrays = True
	if arr1 == [] or arr2 == []:
		if joinArrays:
			return arr1+arr2
		return (arr1, arr2)
	n = len(arr1)
	m = len(arr2)
	for i in range(0, n):
		if arr1[i] > arr2[0]:
			#Swap arr1[i] and arr2[0]
			tmp 		= arr1[i]
			arr1[i]	= arr2[0]
			arr2[0]	= tmp
			for j in range(0, m-1):
				#Reorder arr2 for the new element
				if arr2[j] > arr2[j+1]:
					tmp			= arr2[j]
					arr2[j]		= arr2[j+1]
					arr2[j+1]	= tmp
				else:
					break
	if joinArrays:
		return arr1+arr2
	return (arr1, arr2)

def mergesort(arr):
	if arr == [] or len(arr)==1:
		return arr
	midpoint = floor(len(arr)/2)
	right    = arr[midpoint:]
	left     = arr[:midpoint]
	return mergeInPlace( mergesort(right), mergesort(left), {'joinArrays':True})
		

if __name__ == "__main__":
	arr1 = [1,2,3,4,5,6,7]
	arr2 = [1,2,2,2,3,3,4]
	arrTuple = mergeInPlace(arr1, arr2)
	arr1 = arrTuple[0]
	arr2 = arrTuple[1]
	assert arr1 == [1,1,2,2,2,2,3]
	assert arr2 == [3,3,4,4,5,6,7]

	arr1 = [7,6,5,4,3,2,1]
	arr2 = [4,3,3,2,2,2,1]
	arr1 = mergesort(arr1)
	arr2 = mergesort(arr2)
	arrTuple = mergeInPlace(arr1, arr2)
	arr1 = arrTuple[0]
	arr2 = arrTuple[1]
	assert arr1 == [1,1,2,2,2,2,3]
	assert arr2 == [3,3,4,4,5,6,7]
