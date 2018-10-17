'''
1. Route Between Nodes
	Give a direcred graph, deisng an algorithm to find out whether there
	is a route between two nodes.

Thoughts:
	Need to init Node class.
	A Node needs property `connections`, which is an array of other nodes
	that __node is connected to.
	If we iterate backwards with `connectedFrom`, we will efficiently use
	BFS to find a connection from end point to start point.
	We can then return this, but reversed, to have an actual path.
'''
import sys
sys.path.append('/Users/tannerleewoody/Workspace/google/CtCI/4_treesAndGraphs/')
from graph import DirectedGraph

def generatePaths(g, n1, n2):
	paths ={}
	return paths

def bfs(g, start, end):
	''' Given a start node, traverse to the end node '''
	explored = []
	queue    = [ [start] ]
	while queue:
		path = queue.pop(0)
		node = path[-1]
		if node not in explored:
			neighbors = g[node]
			for neighbor in neighbors:
				new_path = list(path)
				new_path.append(neighbor)
				queue.append(new_path)
				if neighbor == end:
					return new_path
			explored.append(node)
	return []

def q1():
	g = {
		'A':['B', 'C', 'D'],
		'B':['C'],
		'C':[],
		'D':['E', 'F'],
		'E':[],
		'F':['A']
	}
	paths = []
	x = bfs(g, 'A', 'A')
	y = bfs(g, 'C', 'A')
	assert x == ['A', 'D', 'F', 'A']
	assert y == [] #Does Not Exist
	print('q1: PASSED ALL TESTS')

if __name__ == "__main__":
	q1()

