'''
	6. Palindrome
			Implement a function to check if a linked list is a palindrome.
			Hints:
				5, 13, 29, 61, 101

	Thoughts:
		1,1,2,1,1 is palindrome & Odd
		Is 2,1,1,1,1 a palindrome then?
			No, it is not.
		
		We can compare each half of the list.
		IF the list is odd, make sure we skip over the middle man.
		Compare the two halves by building a temp comparison list for half of 
			the provided list.
		Then, for the remained of the provided list's length, compare to the
			last items in the temp comparison list (via pop()).
'''
def isPalindrome(mList):
	compareL = []						#Build list to compare to
	i = 0
	while i < len(mList)//2:		#Only build for 1/2 the list
		compareL.append(mList[i])
		i +=1
	if len(mList)%2 ==1:
		i +=1								#skip over odd middle man
	while i < len(mList):
		compare = compareL.pop()
		if mList[i] != compare:
			return False
		i +=1
	return True
	

def q6():
	assert isPalindrome([]) == True
	assert isPalindrome([1]) == True
	assert isPalindrome([1,2]) == False
	assert isPalindrome([1,2,1]) == True
	assert isPalindrome([1,2,2,1]) == True
	assert isPalindrome([1,2,3,1]) == False
	print('PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q6()

