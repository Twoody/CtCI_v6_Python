import re
def printbanner():
	print("****************************************")
	print("***********  Q3: PASSED TEST  **********")
	print("****************************************")
	print("")

def urlify(_input):
	_input = re.sub(" ", "%20", _input)
	return _input

def q3():
	'''
	Q1.3: URLify
		Write a method to replace all spaces in a string with %20.
		You may assume that the string has sufficient space at the
		end to hold the additional character, and that you are
		given the `true` length of the string.
		(NOTE: if in java, use a character array to perform in palce)
		Example:
			I: "Mr John Smith    ", 13
			O: "Mr%20John%20Smith"

	Thoughts:
		1. Regex!
			A regular expression will run in O(n) but take O(2^m) space (not bad here)
		2. A brute search and replace.
			This will take O(n) again, as we are only looking for the space.
			We can start with a brand new string, and cacatenate to it every
			characater we come accross in the original string.
	'''
	i = "Mr john smith"
	o = urlify(i)
	assert o == "Mr%20john%20smith"
	
	assert urlify("") == ""
	assert urlify(" ") == "%20"
	assert urlify("foo ") == "foo%20"
	assert urlify("  ") == "%20%20"
	printbanner()
if __name__ == "__main__":
	q3()
