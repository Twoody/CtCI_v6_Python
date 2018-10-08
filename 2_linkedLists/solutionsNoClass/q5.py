'''
	5. Sum Lists
			Given two numbers represented by a linked list, where each
			node contains a single digig, write a function that adds the
			two numbers and returns the sum as a linked list.
			The digits are stored in reverse order, such that the 1's
			digit is at the head of the list.
			Example:
				Input: (7-> 1 -> 6) + (5 -> 9 -> 2).
					That is, 617 + 295.
				Output: 2 -> 1 -> 9.
					That is, 912.
			FOLLOW UP:
				Suppose the digits are stored in forward order. 
				Repeat the above problem.
				EXAMPLE
					Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).
						That is,617 + 295. 
					Output: 9 -> 1 -> 2.
						That is, 912.
			Hints: 
				#7, #30, #71, #95, #109
'''
def printList(mlist):
	i = len(mlist)
	s = ""
	while (i >=0):
		i -= 1
		s += mlist[i]
	print (s)

def addList(list1, list2):
	''' lists are representory of an actual number '''
	''' For example, [9,5,2] == 295 '''
	len1 		= len(list1)
	len2 		= len(list2)
	ret		= []
	carriage	= 0
	if len1 >= len2:
		biggest = len1
	else:
		biggest = len2
	for i in range(0, biggest):
		if list1[i]:
			x = list1[i]
		else:
			x = 0
		if list2[i]:
			y = list2[i]
		else:
			y = 0
		if x+y+carriage>=10:
			ret.append(x+y+carriage-10)
			carriage = 1
		else:
			ret.append(x+y+carriage)
			carriage = 0
	return ret


def q5():
	assert addList([], []) == []
	assert addList([0], [0]) == [0]
	assert addList([1], [1]) == [2]
	assert addList([0,1], [0,1]) == [0,2]
	assert addList([1,1], [4,2]) == [5,3]
	assert addList([4,2], [1,1]) == [5,3]
	assert addList([9,5,2], [7,1,6]) == [6,7,8]
	assert addList([], []) == []
	assert addList([], []) == []
	print('PASSED ALL TESTS')
	return True

if __name__ == "__main__":
	q5()

