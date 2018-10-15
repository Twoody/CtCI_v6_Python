'''
	Q1.4: Palindrome Permutation
		Given a string, write a function to check if it is a
		palindrome. A palindrome is a word or phrase that is the same
		forwards and backwards. A permutation is a rearrangement of
		letters. The palindrome does not need to be limited to just
		dictionary words.

	Example:
		i: acot coa
		o: True --> "taco cat"

		i: foo bar
		o: False

	Thoughts:
		Ascii? Unicode?
		We can just check if each character exists.
		An input is not true if there exists more than 1 char
		with an odd amount of occurrences. See `foo bar` above and `f` `b`
		being odd occurrences.

		A more complex route would be to sort the string, and set a flag 
		for finding an odd amount of chars while going through it.
		If the flag goes off twice, we fail.
		This would take O(n logn) time to sort then iterate.

		A cool approach is to make a bit vectore of the possible number
		of choices. Say our choices lied in the alphabet, then our 
		choices would be a bit vector of:
			00000000000000000000000000
		And if we find an `a`:
			10000000000000000000000000
		And if we find an `y`:
			10000000000000000000000010
		So on and so forth.
		Then, we just go through the bit vector, looking for multiple `1`s.
		Or, we can do fancy math and have:
			Let b = our accumulated bit vector.
			Let c = b-1
			Then 0 = b&c implies only one `1`
			And 1 = b&c implies more than one `1`
'''

def isPalindromePerm(_input):
	'''O(n) runtime'''
	_input = _input.replace(" ", "")
	htbl = {}
	hasOdd = False
	for i in range(0, len(_input)):
		char = _input[i]
		if char in htbl:
			htbl[char] += 1
		else:
			htbl[char] = 1
	for key in htbl:
		val = htbl[key]
		if val%2==1:
			if hasOdd==False:
				hasOdd = True
			else:
				return False
	return True

def q4():
	assert isPalindromePerm("oof") == True
	assert isPalindromePerm("aboofr") == False
	assert isPalindromePerm("taco cat") == True
	print("PASSED ALL TESTS FOR Q4")

if __name__ == "__main__":
	q4()
