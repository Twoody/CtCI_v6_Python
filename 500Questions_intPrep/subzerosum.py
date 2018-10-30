'''
Author:
	Tanner Woody
	20181029

Purpose:
	Suppose we have condition1 which is that for each item in an array,
		add the item to a total sum, and return True iff that sum is zero.
	Given an array, find a subarray within that array which meets condition1.
'''

def hasZeroSumSub(arr):
	''' Return true iff sum of a subarray's items == zero '''
	currentsums = {}
	for i in range(0, len(arr)):
		val = arr[i]
		for key in currentsums:
			neededvalue = 0-currentsums[key]
			print('\t' + str(neededvalue))
			if neededvalue == val:
				print( 'ZERO SUM SUB ARRAY FOUND:' )
				print( '\t' + str(arr[key:i+1]) )
				print()
				return True
			currentsums[key] += val
		#We did not find a pair
		#Create a new list of this value for further seeking
		currentsums[i] = val
	print('NO ZERO SUM SUBARRAY FOUND')
	return False

if __name__ == "__main__":
	a = [1,4,3,5,33,60,3,4,5,3,-4,-30,-29,-20, -10, -5, 5]
	assert hasZeroSumSub(a) == True
	assert hasZeroSumSub([1,-1]) == True
	assert hasZeroSumSub([1]) == False
	assert hasZeroSumSub([1,3,-4]) == True


