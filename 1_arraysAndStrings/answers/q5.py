'''
	Q1.5: One Away
		There are three types of edits that can be performed on 
		strings:
			insert, remove, replace
		Given two strings, determine if string2 is one edit from
		string1.

	Thoughts:
		Store string one in htble with value of occurrences.
		Create a flag of didTakeAction.
		Iterate over string two.
		If char from string two not in htbl, didTakeAction is True
		If didTakeAction is True, and a second new character, return False.

		At End of string two, go through htble, counting all remaining
			occurences.
		If didTakeAction is False and htblCount is 1, we removed a char.
		If didTakeAction is True and htbleCount is 1, we replaced a char.
		If didTakeAction is True and htbleCount is 0, we inserted a char.
		If didTakeAction is False and htbleCount is 0, we have the same string.
			--> Check if string is the same at head of function...
		Thus, if htblCount is greater than 1, return false.
		And if htbleCount is zero, check didTakeAction.

		This should run in O(n + m + n) ~ O(n)

		We can optimize by also checking the length of the strings at the head
		of the function too. If the difference is more than 1, return false.

		Example:
			s1 = "foo"
			s2 = "ooo"
			htbl is ['f':1, 'o':2]
			we will then change htbl to ['f':1, 'o': -1]
			Total changes is 0,

		After implementing this, you might see that this is a little hard
		to debug.
		A better attempt might be to stick to single responsibility and
		having a isOneDeleteAway, isOneReplaceAway, and isOneInsertAway
		block of methods.
'''
def isOneDeleteAway(s1, s2):
	didTakeAction	= False
	index1 = 0
	index2 = 0
	while (index1 < len(s1) and index2 < len(s2)):
		char1 = s1[index1]
		char2 = s2[index2]
		if char2 != char1:
			if didTakeAction == True:
				return False
			didTakeAction = True
			index2 += 1
		else:
			index1 += 1
			index2 += 1
	return True

def isOneInsertAway(s1, s2):
	didTakeAction	= False
	index1 = 0
	index2 = 0
	while (index1 < len(s1) and index2 < len(s2)):
		char1 = s1[index1]
		char2 = s2[index2]
		if char2 != char1:
			if didTakeAction == True:
				return False
			didTakeAction = True
			index2 += 1
		else:
			index1 += 1 
			index2 += 1
	return True

def isOneReplaceAway(s1, s2):
	didTakeAction = False
	for i in range(0, len(s1)):
		char1 = s1[i]
		char2 = s2[i]
		if char1 != char2:
			if didTakeAction == True:
				return False
			didTakeAction = True
	return True

def isOneAway(s1, s2):
	'''s1 is original; s2 is new'''
	if s1 == s2:
		return False 					#Same string
	lenDiff = len(s2) - len(s1)

	if lenDiff > 1 or lenDiff < -1:
		return False 					#To many changes
	elif lenDiff == 1:
		return isOneInsertAway(s1, s2)
	elif lenDiff == -1:
		return isOneDeleteAway(s1,s2)
	else:
		return isOneReplaceAway(s1,s2)

def q5():
	assert isOneAway('foo', 'ooo') == True
	assert isOneAway('foo', 'foe') == True
	assert isOneAway('foo', 'fo') == True
	assert isOneAway('', 'o') == True
	assert isOneAway('foo', 'fff') == False
	assert isOneAway('', 'ff') == False
	assert isOneAway('ffff', 'ff') == False
	assert isOneAway('foo', 'foff') == False
	print("PASSED ALL TESTS FOR Q5")


if __name__ == "__main__":
	q5()
