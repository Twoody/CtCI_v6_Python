def printbanner():
	print("****************************************")
	print("***********  Q2: PASSED TEST  **********")
	print("****************************************")
	print("")
def isPermutationInString(smallS, bigS):
	"""Return the int of start of permutation"""
	"""Else, -1"""
	htbl = {}
	for i in range(0, len(smallS)):
		char = smallS[i]
		if char in htbl:
			htbl[char]+=1
		else:
			htbl[char] = 1
	for i in range(0, len(bigS)):
		char  = bigS[i]
		if char in htbl:
			temptbl = dict(htbl)
			jCeiling = len(smallS)+i
			for j in range(i, jCeiling):
				if bigS[j] not in temptbl:
					#Not a complete permutation
					break
				elif temptbl[bigS[j]] == 0:
					#Ran out of chars; Not perm.
					break
				else:
					temptbl[bigS[j]] -=1

				if j == jCeiling-1:
					#All the way through tbl, with match!
					return i
	return -1

def q2():
	'''
	Q1.2: Check Permutation
		Given two strings, write a method to decide if one is a 
		permutation of the other.

	Thoughts:
		A permutation is any possible arrangement of items.
		First, we should probably work with the smaller string.
		If we go through and find all permutations of that string,
		we can this would take (n)(n-1)(n-2)...(1) runtime.
		This runtime is equivalent of n!
		Let's do better...

		If we put each character in a data structure, 
		we can see if the item exists in the table, 
		The hashtable can be key value pairs of the char, with
		its number of observances. And each time we observe it in
		the second string, we then subtract from the iterations.
		If all iterations in the hashtable are zero, we return true.
		This will take O(n) time for storing in the hash table,
		and then it will take O(m + m-1 + ... + n) , aka Gauss, 
		as its worse rutime. O(n^2+n) + O(n)
		However, depending on the strings, this might be okay...
	'''
	assert isPermutationInString("Foo", "Bar") == -1
	assert isPermutationInString("Foo", "BaooFr") == 2
	bigS   = "wihr no rest"
	assert isPermutationInString('erst', bigS) == 8
	bigS   = "res rest"
	assert isPermutationInString('erst', bigS) == 4
	bigS   = "this is a completely random sentence that I will strip the whitespace from and try to avoid punctuation by creating a very long and verbose run on sentence such that the reader will be dumbfounded by its theft of brevity with no rest"
	assert isPermutationInString('erst', bigS) == 229
	printbanner()

if __name__ == "__main__":
	q2()
