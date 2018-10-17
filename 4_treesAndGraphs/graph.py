class Node:
	def __init__(self, value, pathsTo=None, pathsFrom=None):
		self.value     = value
		if pathsTo is None:
			self.pathsTo = []
		else:
			self.pathsTo = pathsTo
			#for node in pathsTo:
			#	node.pathsFrom.append(self)
		if pathsFrom is None:
			self.pathsFrom = []
		else:
			self.pathsFrom = pathsFrom
			for node in pathsFrom:
				node.pathsTo.append(self)
	def __eq__(self, other):
		if self.pathsTo != other.pathsTo:
			return False
		elif self.pathsFrom != other.pathsFrom:
			return False
		elif self.value != other.value:
			return False
		else:
			return True
	def __str__(self):
		return str(self.value)
	def getPathsTo(self):
		return [x.value for x in self.pathsTo]
	def hasPathTo(self, other):
		''' Does current node have a path to other node  '''
		''' TODO: Stop infinite loops...'''
		if other in self.pointsTo:
			return True
		for i in self.pointsTo:
			if hasPathTo(i, other):
				return True
		return False

class DirectedGraph:
	def __init__(self, points=[]):
		self.points = points
	def __iter__(self):
		for i in self.points:
			yield i.value
	def __eq__(self, other):
		return self.points == other.points
	def addnode(self, node):
		self.points.append(node)
		return node
	def addpath(self, node1, node2):
		for node in self.points:
			if node is node1:
				node.pathsTo.append(node2)
				if node2 not in self.points:
					self.points.append(node2)
				return node2
		raise TypeError('ERROR: Graph.addpath(): args[0] NOT FOUND')
	def connect(self, node1, node2):
		''' Path which goes both ways '''
		found = False
		for node in self.points:
			if node == node1:
				node1.pathsTo.append(node2)
				if found == False:
					found = True
				else:
					return True
			elif node == node2:
				node2.pathsTo.append(node1)
				if found == False:
					found = True
				else:
					return True
		raise ValueError('ERROR: ONE OR BOTH ARGUMENTS NOT FOUND')

	def haspath(self, n1, n2):
		''' BFS to find path from n1 to n2    '''
		''' Returns False IFF not path           '''
		''' Returns True IFF path '''
		for ni in n1.pathsTo:
			if ni is n2:
				return True
		for ni in n1.pathsTo:
			if ni is n1: #Avoid infinite loop
				continue
			ret = haspath(ni, n2)
			if ret == True:
				return True
		return False

	def getpath(self, n1, n2):
		''' Returns [] IFF not path           '''
		''' Returns [n0, n1, ..., n] IFF path '''
		paths = {}
		paths[0] = [ [n1,n2] ]
		paths[1] = [ [n1, n1.pathsTo[0], n2], [n1, n1.pathsTo[1], n2] ]
		paths[2] = [ [n1, n1.pathsTo[0], n1.pathsTo[0].pathsTo[0], n2] ]
			
		for ni in n1.pathsTo:
			parr = [n1, ni, n2]
			if ispath(parr) == True:
				return parr
			for nj in ni.pathsTo:
				parr = [n1, ni, nj, n2]
				if ispath(parr):
					return parr
				for nk in nj.pathsTo:
					parr = [n1, ni, nj, nk, n2]
					if ispath(parr):
						return parr
		return False
	def ispath(self, nList):
		''' Validates path existence from array of Nodes (aka `nList`)'''
		''' O(k) '''
		if len(nList) < 2:
			return False
		i = 0
		j = 1
		curr = nList[i]
		nex  = nList[j]
		while j < len(nList):
			paths = curr.pathTo
			if nex not in paths:
				return False
			i += 1
			j += 1
			curr = nList[i]
			nex  = nList[j]
		return True
			

			
	def printgraph(self, args=None):
		if args is None:
			args = {}
		isquite=False
		if 'isquite' in args and args['isquite'] == True:
			isquite = True
		s = ''
		for n in self.points:
			s += str(n.value) + ': [' + ', '.join(n.getPathsTo()) + ']\n'
		if isquite == False:
			print(s)
		return s

if __name__ == "__main__":
	g  = DirectedGraph()
	a  = Node('Alabama')
	b  = Node('Boston')
	c  = Node('Clemson')
	d  = Node('Detroit', [c])
	e  = Node('Everest', [a,b], [c,d])
	g.addnode(a)
	g.addnode(b)
	g.connect(a, b)
	g.addnode(c)
	g.addnode(d)
	g.addnode(e)
	p = "Alabama: [Boston]\nBoston: [Alabama]\nClemson: [Everest]\nDetroit: [Clemson, Everest]\nEverest: [Alabama, Boston]\n"
	assert g.printgraph({'isquite':True}) == p
	tempG = DirectedGraph()
	tempG.addnode(a)
	tempG.addnode(b)
	tempG.addnode(c)
	tempG.addnode(d)
	tempG.addnode(e)
	assert tempG == g
	assert isinstance(g, DirectedGraph) == True
	assert isinstance(a, Node) == True
	print("****************************************")
	print("*******  graph.py: PASSED TESTS  *******")
	print("****************************************")
	print("")
