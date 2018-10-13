Intro

What Interviewer is Looking For:
	Not just an extensive list of test cases.
	Capture the Big Picture
		What is the software really about?
			Payments, shipments, stock, queues
	Knowing How the Pieces Fit Together
		Do you understand how software works?
		Do you understand how software fits int to the ecosystem?
	Organization
		Is there structure to the plan?
		WHAT is the structure to the plan?
		Make a structured approach to the different components of 
		the software in question.
	Practicality
		Reinstalling software is not practical.
		Rebooting the browser is not practival.
		But clicking a button to do the process for `rebooting`
		on the server (or just fixed...).
	
Test a Real World Object
	Step 1: Who will use it and why?
	Step 2: What are the use cases?
	Step 3: What are the bounds of use?
		Temperature, number of items, usage rate, commecial,
		industrial, ...
	Step 4: What are the stress/failure conditions?
		When is failure acceptable? What does failure mean?
		Is there an acceptable number of bad products?
	Step 5: How would you perform testing?
		Use cases defined as measured act, in order to scope 
		life expectancy of product.
	
Testing Software
	Step 1: Black or White Box Testing? Or both?
	Step 2: Who will use it and why?
	Step 3: What are the use cases?
		This is a converstaion to have with the intervierwer.
	Step 4: What are the bounds of use?
		Think on how the use cases will add new items to different 
		features, and think about how false positives/negatives.
	Step 5: What are the stress/failure conditions?
		What does failure look like, and what process gets user 
		out of failure? Error responses? Error handling?
	Step 6: What are the test cases? How to perform tests?
		Null and failure first. Then single instance. Then
		complex testing.

Testing a Functions:
	Step 1: Define a test case
		Null and Failure input tests. 
		Normal and extreme usage tests. 
		Strange vs clean input tests
	Step 2: Define the expected result
		Errors, correct output, and data handling.
	Step 3: Write test code
		Use asserts and naming conventions

Troubleshooting Questions:
	Step 1: Understand the Scenario
		How long ahs the user been experiencing this issue?
		Versions of contained software (jquery, ie, OS)
	Step 2: Break Down the Problem
		Create a flow chart of the issue for a use case.
	Step 3: Create Specific Manageable Tests


Questions
1. Mistake
		```
			unsigned int i;
			for (i=100; i>=0; i--)
				printf("%d\n", i);
		```
	What is the mistake?

2. Random crashes
	A single threaded, C standard lib application is crashing, but
	crashing in different places. What programming errors could be 
	causing this crash? How would you tests each one?

3. Chess Tests
	Given a Piece class and a function `canMoveTo(int x, int y)`, we
	are able to find if a chess piece can move to a spot on the board
	or not. How can we test this method?

4. No Tests Tools
	How would you load test a webpage w/out using any test tools?

5. Test a Pen -- How would you test a pen?

6. Test an ATM -- Show how to test an ATM in a distributed banking system?

