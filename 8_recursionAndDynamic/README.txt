"Design an algorithm to compute the nth *BLAH*", might imply recursion.

How to Approach
	Recursive solutions are built off of solutions to subproblems.
	
	Bottom-Up Approach
		Start with a base case, then build. For example,
			empty array -> len(a) ==1 --> len(a) ==2 --> ... --> len(a) == n
	
	Top-Down Approach
		First think about how we can divide our problem into subproblems.
		Be careful of overlap between cases.
	
	Half-and-Half Approach
		Divide the data in half, just cause.
		For example, binary search and merge sort.
	
Recursive vs. Iteratice Solutions
	Recursion can be spcae inefficient.
	Each recusive call adds a new layer to the stack, which means it uses
	O(n) memory for a depth of n.

	Thus, implement a recursive algothim iteratively.
	All recursive algorithms can be implemented iteratively although
	sometimes, the code to do so is much more complex.
	DISCUSS THIS WITH YOUR INTERVIEWER!

Dynamic Programming & Memoization
	Dynamic programming is mostly just a matter of taking a recursive
	algorithm and finding the overlapping subproblems (that is, the 
	repeated calls).
	You then cache those results for fucutre recursive calls.

	For example, consider the Fib Sequence and computing the nth iteration.
	Start with the recursive aspect (Which we know is bad for O time).
	In Python3, with an i7 processor, `time python3 fib.py`, with this
	O(2^n) approach will take 22 seconds:
		Tanners-MacBook-Air:randoms tannerleewoody$ time python3 fib.py 
		63245986
		real	0m22.811s
		user	0m22.647s
		sys	0m0.065s

	By adding a `memoryD` (aka hash table) param, we can significantly
	improve this!

		Tanners-MacBook-Air:randoms tannerleewoody$ time python3 fib.py 
		63245986
		real	0m0.042s
		user	0m0.026s
		sys	0m0.010s

	This memory approach is not always intuitive. 
	Let us break it down in cases:
		A: fib(4, []) --> 4 not in `memo`; memo[4] = fib(3, []) + fib(2, [])
		
		B: fib(3, []) --> 3 not in `memo`; memo[3] = fib(2, []) + fib(1, [])

		C: fib(2, []) --> 2 not in `memo`; memo[2] = fib(1, []) + fib(0, [])
		
		D: fib(1) --> 1
		E: fib(0) --> 1
	******************** Back up stack ********************
		C: return memo[2]
		B: memo[3] = C + fib(1, [])
		B: memo[3] = C + D
		A: memo[4] = B + fib(2, [])
		A: memo[4] = B + C


QUESTIONS:

1. Triple Step
	A child is running up a staircase with n steps and can hop either 1, 2,
	or 3 steps at a time.
	Implement a method to count how many posible ways the child can run 
	up the stairs.

2. Robot in a Grid
	A robot is sitting on the upper left corner of a grid with r rows and
	c columns. The robot can only move right and down. Certain cells are
	unaccessible. 
	Design an algorithm to find a path for the robot from the top left 
	to the bottom right.

3. Magic Index
	A magic index in an array is such that `A[i] == i`.
	Given a sorted array of distinct integers, write a method to find a
	magic index, if one exists, in array A.
	Follow up:
		What if the values are not distinct?

4. Power Set
	Write a method to return all subsets of a set.

5. Recursive Multiply
	Write a recursive function to multiply two pos. int's w/out using
	the * operator. You can use addition, subtraction, and bit shifting.
	But use the minimal number of operations.

6. Tower of Hanoi


7. Permutations without Dups
	Write a method to compute all permutations of a string of unique chars.

8. Permutations with Dups
	Write a method to compute all permutations of a string whoe chars are
	not necessarily unique.
	List of permutations should not have duplicates.

9. Parents
	Implement an algorithm to print all valid and properly opend/closed
	combinations of n pairs of parentheses.
	Example:
		I: 3
		O: ((())), (()()), ()()()

10. Paint Fill
	Implement the `paint fill` function that one might see on many
	image editing programs. Input is 2D array of colors, a point, and a 
	new color. Output is new array of filled colors.

11. Coins
	Given an infinite number of quearters, dimes, nickles, and pennies,
	write code to calculate the number of ways of representing n cents.

12. Eight Queens
	Write an algorithm to print all ways of arranging 8 queens on an
	8x8 chess board so that none of them share the same row, col, or
	diagonal. In this case, 

13. Stack of Boxes
	With n boxes of widths w, heights h, and depths d: Implement a method
	to compute the height of the tallest possible stack.
	The height of the stack is the sum of the heights of each box.
	The boxes cannot be rotated and can only be stacked on top of one
	another IFF each box in the stack is strictly larger than the box
	above it in width, height, and depth.

14. Boolean Evaluations
	Consider a boolean expression consisting of the symbols 0, 1, &, |, ^, and
	a desired boolean result value `result. 0 == False and 1 == True.
	Implement a function to count the number of ways of parenthesizing the 
	expression such that it evaluats to `result`.
	Example:
		countEval( "1^0|0|1", False" ) --> 2
		countEval( "0&0&0&1^1|0", True ) --> 10


