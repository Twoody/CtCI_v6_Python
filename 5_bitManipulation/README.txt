*************************************************************************
****************************  BIT MANIPULATION  *************************
*************************************************************************
Be ready to manipulate bits by hand and in code.

TEST PROBLEMS:
	 _______________________________________________
	|                    |                          |
	|	1. 0110 + 0010		|	7.		1101 >> 2			|
	|	2. 0011 + 0010		|	8.		1101 ^ 0101			|
	|	3. 0110 - 0011		|	9.		0110 + 0110			|
	|	4. 1000 - 0110		|	10.	0100 * 0011			|
	|	5. 0011 * 0101		|	11.	1101 ^ (~1101)		|
	|	6. 0011 * 0011		|	11.	1011 & (~0 << 2)	|
	|____________________|__________________________|

Bit Tricks and Tips:
	Multiplying by 2 is equivalent to shifting by 1.
	Multiplying by 4 is equivalen to shifting by 2 ...
	binary1 XOR binary2 such that binary2 is the negated value
		of binary1 IS ALWAYS 1.
	
	The following expressions are useful in bit manipulation.
	DO NOT MEMORIZE THEM.
	But, grok them.

		 ____________________________________________
		|              |              |              |
		| X^ 0s  = x	|	x & 0s = 0	|	x | 0s = x  |
		| x ^ 1s = ~x	|	x & 1s = x	|	x | 1s = 1s |
		| x ^ x  = 0	|	x & x  = x	|	x | x  = x  |
		|______________|______________|______________|

Two's Complement and Negative Numbers
	Computers store integers in two's complement representation.
	A positive number is represented as itself while a negative 
	number is represented as the two's complement of its 
	absolute value (with a 1 in its sign bit to indicate that a
	negative value). 

	Let N be a number of bits to be allowed for storage.
	The twos complement of a N-bit number is the complement of 
	the number with respect to 2^N.

	For example, take -3 as a 4-bit integer.
	We want the complement with respect to 2^3, which is 8.
	The complement of 3 (the absolute value of -3) with respect
	to 8 is 5. (Because 5+3 is 8???)
	5 in binary is 101. Therefore, -r in binary as a 4-bit int
	is 1101, with the first sign letting us know it is negative.
	In other words, the binary rep of -K as an N-bit number is
		concat(1, x^(N-1)-K)
	
	Another way to look at this is that we inver the bits in the
	positive representation and then add 1.
	3 is 011 in binary. Flip the bits to get 100 and add 001.
	With 101, prepend the sign bit to get 1101.

	Just remember that there is typically signed zero's esp. with
	IEEE. For example: 1000 == -0 AND 0000 == +0

Arithmetic vs Logical Right Shift (>> operator)
	In a logical right shift, we shift the bits and put a 0 in the
	significant bit. Indicated with >>
	In arithmetic shift, we shift the values, but retain the
	signed bit.

*************************************************************************
****************************  Answers to Test  **************************
*******************************  Problpems  ******************************
*************************************************************************
Answers to Test Problems:
	1. 1000 == 0110 + 0010
		Simple movement of bits

	2. 0101 == 0011 + 0010
		Simple movement of bits

	3. 0011 == 0110 - 0011
		"0011 + XXXX == 0110"

	4. 0110 + XXXX == 1000
		0010 == XXXX

	5. 3 * 5 --> 0011 * 0101 -->   0011
							           x 0101
						            _________
				      	      		 0011
				      	      		00000
				      	      	  001100
				      	      +	 0000000
				      	      ____________
				      	          0001111
		1111

	6. 0011 * 0011 --> 0011 + 00110 --> 1001
		(1+2)*(1+2) --> 3*3 --> 8+1 --> 1001

	7.	1101 --> 0110 --> 0011
	8. 1101 ^ 0101 --> EXCLUSIVE OR --> XOR
		1XOR0 --> 1 \
		1XOR1 --> 0  \ --> 1000  
		0XOR0 --> 0  /
		1XOR1 --> 0 /

	9. 0110 + 0110 --> 0110 * 10 --> 01100

	10. 0100 * 0011 --> 0011 * 0100 --> 1100

	11. 1111 --> XOR with Negated
		1101 ^ (~1101)  --> 1101 ^ 0010 --> 1111

	12. 1000
		1011 & (~0 << 2) --> 1011 & (~0000 <<2) --> 1011 & (1111 <<2)
		--> 001011 & (111100) --> 001000 --> 1000 --> 8
	
More problems:
		5. 6 * 6 --> 0110 * 0110 -->   0110
							              x 0110
							            _________
					      	      		 0000
					      	      		01100
					      	      	  011000
				   	   	      +	 0000000
				      		      ____________
				      		          0100100

		100100 == 0+0+4+0+0+32 == 36


*************************************************************************
*******************************  QUESTIONS  *****************************
*************************************************************************

1. INSERTION
	You are given two 32-bit numbers, N and M. You are also given two bit
	positions, i and j.
	Write a method to insert M into N such that M starts at bit j and ends
	at bit i.
	You can assume that the bits j throug hi jave enough space to fit all
	of M. That is, if M = 10011, you can assume that there are at least
	5-bits between j and i.
	You would not, for example have j=3 and i=2 because M could noy fully
	fit between bit 3 and bit 2.
	Example:
		I: N = 10000000000, M = 10011, i=2, j=6
		O: N = 10001001100

2. Binary to String
	Given a real number bewtten o and 1 that is passed in as a double,
	print the binary representation.
	If the number cannot be rep'ed accurately in binary with at most 32
	characters, print 'ERROR'.

3. Flip Bits to Win
	You have an int and you can flip exactly one bit from a 0 to a 1.
	Write code to find the length of the longest sequesnce of 1s you 
	could create.
	Example:
		I: 1775 --> 110111011111
		O: 8    -->       1

4. Next Number
	Given a positive int, print the next smallest and the next largest 
	number that have the same number of 1 bits in their binary 
	representation.

5. Debugger
	Explain what the following code does:
		( ( n & (n-1) ) == 0 )
	1000 & (1000 - 1) --> 1000 & 0111 --> 0000  --> True
	0001 & 0001-1 --> 0000 & 0000 --> 0000      --> True
	1111 & 1111-1 --> 1111 & 1110 --> 1110      --> False

	I suspect it is just looking to see if it is odd :D

G. Conversion
	Write a function to determine the number of bits you would need to
	flip to convert int A to int B.
	Example:
		I: (29, 15) --> (11101, 011111)
		O: 2

7. Pairwise Swap:
	
8.

