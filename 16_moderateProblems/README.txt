Questions

1. Number Swapper
	Write a function to swap a number in place (that is, with temp vars.).

2. Word Frequencies
	Design a method to find the frequency of occurrences of any given word 
	in a book. What if we were running this algorithm multiple times?

3. Interaction
	Given two straight line segments (represented as a start point and and 
	end point), compute the point of intersections, if any.

4. Tic Tac Win
	Design an algorithm to figure out if someone has won a game of tic-tac-toe.

5. Factorial Zeroes:
	Write an algorithm which computes the number of trailing zeros 
	in `n` factorial.

6. Smallest Difference
	Given 2 arrays of integers, compute the pair of values (one value in each
	array) with the smalled (non-negative) difference.
	Return the difference.
	Example:
		I: {1,3,15,11,2}, {23,127,235,19,8}
		O: 3 --> From 11 and 8

7. Number MAx:
	Write a method that finds  the max of 2 numbers.
	You should not use if-else or any comparison operators.

8. English Int
	Given any int, print and English phrase that describes the int.
	For example: "One Thousand, Two Hundered Thirty Four"

9. Operations
	Write methods to implement the multiply subtract, and divide operations.
	Focus on integer input and integer output only.

10. Living People
	Given a list of ppl with their birth and death years, implement a method
	to compute the year with the most number of people alive.
	You may assume that all ppl were borne between 1900 & 2000.
	If a person was alive during any portion of that year, they should be
	inlcuded in that years count.
	For example:
		Person(birth=1908, death=1909 is inlcuded in the counts for both 
		1908 and 1909

11. Diving Board
	Given a bunch of planks, design a diving board by placing the planks
	end-to-end. There are two tyupes of palnsk, one of length `shorter` and 
	one of length `longer`. You must use exactly K planks of wood.
	Write a method to generate all possible lengths for the diving board.

12. XML Encoding
	Since XML is very verbose, you are given a way of encoding it where each 
	tage gets mapped to a pre-defined integer value.
	The language/grammar is as follows:
		Element       --> Tag Attributes END Children End
		Attribute     --> Tag Value
		END           --> 0
		Tag           --> some predefined mapping to int
		Value         --> string value
	For example, take following XML:
		<family lastname="McDowell" state="CA">
			<person firstname="Gayle">Some Message</person>
		</family>
	We would have the following returned:
		1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0
	Write code to print the encoded version of an XML element

13. Bisect Squares
	Given two squares on a 2-dimensional palne, find a line that would 
	cut these two squares in half. Assume that the top and bottom sides 
	of the square run parallel to the x-axis.

14. Best Line
	Given a two dimensional graph, with points on it, find a line which 
	passes the most number of points.

15. Master Mind
	The game of Master Mind is played as follows:
		1. The computer has 4 slots.
		2. Each computer slot contains a ball.
		3. A ball is Red, Yellow, Green, or Blue
		4. The user needs to guess the solution of colors.
		5. The user is returned a `1` if correct guess.
		6. If the user guesses a correct color, but wrong slot, a `2` is ret.
		7. If the user guesses an incorrect color, `0` is returned.
	Design the game and write a program to solve it.

16. Sub Sort
	Given an  array of integers, write a method to find indices m and n
	such that if you sorted elements m through n, the entire array would
	be sorted. Minimize n -m to find the smallest such sequence.
	Example:
		I: 1, 2, 3, 4, 10, 11, 7, 12, 6, 7, 16, 18, 19
		O: (3,9) --> 4, 10, 11, 7, 12, 6, 7

17. Contiguous Sequence
	You are given an array of ints (positive and engative).
	Find the contiguous sequence with teh largest sum.
	Return the Sum:
	Example:
		I: 2, -8, 3, -2, 4, -10
		O: 5 --> {3, -2, 4}

18. Pattern Matching
	You are given 2 strings: `pattern` and `values`.
	`pattern` consists of just hte letters `a` and `b`, such that `a` and `b`
	represent a specific pattern to themselves.
	For example:
		"catcatgocatgogo" == "aababb"
	Write a method to determine if `values` is somehow equivalent to `pattern`.

19. Pond Sizes
	Given an int matrix represening a plot of land, such that the value at 
	mXn is the height above sea level for that plot.
	A value of zero indicates water.
	A pond is an area of water connected:
		1. vertically, 
		2. horizontally, or 
		3. diagonally
	The Size of the pond is the total number of connected water cells.
	Write a method to compute the sizes of all ponds in the matrix.

20. T9
	On original cell phones, users typed on a numberic keypad and the phone
	would provide a list of words that matched thses numbers.
	Each digit mapped to a set of 0-4 letters.
	A dictionary is provided for allowed words.
	The mapping is as follows:
		1: [SPECIAL CHARACTERS] --> Comma, period, apostrophe.
		2: [a,b,c]
		3: [d,e,f]
		4: [g,h,i]
		5: [j,k,l]
		6: [m,n,o]
		7: [p,q,r,s]
		8: [t,u,v]
		9: [w,x,y,z]
		0: []
	Implement an algorithm to return a lsit of matching words, give a sequence.

21. Sum Swap
	Given 2 arrays of ints, find a pair of values such that swapping them
	would make the arrays equal one another.
	Example:
		I:	[4,1,2,1,1,2], [3,6,3,3]
		O: [1,3]

22. Langton's Ant
	An ant is sitting on an infinite grid of white and black squares.
	It traverses the squares as such:
		1. Initially facing right
		2. W square:
				flip the color of the square, turn 90 deg. clockwise,
				and move forward 1 unit.
		3. B squlare:
				Flip the color of the square, turn 90 deg. counter clockwise,
				and more forward 1 unit.
	Write a program to simulate the first K moves that the ant makes 
	and print the final board as a grid.
	Note that you are not provided with teh data struct to represent the grid.
	The only input to your method is K.
	You should print the final grid and return nothing.
	The Method signature might be soemthign like `printKMoves(int K)`.

23. Rand7 from Rand5
	Given a method that generate a random number between 0 and 4, write a 
	method to generate a random number between 0 and 6.

24. Pairs with Sum
	Design an algorith to find all pairs of ints in an array such that the 
	pair of ints sums to a specific value.

25. LRU Cache
	Design and build a 'least recently used' cache.
	The cache evicts the least recently used item.
	The cache should map from keys to values and be init'ed w/ a max size.
	When the cache is full, it should evict the least recently used item.

26. Caclulator
	Given an arithemetic equation consisting of:
		1. positive integers
		2. Addition
		3. Subtraction
		4. Multiplication
		5. Division
	, compute the result.
	Example:
		I: "2*3+5/6*3+15"
		--> "6 + 5/6*3 + 15" --> "6 + 0.333*3 + 15" --> "6 + 2.5 + 15" 
		--> "23.5"
		O: 23.5

