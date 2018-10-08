'''
	8. Loop Detections:
			Given a circular libked list, implement an algorithm that returns
			the node at the `beginning` of the loop.
			Definitions:
				Circular linked list is a "corrupt" linked list in which
				a nodes next pointer points to an earlier node, so as to make
				a loop in the linked list.
			Example:
				I: A->B->C->D->E->C (The same as C earlier)
				O: C
			Hints:
				50, 69, 83, 90
	
	Thoughts:
		We do not have a circular linked list...
		Do we just point tail to head and head to tail?
'''
import sys
sys.path.append('/Users/tannerleewoody/Workspace/google/CtCI/linkedLists/')
from LinkedList import LinkedList
from LLCircular import LLCircular

def q8():
	foo = LLCircular([1,2,3])
	assert foo.isCircular() == True
	assert str(foo) == "1 -> 2 -> 3 -> ..."
	foo.append(99)
	assert foo.isCircular() == True
	assert str(foo) == "1 -> 2 -> 3 -> 99 -> ..."
	bar = foo.get(0)
	assert bar is foo.head
	bar = foo.get(56) 		#56%4 == 0
	assert bar is foo.head
	bar = foo.get(55) 		#55%4 == 3
	assert bar is foo.tail
	foo.remove(0)
	assert foo.isCircular() == True
	assert str(foo) == "2 -> 3 -> 99 -> ..."

	foo2 = LLCircular([1,2])
	assert foo2.isCircular() == True
	foo3 = LinkedList([1,2])
	assert foo3.isCircular() == False
	foo3 = LinkedList([1])
	assert foo3.isCircular() == False

	print('q8.py: PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q8()

