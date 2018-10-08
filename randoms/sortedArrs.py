'''
	Tanner 201809

	Question:
		Given two sorted arrays, find the number of elements in common.

	Thoughts:
		The brute force way would be O(n^2).
		The second method would be doing binary search on elements
		Binary search would run in O(nLogn) time.
		The choice recommended in the book is to put all of the items in
			one array into a hashtable, with lookup time O(1).
		If we used a hashtable, we would have to go through arr1
			at O(m) time, Then we would still have to look each item,
			in the other array, taking a new total of O(n*m)...
		The book says this should be O(n)...
		It is in face O(2n) ~ O(n)
		The runtime is O(n + n), not O(n * n)

	Status:
		Complete
'''
import random
def printbanner():
	print("****************************************")
	print("****************************************")
	print("")

def getInCommon(arr1, arr2):
	'''With arr1 and arr2 of equal size and sorted'''
	'''Return list of items that are in common'''
	ret  = []
	htbl = {}
	for i in range(0, len(arr1)):
		htbl[str(arr1[i])] = True
	for i in range(0, len(arr2)):
		if str(arr2[i]) in htbl:
			ret.append(arr2[i])
	return ret

def main():
	#Run test example of two sorted arrays
	arr1 = [0,1] #Will do fib squence
	arr2 = [0,1] #Will do randoms in range
	for i in range(0,98):
		num1 = arr1[i] + arr1[i+1]
		num2 = random.randint(arr2[i+1]+1, arr2[i+1]+10)
		arr1.append(num1)
		arr2.append(num2)
	incommons = getInCommon(arr1, arr2)

	printbanner()
	for j in incommons:
		print ('\t' + str(j))

	printbanner()
	print (", ".join(str(x) for x in arr1))
	printbanner()
	print (", ".join(str(x) for x in arr2))
		

if __name__ == "__main__":
	main()
