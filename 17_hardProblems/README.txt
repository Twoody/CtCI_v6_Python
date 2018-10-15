Questions:

1. Add Without Plus
	Create a funtion that adds without using any operators.

2. Shuffle
	Shuffle a deck of cards via a `shuffle()` method.
	Each of the 52! permutations must be possible.

3. Random SEt
	Write a method to randomly generate a set of m integers from an array of
	size n. Each element must have equally probs of being chosen.

4. Missing Number
	An array A contains all the ints from 0 to n, except for one number.
	Numbers are stored as binary arrays.
	We cannot access the whole number, just single bits.
	Find the missing number as efficiently as possible.

5. Letters and Numbers
	Given an array filled with letters and numbers, find the longest subarray
	with an equal number of letters and numbers.

6. Count of 2s
	Write a method to count the number of 2s that appear in all the numbers
	between 0 and n (inclusively).
	Example:
		I: 25
		O: 9 --> 2, 12, 20, 21, 22, 23, 24, 25  --> Note 22 counts twice.

7. Baby Names
	Given a list of common baby names, design an algorithm to join synonymous
	names together, with combined frequncies. For example, [Jon, Jonny, John]
	should all be under a single instance.

8. Circus Tower
	Given a circus routine such that people stand on one another's shoulders,
	design an algorithm to find the maximum height of the tower with an 
	array of performers (with height, and weight properties). The only
	requirement for the tower is that the person on someone's shoulders
	must be both shorter and lighter than the person before them.

9. Kth Multiple
	Design an algorithm to find the kth number such that the only prime
	factors are 3, 5, and 7. Note that 3, 5, and 7 do not have to be 
	factors, but it should not have nay other prime factors.
	For example, the first several multiples would be (in order):
		1, 3, 4, 5, 7, 9, 15, 21

10. Majority Element
	A majority element is an element that makes up more than half of the item
	in an array. Given a positive integers array, find the majority eleemnt.
	If there is no majority element, return -1.
	Do this in O(N) tiem and O(1) space.
	Example:
		I: 1 2 5 9 5 9 5 5 5
		O: 5

11. Word Distance
	Givena large text file containing words. Given any two words, find the
	shortest distance (in terms of number of words) between them in the file.
	If the operation will be repeated many times for the same file, what
	optimizations can be made?

12. BiNode
	Consider a Node class that's purpose is to point to other Nodes.
	BiNode could be used to represent both a bin tree (when node1 is the
	lest node, and node2 is the right node) or a doubly linked list (node1
	is the previous and node2 is next).
	Implement a method to convert a binary search tree using BiNode into
	a doubly linked list.
	The values should be kept in order and the operations should be 
	performed in place.

13. Re-Space
	Given a document full of valid words such that the document has no
	spaces, no punctuation, and no capital letters, design an approach
	to simply first reinsert the spaces to make this doc readable.
	Note that some words are not validated.
	Example:
		I: jesslookedjustliketimherbrother
		O: jess looked just like tim her brother
	--`jess` and `tim` were not recgonized in our dictionary.

14. Smallest K
	Design an algorithm to find the smalled K numbers in an array.

15. Longest Word
	Given a list of words, write a program to find the longest word made 
	of other words in the list.
	Example:
		I: cat, banana, dog, nana, walk, dogwalker
		O: dogwalker

16. The Masseuse
	A popular masseuse receives a sequence of back-to-back appointment
	requests and is debating which ones to accept. 
	She needs a 15-minute break between appointments and therefore
	she cannot accept any adjacaent requests.
	Given a sequence of back-to-back appointment requests, find the
	optimal set the masseuse can honer.
	Return the minutes.
	Note optimal means highest total booked minutes.
	Note all requests are mutiples of 15, non overlapping, and immovable.
	Example:
		I: [30, 15, 60, 75, 45, 15, 15, 45]
		O: 180 minutes --> [30, 60, 45, 45]

17. Multi Search
	Given a string b and an array of smaller strings T, design a method
	to search b for each small string in T.

18. Shortest Suersequence
	Given two arrays, one shorter and one longer, find the shortest sub-
	array in the longer array that contains all the elements in the shorter.
	The items can appear in any order; Array S contains distinct elements.

19. Missing Two
	You are given an array with all the numbers from 1 to N, appearing
	exactly once, except for on number that is missing.
	How can you find the missing number in O(N) time and O(1) space?
	What if there were two numbers missing?

20. Continuous Median
	Numbers are randomly generated and passed to a method.
	Write a program to find and maintain the median values as new values
	are generated. 

21. Volume of Histogram
	Design an algorithm to compute the volume of water a histogram display
	box could hold given that each histogram bar has width 1.
	The display box does not have a fixed height.
	We are pouring water in between the bars of the histogram.

22. Word Transformer
	Given two words of equal length that are in a dictionary, write a method
	to transform one word into another word by changing only one letter at
	a time.
	The new word you get in each step must be in teh dictionary.
	Example:
		I: DAMP, LIKE
		O: DAMP --> LAMP --> LIMP --> LIME --> LIKE

23. Max Black Square
	Given a square matrix, where each cell is black or white, find the max
	subsquare such that all four borders are filled black.

24. Max Submatrix
	Given an NxN matrix of positive and negative ints, find the submatrix
	with the largest possible sum.

25. Word Rectable
	Given a list of millions of words, find the largest possible rectangle
	of letters such that every row forms a word (reading left to right
	and every column forms a word (reading top to bottom).
	The words need not be chosen consecutively from the list, but all rows
	must be the same length, and all columns msut be the same height.

26. Sparse Similarity
	Suppose that we have two documents, containing distinct integers.
	Upon finding the similar elements (the intersection), and the union
	(all elements together, but distinct), a similarity score can be 
	generated by dividing the size of the intersection by the size of the
	union.

	A similarity score is said to be `sparse` if any two arbitratily 
	selected documents are very likely to have similarity zero.
	Design an algorithm that returns a list of paris of document IDs and
	the associated similarity.
	Print only the pairs with similarity greater than zero.
	Empty documents are not printed.
	The union does not count intersecting elements twice.
	Example:
		I:	[1,2,3,4], [1,2,5,6]
		O: 0.33 --> 1/3 --> 2/6 --> len([1,2])/ len([1,2,3,4,5,6])

