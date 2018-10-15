Tanner 20180919

Covers:
	Hash Tables
		Def:
			Data structure that maps keys to values for highly 
			efficient lookup.
			In python, this is a dic.
		Warnings:
			Collisions...
			Make sure to store key value pairs as key array of pairs
			to avoid collisions if similar hash.
		Runtime:
			Lookups are considered O(1)
			Worst case is O(n) where one hash stores array of all
			elements.
	ArrayList and Resiable Arrays
		Def:
			Grows as items are appended.
			Considered fixed length.
		Func:
			When array is full, array doubles in size.
			The amortized insertion runtime is still O(1)
				If array is size n, increase size by:
					n/2	//final cap increase
					n/4	//prev cap increase
					n/8	//prev cap increase
					...	//
					2		//second cap increase
					1		//first cap increase
				Therefore, we can do some math tricks to have
				1+2+SUMMATION(1/(2^n)) ~ 1+2+1 
					**See zenos paradox

	String Builder
		Java 7 specific

Q1.1: Is Unique
	Implement an alogirthm to determine if a string has all 
	unique characters.
	Implement a second algorithm if you cannot use data structs.

Q1.2: Check Permutation
	Given two strings, write a method to decide if one is a 
	permutation of the other.

Q1.3: URLify
	Write a method to replace all spaces in a string with %20.
	You may assume that the string has sufficient space at the
	end to hold the additional character, and that you are
	given the `true` length of the string.
	(NOTE: if in java, use a character array to perform in palce)
	Example:
		I: "Mr John Smith    ", 13
		O: "Mr%20John%20Smith"

Q1.4: Palindrome Permutation
	Given a string, write a function to check if it is a
	palindrome. A palindrome is a word or phrase that is the same
	forwards and backwards. A permutation is a rearrangement of
	letters. The palindrome does not need to be limited to just
	dictionary words.

Q1.5: One Away
	There are three types of edits that can be performed on 
	strings:
		insert, remove, replace
	Given two strings, determine if string2 is one edit from
	string1.

Q1.6: String Compression
	Implement a method to perform basic string compression
	using the counts of repeated characters. For exmaple, the 
	string `aabcccccaaa` would become `a2b1c5a3`. If the 
	compressed string would not become smaller than the original
	string, your method should return the original string.

Q1.7: Rotate Matrix
	Given an image represented by an NxN matrix, where each
	pixel in the image is 4 bytes, write a method to rotate the
	image by 90 degrees. Can you do this in place?
	
Q1.8: Zero Matrix
	Write an algorithm such that if an element in an MxN matrix
	is 0, its entrie row and column are set to zero.

Q1.9: String Rotation
	Assume you have a method `isSubstring` which check if one
	word is a substring of another. Given two strings, `s1` and
	`s2`, write code to check if `s2` is a rotation of `s1`
	using only on call to isSubstring.
	For example: `waterbottle` is a rotation of `erbottlewat`
