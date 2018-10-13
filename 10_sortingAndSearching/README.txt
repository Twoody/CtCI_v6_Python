Intro
		"Given a very large array of Person objects, 
		sort the people in increasing order of age."
	We are given two interesting bits of knowledge here:
		1. It is a large array, so efficiency is very important
		2. We are sorting based on ages, so we know the values are in
			a small range.

	By scanning through the various sorting algorithms, we might notice
	that bucket sort (or radix sort) would be a perfect candidate for
	this algorithm. In fact, we can make the buckets small (just 1 year
	each) and get O(n) running time.

Common Sorting Algorithms
	Name	|	RunTime	|	Memory
	Bubble Sort	|	O(n^2)	|	O(1)
	Selection Sort	|	O(n^2)	|	O(1)
	Merge Sort	|	O(n logn)	|	Depends
	Quick Sort	|	O(n logn)	|	O(logn)
	Radix Sort	|	O(kn)	|	???

Searching Algorithms
	Sorted Arrays:
		Binary Search
		Jump Search
		Interpolation Search
		Exponential Search
			Extends binary search
		Fibonacci Search
			Jump at fib. intervals
		Ubiquitous Binary Search
	Unsorted Arrays:
		???
	Regular Expressions:
		https://swtch.com/~rsc/regexp/regexp1.html
	Lists in List:
		Sublist Search	|	O(m*n)
			"Is one list contained in the other list?"

	Binary Search
		Start with finding bound in the middle.
		Set middle as a lower and higher bound, and find next middle.
	Jump Search -- O(sqrrt(n)) -- O(1)
		Iterate through array at an index rate of sqrrt(size(Arr))
	Interpolation Search
		Sorted array of uniformly distributed values.
		Linear search using a probe position formula
	Exponential Search


Questions
1. Sorted Merge
	You are given two sorted arrays, A and B.
	A has a large enough bugger to hold B.
	Merge A into B.

2. Group Anagrams
	Write a method to sort an array of strings such that all
	anagrams are next to each other.

3. Search in Rotated Array

4. Sorted Search, No Size

5. Sparse Search

6. Sort Big File
	20GB file w/ one string per line. How to sort?

7. Missing Int
	

8. Find Duplicates

9. Sorted Matrix Search

10. Rank from Stream

11. Peaks and Valleys

