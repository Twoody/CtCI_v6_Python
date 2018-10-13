Intro:
	If you express knowledge in DB's, expect questions on them.

SQL: Syntax and Variations
	sql questions can range from very humbling keyword usage to
	very simple select questions.

	Explicit vs Implicit Joins:
		```
			SELECT * FROM Foo INNER JOIN Bar on Foo.id = Bar.id
			SELECT * FROM Foo JOIN Bar WHERE Foo.id = Bar.id
		```
		Do not omitt the join. Just because something looks a little easier,
		it can easily omit some reliability and readability.
		For example, is it a cross join, outter join, right join?
	
	Denomalized vs. Normalized DB's
		Normalized are meant to reduced redundancy.
			Foreign keys are typically used between tables.
			Expensive joins are then present.
		Denormalized are meant to optimize read time.
			Offers highly scalable system w/ redudnant, EZ to acceess data.

	SQL statements:
		Inner vs. Cross vs. Right vs. Left
			
		... FROM ( SELECT ... WHERE)
			Example of selecting from a subquery.
			A Subquery is an sql query nested in a larger query.
		GROUP BY
			Group aggregate functions by a column/field.
		INTEGER PRIMARY KEY
			How most tables are with `id`.
	
	Keys
		Super
			A set of one or more key(s) that can be used to identify a record 
			uniquely in a table.
			Examples: Primary, Alternate, and Unique
		Candidate
			A set of or or more fields/columns that can identify a record 
			uniquely in a table.
			Example, coursecode.
		Primary
			A set of one or more fields/column of a table that uniquely identify
			a record in a DB table.
			Cannot accept null nor duplicate values.
			Only one candidate key can be a primary key.
		Alternate
			A candidate key that is not a primary key.
		Composite/Compound
			A combo of more than one fields/column which can be a cadidate or
			primary key.
		Unique
			A set of one or more fields/column that uniquely identify a record
			in a DB table.
			This is a primary key that can have Null, but still no duplicates.
		Foreign
			A fieldthat is a primary key for another table.
			Might have multiple instances of Foreign keys depending on 
			relationship.

Design your Database: Samll
	Step 1: Handle Ambiguity
	Step 2: Define the Core Objects
		OOD approach where tablename is Class and fields are Properties.
		Always have Keys.
	Step 3: Analyze Relationships
		1to1, 1toM, MtoM?
	Step 4: Investigate Actions
		`KISS List` --> List shared, List completed, Dates changed. ...

Design your Database: Large
	Joins are slow. Be sure to denormalize your data. 


Questions:
1. Multiple Apartments
	Write query to get a list of tenants who are renting more than one
	apartment.

2. Open Requests
	Write query to get a list of all buildings and the number of open 
	requests (Requests in which status equals `Open`).

3. Close All Requests
	Write a query to SET all `open`s to `closed` where buildingNumber == 11

4. Joins
	What are the different types of joins? Explain them with situational
	dependencies.

5. What is denormalization? Pros and cons?

6. Entity Relationship Diagram
	Draw an entity relationship diagram for a DB w/ companies, people, and
	professionals (ppl who work for companies).

7. Design Grade DB
	Write a DB for students grades. Write a query to get a lit of honor roll
	students (top 10%), sorted by their grade point average.




