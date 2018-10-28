*************************************************************************
*********************************  TREES ********************************
*************************************************************************

Types of Trees:
	A tree can be thought of as a starting root node, with nodes added
	one after the other. These addes nodes are child nodes. And each
	node has zero or more child nodes.

	Trees cannot contain cycles.

	Trees vs. Binary Trees
		A binary tree is a tree in which each node has up to two children.
		Not all trees are binary trees.
		Some binary tree definitions are in context to repeated values,
		and if they are allowed or not.

	Balanced vs. Unbalanced
		While many trees are balances, not all are.
		ASK YOUR INTERVIEWER IF IT IS BALANCED.

		Common types of balanced trees are red-black trees and AVL trees.

	Complete Binary trees (CBT)
		A CBT is a binary tree in which ever level of the tree is fully
		filled, except for perhaps the last level.
		To the extent that the last level is filled, it is filled left to
		right.

	Full Binary Tree (FBT)
		a FBT is a binary tree in which every node has either zero or two
		children.
		That is, no nodes have only one child.

	Perfect Binary Tree:
		A PBT is BOTH an FBT and a CBT.
		All leaf nodes will be at the same level, and this level has the
		maximum number of nodes.
		Note that PFT's are rare in interviews and in real life.

Binary Tree Traversal
	Prior to INTERVIEW you should be comfortable implemeting:
		in-order
		post-order
		pre-order
	, tree traversals.

	In order Traversal:
		Visit the left branch, then the current node, and finally, the 
		right branch.

	Pre-Order Traversal
		Visits the current node before its child nodes
		The root is always the first node visited.

	Post-Order Traversal:
		Visits the current node AFTER its child nodes.
		The root is always the last node visited.

Binary Heaps (min and max heaps)
	Max heaps
		Equivalent to min heaps, but elements are in descending order
		rather than ascending order.
	
	Min Heaps
		A CBT (totally filled other than the rightmost elements on the 
		last level) where each node is smaller than its children.

		The root is the min element in the tree.
		
		Two key operations: INSERT and EXTRACT_MIN
		Insert:
			Start by inserting the element at the bottom.
			Insert at the rightmost spot so as to maintain the CBT property.
			Then, we fix the tree by swapping the new element with its
			parent, until we find an appropriate spot for the element.
			We essentially bubble up the min element.
		Extract_min:
			Finding the min element of a min-heap is easy:
				ITS ALWAYS AT THE TOP.
			The tricker part is how to remove it.
				Remove the min element and swap it with the last element in 
				the heap (bottom right element).
				Bubble down this element, swapping it with one of its 
				children until the min heap property is restored.
			Swapping either left or right child dpeneds on the values.
			There is no inherent ordering between the left and right 
			elements, but youll need to take the smaller one in order to
			maintain the min-heap ordering.
			This algorithm will also take O(log n).

Tries (Prefix Trees)
	Variant of an n-ary tree in which characters are stored at each node.
	Each path down the tree may represent a word.

	The * nodes (aka null nodes) are often used to indicate complete words.
	For example, the fact that there is a * node under MANY is a complete
	word.
	The existence of the MA path indicates there are wrods that start with
	MA.
	The actual implementation of these * nodes might be a special type of
	child (such as a terminatingTrieNode, inherited from TrieNode).
	Or, we could use just a boolean flag `terminates` within the parent
	node.
	A node in a trie could have anywhere from 1 through ALPHABET_SIZE+1 
	children (or 0 through ALPHABET_SIZE, if boolean flag instead of a *
	node).
	Trie's are used to store english words:
		prefix, root, suffix
	
*************************************************************************
********************************* GRAPHS ********************************
*************************************************************************
	
A tree is actually a type of graph.

A graph is a collection of nodes with edges between (some of) them.
	Graphs can be either directed or undirected.
		Directed edges are like a one-way street.
		Undirected edges are like a two-way street.
	Graph might consist of multiple isolated subgraphs
	Connected graphs
	Acyclic Graphs and Cyclic Graphs
		no cycle vs cycle

