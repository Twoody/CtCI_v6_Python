'''
10.	Poison
	You have 1000 jugs of water. 1 is poisoned.
	You have 10 test strips, which can be used to detect poison.
	A single drop of poison will turn the test strip positive permanently.
	You can put any number of drops on a test strip at once, and you can 
	reuse a test strip as many times as youd like.
	However, you can only run tests once per day, and it takes seven days
	to return a result. How would you figure out the poisoned bottle in as 
	few dats as possible?

Thoughts:
	Fact1: A jug is either poisoned or not poisoned --> Binary!
	Fact2: A strip is either positive or negative --> Binary!

	Propsition: Is it viable to encompass 1000 in 10?
	What I am getting at here is that we have 1000 possible "tests"
	that we need to run, and 10 test strips. If we did something 100 
	times for each test strip, that would be 1000 total cases, for example.
	And if we did something like 2^10, that would be 1024 possible test cases.

	This leads me to my thought on binary. We can represnet each number between
	0 and 1000 in binary with 10 spaces. As each number is a unique
	representation, we can in fact just look at the number, and correlate
	a `0` as a positive case, and a `1` as a false case.
	This also

	Let our strips and jug of water we are testing look like the following:
		strip1:	0, 2, 4, 6, 8, ..., 998					<-- 500 Test
		strip2:	0, 1, 4, 5, 8, 9, 11, ..., 998 	 	<-- 333 Tests
		strip3:	0, 1,2,3, 8,9,10,11, ..., 998			<-- 125 tests
		strip4:	0, 8, 16, 24, 32, ..., 999  			<-- 125 Tests
		strip5:	0, 1, ..., , 64, ...,       		<-- 64 tests
		strip6:	0 - 32, 64, 96, ..., 1024				<-- 33 tests
		strip7:	0 - 64, 128, 172, ..., 1024				<-- 17 tests
		strip8:	0 - 128, 256, 384, ..., 1024      	<-- 9 tests
		strip9:	0 - 256, 512, 768, 1024					<-- 5 tests
		strip10:	0 - 511										<-- 511 tests
									>>>bin(1000) == 11 1110 1000
	Now, let us make a jug poisoned  at random, say #17.
	17 in binary is 1111, or 10-bits --> 00 0000 1111
	That is, we would have strip1 through strip4 negative, and strip5
	through strip10 positive.

'''
