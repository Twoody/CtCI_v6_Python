*************************************************************************
****************************  OBJECT ORIENTED  **************************
*********************************  Design  ******************************
*************************************************************************

OOD questions require a candidate to sketch out the classes and methods 
to implement techincal problems or real-life objects.
These problems give -- or at least are believed to give -- an interviewer 
insight into your coding style.

These questions are not so much about requrgitating design patterns as they are about demonstrating that you understand how to create elegant, maintaiblable, OOD code.
Poor performance on this type of question may raise serious red flags.

How To Approach
	1. Handle Ambiguity
	2. Define the core Objects
	3. Analyze Relationships
	4. Investigate Actions

	Handle Ambiguity:
		OOD questions are often intinteionally vague in order to test whether or not you will make assumptions or if youll ask clarigying questions.
		After all, a developer who just codes something without understanding what she is expected to create wastes the company's time and money, and may create much more serious issues.
		
		When being asked an OOD questions, go through the six W's:
			1. Who		3. When		5. How
			2. What		4. Why		6. Where

		For example, suppose you were asked to describe the ood for a 
		coffee maker.
		Is it industrial/personal? Where does it live? What does the 
		coffee maker do? How does it do it? What does the coffee maker
		need to operate correctly? Who commands the coffee maker?
	
	Define the Core Objects:
		In regards to our coffee maker again, core objects are things like
		Filters, Grinder, Beans, Water, Pot, Electricity, Operator, Scale.
	   ____________________________________________________________________
	  |Filer.isClean()	| Filter.getCount()  |	Electricity.hasCurrent()  |
	  |Water.getLevel()	| Pot.hasCoffee()		|	Electricity.measureCurr() |
	  |Beans.isGround()	| Pot.isClean()		|	Filter.hasBeans()         |
	  |Beans.getGrind()	| Pot.empty()			|	Scale.weigh(foo) 			  |
	  |Beans.setGrind()	| Beans.putInTrash()	|	Grinder.grind(beans)      |
	  |__________________|____________________|____________________________|

		Notice the use of `getters` and `setters`, as well as the usage of
		the suffix `is` and `has`.
		Notice the use of action verbs like `put`, `empty`, `grind`, `weigh`.
		Finally, we want to think of the datatypes for each value.
		Are we expected to inspect each bean, such that all beans are ground
		to our precise level? Or are we just going to dump a weight of beans
		into the grinder, grind, and now have a case representation on how
		these beans have been ground?
		This is one of the nice things about computers, we could in fact
		have a job put in place to grind each individual bean. However, in
		the real world, griding each individual bean is idiotic and a huge
		waste of time.

	Analyze Relationships
		Which objects are members of which other objects?
		Do any objects inherit from any others?
		Are relationships many-to-many or one-to-many?
		We need to be careful here. Just because our filter is wet, does
		not mean that we have used the filter. Some people `bloom` their
		beans. And just because the Pot is full of coffee does not mean that
		we cannot make more coffee. But, we cannot make more coffee if the
		Water is all used and if the Electricity is off. 
		Thus, there is a one to many relationship between the Water and
		Electricity that effects the Filter, Pot, Beans, Scale, etc.
		And then we have a relationship between the temperature of the water
		and the beans:
			w1 = Water.getTemp() # == 100 #Celsius
			w2 = Water.getTemp() # == 1   #Celsius
			b  = Filter.getBeans() #float of weight of beans in metric
			while(w1.getLevel()):
				while(w1.getTemp() < 100):
					w1.increaseHeat()
				CoffeeMaker.pump(w1) #Putting water on beans/filter via a pump
			'''
			def CoffeeMaker.pump():
				f = CoffeeMaker.getFilter()
				w = CoffeeMaker.getWater()
				if not f.hasFilter():
					raise Error('Needs filter!')
				elif not f.hasBeans():
					#Viable option for tea
				elif not f.isClean():
					raise Error('filter is dirty ::vomit::')
				#More error messages and feedback for user...
				else:
					#passed all error msg's and opening valve for water
					#to go on the filter and beans.
					CoffeeMaker.releaseValve()
			'''

	Investigate Actions
		Make a few flow charts to address the use case of your code
		and how it will in fact operate.
		For example:
			An Operator puts a Filter in the CoffeeMaker,
			fills the Water with cold tap water,
			weighs out their Beans on the Scale,
			grinds the Beans in the Grinder,
			puts Beans in the Filter,
			presses `Start` button on CoffeeMaker.
			CoffeeMaker notifies Operator Water is all used,
			Opeartor pours themselves a cup of coffee.