Connected Graph
	If there is a path between every pair of vertices

Adjacency List
	This is the most commone way to represent a graph.
	Every vertex (i.e. node) stores a list of adjacent vertices.
	In an undirected graph, an edge like (a,b) would be stored twice:
		once in a's adjacent vertices
		once in b's adjacent vertices

Adjacency Matrices
	An adjacency matrix is an NxN boolean matric (where N is the node cnt).
	A true value at m[i][j] indicates an edge from node i to node j.
	In an undirected graph, and adjacency matrix will be symmetric.
	In a directed graph, an adjacecny matric will not always be symmetric.

	The same graph algs that are used on adjacency lists (BFS, etc.) can
	be performed with adjacency matrices, but they may be somewhat less
	efficient.
	In the adjacency list representation you can easily iterate through
	the neghbors of a node.
	In an adjacecny matric representation, you will need to iterate all the
	nodes to identify a node's neighbor.

Graph Search
	DFS and BFS
		BFS uses Queues
		DFS uses

Additional Terms:
	Topological Sort
	Dijkstra's Algorithm
	AVL Trees
	Red-Black Trees


*************************************************************************
******************************  QUESTIONS  ******************************
*************************************************************************

1. Route Between Nodes
	Give a direcred graph, deisng an algorithm to find out whether there
	is a route between two nodes.

2. Minimal Tree
	Given a sorted (increasing order) array with unique integer elements, 
	write an algorithm to create a binary tree with minimal height.

3. List of Depths:
	Given a binary tree, design an algorithm which creates a linked list
	of all the nodes at each depth (e.g. if you have a tree with depth D,
	you will have D linked lists).

4. Check Balanced
	Implement a function to check if a binary tree is balanced.
	For the prupose of this question, a balanced tree is defined to be a 
	tree such that the height of the two subtrees of any node never differ
	by more than one.

5. Validate BTS
	Implement a function to check if a binary tree is a binary search tree.

6. Successor
	Write an algorithm to find the `next` node (i.e. in-order successor) of
	a given node in a BST. You may assume that each node has a link to its
	parent.

7. Build Order
	You are given a list of projects and a list of dependencies (which is a
	list of pairs of projects, where the second project is depenedent on
	the first project). All of a project's dependencies must be built 
	before the project is. 
	Find a build order that will allow the projects to be built. If there is 
	no valid build order, return an error.
	EXAMPLE:
		I: projects: a,b,c,d,e,f
			dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)
		O: f,e,a,b,d,c

8. First Common Ancestor
	Design an algorithm and write code to find the first common ancestor
	of two nodes in a Binary Tree.
	Avoid storing additional nodes in a data strucutre.
	Note:
		This is not necessarily a BST

9. BTS Sequences
	A Binary search tree was created by traversing through an array from 
	left to right and inserting each eelemtn. Given a BST with distinct 
	element, print all possible arrays that could have led to this tree.
	EXAMPLE:
		I: { '2':[1,3], '1':[], '3'[] }
		O: {2,1,3}, {2,3,1}

10. Check Subtree
	T1 and T2 are two very large binary trees, with T1 much bigger than T2.
	Create an alogirhtm to determine if T2 is a subtree of T1.
	A tree T2 is a subtree of T1 if there exists a node n in T1 such that 
	the subtree of n is identical to T2.
		That is, if you cut off the tree at node, n, 
		the two trees would be identical.

11. Random Node
	You are implementing a binary tree class from scrach which in addition 
	to `insert()`, `find()`, and `delete()` has a methode getRandomNode() 
	which returns a random node from the tree.
	All nodes should be equally likely to be chosen. 
	Design and implement an aglorithm to getRandomNode, and explain how you 
	would implement the rest of the methods.

12. Paths with Sums
	You are given a BT in which each node contains an integer value (which 
	might be positive or negative). 
	Design an alogorithm to count the total paths that sum to a given value.
	The path does not need to start or end at the root of a leaf, but it 
	must go downwards (traveling only from parent nodes to child nodes).
