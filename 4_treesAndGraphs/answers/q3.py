'''
3. List of Depths:
	Given a binary tree, design an algorithm which creates a linked list
	of all the nodes at each depth (e.g. if you have a tree with depth D,
	you will have D linked lists).

Thoughts:
	We can do a DFS that goes all the way down, and then it just `pop`s
	for next L.L. from the init. This would looke like:
	     
                .....................15...................
               /           \                 /           \
              5             9               20           31
             / \           / \             /  \         /  \
            /   \         /   \           /    \       /    \
           4     6       8    10         17    25     29    40
          / \   / \     / \   / \       / \   /  \   /  \   / \
         1   3     7                   16 18 21  26 28  30 35 45

	     
		INSERT: 19
                .....................15...................
               /           \                 /           \
              5             9               20           31
             / \           / \             /  \         /  \
            /   \         /   \           /    \       /    \
           4     6       8    10         17    25     29    40
          / \   / \     / \   / \       / \   /  \   /  \   / \
         1   3     7                   16 18 21  26 28  30 35 45



'''
import sys

def q3():
	
if __name__ == "__main__":
	q3()