Design Patterns:
	Design patterns are usually beyond the scope of an interview.
	The inteviewer is more intersted in our knowledge and capabilities.
	That beins said, make sure that the SINGLE RESPONSIBILITY PRINCIPLE is
	always being followed, as well as the Factory Method.

	Singleton Class:
		Ensures that a class has only one instance and ensures access 
		to the instance through application. This is useful in cases 
		where you have a 'global' object with exactly one instance.
		
		In terms of practical use Singleton patterns are used in logging, 
		caches, thread pools, configuration settings, device driver objects.
		For example, reading a config file at bootup, which needs to be 
		encapsulated, can be done by encapsulation in a Singleton.
		Another example is a similar Log class that all objects use, to
		log their output, erros, etc.
		This Log class should only be called once, and then encapsulated
		in a Singleton, where we know if some other thread or process is
		accessing it.
		
		In Python, we can accomplish this with a decorator or a metaclass.
		A metaclass is reccommended.
	
	Factory Method:
		Offers an interface for creating an instance of a class, with its 
		subclasses desciding which class to instantiate.
		You might want to implement this with the Creator class being abstract
		and not providing an implementation for the Factory method.
		Or, you could have the Creator class be a concrete class that provides
		an implementation for the Factory method.
		In this case, the Factory method would take a parameter representing 
		which class to instantiate.


*************************************************************************
****************************  BIT MANIPULATION  *************************
*************************************************************************
1. Deck of Cards
	Design the data structure for a generic deck of cards.
	Explain how you would subclass the data struct. to implement BlackJack.

2. Call Center
	There is a call center with employee positions:
		Respondent, Manager, Director
	A phone call must first go to a Respondent. 
	IFF the Respondent cannot handle the call, it is sent to Manager.
	IFF not Manager.isFree() or not Manager.canHandle(problem),
		then send problem to Director.
	Design the classes and data structures for this problem.
	Implement a method `dispatchCall` which assigns a call to the
	first available employee.

3. Jukebox
	Design a musical jukebox using OOD.

4. Parking Lot
	Designe a parking lot using OOD.

5. Online Booke Reader
	Design the data struct for an online book reader system.

6. Jigsaw
	Implement an NxN jigsaw puzzle. Design the data struct and explain
	an algorithm to solve the puzzle.
	You can assume that you have a `fitsWith()` method, which when 
	passed two puzzle pieces, returns True or False.

7. Chat Server
	Explain how you would design a chat server.
	In particular, provide details about various backend components, classes
	and methods. What would be the hardest problems to solve?

8. Othello
	Othello is played as follows:
		Each Othello pices is white on one side and black on the other.
		When a piece is surrounded by its opponents on both the left and
		right sides (or top and bottom), it is said to be captured, and 
		flipped to the other side.
		On your turn, you must capture at least one of your opponents pieces.
		The games ense when a User has no more valid moves.
		Who ever has the most pieces wins.
	Implement OOD for Othello

9. Circular Array
	Implement a CircularArray class that supports an array-like data struct
	which can be efficiently `rotated`. 
	If possible, the class should use a generic type (also called a 
	template), and should support iteration via standard `for i in foo`.

10. Minesweeper
	Implement a Mine Sweeper game with OOD.

11. File System 
	Explain the data structs and algorithms that you would use to design an 
	in-memory file system. Illustrate with code examples where possible.

12. HAsh Tables
	Design and implement a hash table which uses chaining (LinkedList's)
	to handle collisions.


