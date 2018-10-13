Intro
	These are not "tough" algorithmic questions but more sensible
	every day questions. Can you design the system?

Handling the Questions:
	1. Communicate
			Stay engaged. Ask questions. Be open about issues.
	2. Go Broad First
			Do not get excessively focued on one part. 
			Be like water, my friend.
	3. Use the Whiteboard
			Draw and illustrate your thoughts.
	4. Acknowledge Interviewer Concerns
			Do not brush off interviewer concerns. Validate them.
	5. Be Carefule with Assumptions
			An incorrect assumption can be a humongous change.
	6. State your assumptions explicitly
			When making assumptions, state them.
	7. Estimate when Necessary
			Do we have our data stored? How much will it cost to store?
	8. Drive
			Stay in the drivers seat.

Design: Step-By-Step
	Step1: Scope the Problem
	Step2: Make Reasonable Assumptions
	Step3: Draw the MAgic Components
	Step4: Indtify the Key Issues
	Step5: Identify the Key Issues

Algorithms that Scale: Step-By-Step
Step 1:	Ask Questions
Step 2: Make Believe
Step 3: Get Real
Step 4: Solve Probems

Key Concepts
	Horizontal vs. Vertical Scaling

	Local Balancer

	Database Denormalization and NoSQL

	Database Partitioning (Sharding)
		Vertical Partitioning
		Key-Based (or hash-based) Partitioning
		Directory-Based PArtitioning

	Caching

	Asynchronous Processing and Queues

	Networking Metrics
		Bandwidth
		Throughput
		Latency
		MapReduce

Considerations
	Failures
	Available and Reliability
	Read very vs. write heavy
	Secuirty

There is no "perfect" system

Questions
1. Stock Data
	1,000 client applications are calling your server for end-of-day
	stock price information (open, close, high, low). You may assume
	that you already have the data, and you can storie it in any format
	you wish. How would you design the client facing service that 
	provides the information to client applications?
	You are responsible for the development, rollout, and ongoing 
	monitoring and maintenance of the feed.
	Describe the different methods you considered and why ou would 
	recommend your approach.
	Your service can use any tech you wish, and you can distribute the
	information to the clint apps in any mechanism.

2. Social Network
	How would you design the data structures for a very large social 
	network like FB of Linkedin?
	Describe how you would design an alogorithm to show the shortest
	path between two people (e.g Me -> Bob -> Susan -> Jason -> You)

3. Web Crawler
	If you were desiging a web crawler, how would you avoid getting 
	into infinite loops?

4. Duplicate URLs
	You have 10 billion urls. How do you detect the duplicate documents?
	In this case, assume 'deuplicate' measn that the URLs are identical.

5. Cache
	Consider a web server for a  search engine. This system has 100 
	machines to respone to search queries, which may then call out to 
	anothe cluster of machines to get a result.
	The machine which responds to a given query is chosen at random, so
	you cannot guarantee that the same machien will always respond to 
	the same request.
	The method `processSearch(String query)` is expensive and required
	for inner cluster communication.
	Designe a chachine mechanism for the most recent queries.
	Explain how to update the chache when data changes.

6. Sales Rank
	An eCommerce company wishes to list the best-selling products, 
	overall and by category. For example, one product might be the 
	#1056th best-selling product under "Sports Equipment and the 24th 
	best-selling product under `Safety`. 
	Describe how to design this system.

7. Personal Financial Manager
	Explain how you would design a personal financial manager (like
	mint.com). This system would connect to your bank accounts, analyze 
	your spending habits, and make recommendations.

8. Pastbin
	Design a system like Pastebin, where a user can enter a piece of 
	text and get a randomaly generated utl to access it
