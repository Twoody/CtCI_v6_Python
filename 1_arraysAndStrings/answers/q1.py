def isunique(string):
	'''Is each char in string unique'''
	'''Assuming ASCII not unicode'''

	if len(string) > 128: #only 128 chars in ascii...
		return False
	
	htble = {}
	for i in range(0, len(string)):
		char = string[i]
		if char in htble:
			return False
		else:
			htble[char] = True
	return True

def q1():
	'''
	Q1.1: Is Unique
		Implement an alogirthm to determine if a string has all 
		unique characters.
		Implement a second algorithm if you cannot use data structs.
	
	Thoughts:
		Brute force would be to put each element in a hashtable.
		Look up the element in hash table, if exists, return false
		Else, keep adding to table.

		That is going to take O(n) time.
		The BCR is magically getting the pointer in place on an
		item that is not unique. This seems to have more intuition
		than I can put in a computer.
		The last option would be O(log n)
	'''
	s1 = 'Foo Bar Baz' 	#Is not unique
	s2 = 'Foo'				#Is not unique
	s3 = '' 					#Is unique
	s4 = '1'					#Is unique
	s5 = 'aa'				#Is not unique
	s6 = 'bar'           #Is unique

	assert isunique(s1) == False
	assert isunique(s2) == False
	assert isunique(s5) == False
	assert isunique(s3) == True
	assert isunique(s4) == True
	assert isunique(s6) == True
	print('Q1: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q1()

