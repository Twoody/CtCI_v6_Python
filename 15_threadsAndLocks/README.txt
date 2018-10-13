Threads in Java
	A "main" thread is created at execution time to run main().
	This thread is a unique object of the `java.lang.Thread` class.
	In java, a thread can be implemented in one of two ways:
		1. Implementing the java.lang.Runnable interface
		2. Extending the java.lang.Thread Class

Implementing the Runnable Interface in Java
	To create and use a thread using this interface, we do the following:
		1. Create a class that `implements` Runnable interface.
				An object of this class is a Runnable object.
		2. Create an object of type Thread by passing a Runnable object
			as an argument to the Thread constructor.
			The thread obj now has a Runnable obj that implements the run() method.
		3. The start() method is invoked on the Thread obj created in the prev step.

Extending the Thread Class
	Alternatively, we can create a thread by extending the Thread class.
	This means that wiill override the run() method, and the sublcass may also call
	the thread constructor explicitly in its constructor.

Extending vs. Implementing
	Java does not support multiple inheritances. Therefore, extending the Thread
	class means that the subclass cannot extend any other class.
		A class implementing the Runnable interface will be able to extend another
		class.
	A class might only be interested in being runnable, and therefore, inheriting
	the full overhead of the Thread class would be excessive.


Synchronization and Locks in Java
	Threads within a given process share the same memory space, which is both a positive and a negative.
	It enables threads to share data, which can be valuable. However, it also creates
	the opportunity for issues when two threads modify a resource at the same time.
	Java provides synchronization in order to control access to shared resources.

	The keyword `synchronized` and the `lock` form the basis for implemnenting
	synchronized execution of code.

	Synchronized Methods
		most commonly, we restrict access to shared resources through the use of
		the synchronized keyword. It can be applied to methods and code block, and
		restricts multiple threads from executing the code simultaneously on the 
		same obj.
	Synchronized Blocks

	Locks

Deadlocks and Deadlock Prevention
	

Questions
1. 
2. 
3. 
4. 
5. 
6. 
7. 
