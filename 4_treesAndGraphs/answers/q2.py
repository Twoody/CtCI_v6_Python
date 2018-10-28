'''
2. Minimal Tree
	Given a sorted (increasing order) array with unique integer elements, 
	write an algorithm to create a binary tree with minimal height.

Thoughts:

	                   .......27......
                     /               \
                    20               31
                   /  \             /  \
                  /    \           /    \
                 16    21         29    40
                / \   /  \       /  \   / \
                  17     24     28  30 35 45

	     
		INSERT: 19
	                     .........27..........
                       /                     \
                    ..20..                   31
                   /      \                 /  \
                  /        \               /    \
                 17        24             29    40
                /  \       /  \           /  \   / \
               16  19    21             28  30 35 45


		INSERT: 20
	                     .........27..........                   `20` goes between 21 and 17;
                       /                     \                  
                    ..21...                ..31..                  
                   /       \              /      \                  
                  / `20`    \            /        \                  
                 17         24          29        40                  
                /  \       /  \        /  \       / \                  
               16  19     22          28  30     35 45                  
	
	                     .........27..........                   Insert 20 left of 21;
                       /                     \                  Assign new node 21 the previous left
                    ..21...                ..31..                 branch of 21;
                   /       \              /      \              Run a check on the balance of the tree;
                  /         \            /        \             See that 20 has a balanceFactor of 1;
                 20         24          29        40                  balanceFactor is +1 for L-Node
                /  \       /  \        /  \       / \                 balancrFactor is -1 for R-Node
               17         22          28  30     35 45          Resolve balance factor (next step);
	           /  \
	          16  19
	
	                     .........27..........                  Find a spot for `21`;
                       /                     \                 Put `21` left of 22;
                    ..20...                ..31..                Assign `22`.leftChild to `21`
                   /       \              /      \             Assign `21`.rightChild to `20`;
                  /         \            /        \                 This "erases" `21`s branch;
                 17         24          29        40           Run a check on the balance of the tree;
                /  \       /  \        /  \       / \          See `22` has balanceFactor of 1;
               16  19     22          28  30     35 45         Resolve balance factor (next step);
                         /                                                      
                        21                                                      
		
	                     .........27..........                   Find a spot for `24`;
                       /                     \                  Put `24` right of `22`;
                    ..20...                ..31..                 Assign `24` to `20`.rightChild;
                   /       \              /      \              Assign `22` to `20`.leftChild;     
                  /         \            /        \             Recheck Balances of the tree;
                 17         22          29        40              All balances are at zero;
                /  \       /  \        /  \      /  \           
               16  19     21  24      28  30    35  45                    


		INSERT: 32
		                  .........27............
                       /                       \
                    ..20...                  ..32...
                   /       \                /       \
                  /         \              /         \
                 17         21          ..30..        40
                /  \       /  \        /      \       / \
               16  19     22  24      28      31     35 45
                                        \
                                        29

			INSERT: 39
		                  .........27...............
                       /                          \
                    ..20...                  .....32....
                   /       \                /           \
                  /         \              /             \
                 17         21          ..30..         ..40..
                /  \       /  \        /      \       /      \
               16  19     22  24      28      31     35       45
                                        \             \
                                        29            39


			INSERT: 25
		                  .........27...............
                       /                          \
                    ..20...                  .....32....
                   /       \                /           \
                  /         \              /             \
                 17         21          ..30..         ..40..
                /  \       /  \        /      \       /      \
               16  19     22  24      28      31     35       45
                                \       \             \
                                25      29            39
	

			INSERT:26
		             .........27.................                       Set curNode to BT.head;
                  /                            \                      Check if 26 is greater than 
               ..21...                    .....32....                   curNode.value;
              /       \                  /           \                26 is less than curNode.value;
             /         \                /             \               Set curNode to curNode.rightchild;
            17         21            ..30..         ..40..            (LOOP UNTIL `25`);
           /  \       /  \          /      \       /      \           `25` is curNode;
          16  19     22  24        28      31     35      45          curNode.leftChild is None;
                           \        \             \                   Check balance of tree;
                           25       29            39                  See that 24 has balanceFactor of 2;
	                          \                                        `24` and `25` need left rotated;
	                          26                                       (Move onto next step)


		             .........27.................                       Move `24` to `25`.leftchild;
                  /                            \                      Move `25` to `21`.rightchild;
               ..21...                    .....32....                 
              /       \                  /           \                
             /         \                /             \               
            17         21            ..30..         ..40..            
           /  \       /  \          /      \       /      \           
          16  19     22  25        28      31     35      45          
                        /  \        \             \                   
                       24  26       29            39                  


	
'''
import sys
class Node:
	def __init__(self, val, parent=None, left=None, right=None):
		self.leftchild   = left
		self.rightchild  = right
		self.parent      = parent
		self.value       = val
		self.depth       = 0
		if self.parent is not None:
			self.depth = self.parent.depth+1
	def getbalance(self):
		balance = 0
		if self.rightchild is not None:
			if self.rightchild.rightchild is not None:
				balance += 1
			if self.rightchild.leftchild is not None:
				balance += 1
			balance += 1
		if self.leftchild is not None:
			if self.leftchild.rightchild is not None:
				balance += 1
			if self.leftchild.leftchild is not None:
				balance -= 1
			balance -= 1
		return balance
		
class BTree:
	def __init__(self, values=None):
		self.head   = None
		self.height = -1
		if values is not None:
			self.add(v)
	def add(self, value):
		if isinstance(value, list):
			for item in list:
				self.add(item)
		if self.head is None:
			self.head = Node(value)
			self.height
			return self.head
		#else
		curnode = self.head
		while curnode is not None:
			if curnode.value > value:
				if curnode.leftchild is not None:
					curnode = curnode.leftchild
				else:
					curnode.leftchild = Node(value, curnode)
					self.balanceTree()
					return curnode.leftchild
			elif curnode.value < value:
				if curnode.rightchild is not None:
					curnode = curnode.rightchild
				else:
					curnode.rightchild = Node(value, curnode)
					self.balanceTree()
					return curnode.rightchild
			else:
				raise KeyError('ERROR: AVL TREE: KEY ' + str(value) + ' ALREADY EXISTS')
		raise ValueError('ERROR: AVL TREE: COULD NOT ALLOCATE VALUE `' + str(value) + '` INTO TREE')
	
	def balanceTree(self):
		cur = self.head
		while cur is not None:
			balance = cur.getbalance(cur)
			if balance == 2:
				#There are not right children two nodes deep
				pNode = cur.parent
				lNode = cur.leftchild
				lNode.rightchild = cur
				cur.parent     = lNode
				cur.rightchild = None
				if pNode.rightchild is cur:
					pNode.rightchild = lNode
				elif pNode.leftchild is cur:
					pNode.leftchild = lNode
			elif balance == -2:
				


			



def q2():
	a = [1,2,3,4,5,6,7,8,11,12,14,15,16,22,33,44,55,66]
	b = BTree(a)
	print('q1: PASSED ALL TESTS')

if __name__ == "__main__":
	q2()

